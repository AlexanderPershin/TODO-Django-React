from __future__ import absolute_import, unicode_literals
import json
import logging
from datetime import datetime, timedelta, timezone

from django.db.models import Q
from celery import shared_task
from celery.schedules import crontab
from celery.utils.log import get_task_logger
from celery.worker import strategy


@shared_task
def check_todos():
    from tasks.models import Task

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
            # TODO: Notify by email if task expires in an hour
            # TODO: Send socket event to that user
            logger.debug(
                f"Sending email notification to {task.owner.username} informing that {task.title} is about to be expired"
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
            # TODO: Notify by email that task have expired
            # TODO: Send socket event to that user
            logger.debug(
                f"Sending email notification to {task.owner.username} informing that {task.title} is expired"
            )
            task.is_expired = True
            task.save()
    except Exception as e:
        logger.error(f"Error updating expired tasks: {e}", exc_info=True)
