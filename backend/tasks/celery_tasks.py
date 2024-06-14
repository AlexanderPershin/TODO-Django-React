from __future__ import absolute_import, unicode_literals
import json
import logging
from datetime import datetime, timedelta, timezone

import socketio
from django.db.models import Q
from django.core.mail import send_mail
from celery import shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from celery.worker import strategy


@shared_task
def check_todos():
    from tasks.models import Task
    from sockets.sockets_client import sio

    strategy.logger.setLevel(logging.WARNING)
    logger = get_task_logger(__name__)

    logger.debug(f"Checking if some tasks expired or about to be expired...")

    try:
        query_start_date = datetime.now(timezone.utc) + timedelta(hours=1)
        query_end_date = datetime.now(timezone.utc) + timedelta(hours=2)
        about_expired_query = (
            Q(end_date__gte=query_start_date)
            & Q(end_date__lte=query_end_date)
            & ~Q(is_expired=True)
        )
        about_to_expired_tasks = list(Task.objects.filter(about_expired_query))
        for task in about_to_expired_tasks:
            try:
                sio.connect(f'ws://websocket:8765')
            except socketio.exceptions.ConnectionError:
                logger.info('Already connected to socket server')

            message = {
                'event_type': 'task_changed',
                'task_id': str(task.id),
                'status': 'expired_soon',
                'message': f'Task {task.title} will expire soon'
            }
            data = {
                'user_id': str(task.owner.id),
                'message': message,
            }
            sio.emit('django_message', json.dumps(data))

            send_mail(
                f"Task {task.title} expires in less than an hour",
                f"Check your task {task.title}",
                "noreply@todo_app.com",
                [task.owner.email],
                fail_silently=False,
            )
    except Exception as e:
        logger.error(f"Error notifying about soon expireing tasks: {e}", exc_info=True)

    try:
        query_start_date = datetime.now(timezone.utc) - timedelta(hours=1)
        query_end_date = datetime.now(timezone.utc)
        expired_query = (
            Q(end_date__gte=query_start_date)
            & Q(end_date__lte=query_end_date)
            & ~Q(is_expired=True)
        )
        expired_tasks = list(Task.objects.filter(expired_query))
        for task in expired_tasks:
            try:
                sio.connect(f'ws://websocket:8765')
            except socketio.exceptions.ConnectionError:
                logger.info('Already connected to socket server')

            message = {
                'event_type': 'task_changed',
                'task_id': str(task.id),
                'status': 'expired',
                'message': f'Task {task.title} expired'
            }
            data = {
                'user_id': str(task.owner.id),
                'message': message,
            }
            sio.emit('django_message', json.dumps(data))

            task.is_expired = True
            task.save()
            send_mail(
                f"Task {task.title} expired",
                f"Task {task.title} expired",
                "noreply@todo_app.com",
                [task.owner.email],
                fail_silently=False,
            )
    except Exception as e:
        logger.error(f"Error updating expired tasks: {e}", exc_info=True)
