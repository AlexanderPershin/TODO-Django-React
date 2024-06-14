from django.conf import settings
from django.db import models


class Action(models.Model):
    class ActionType(models.TextChoices):
        USER = "USER", "User"
        SYSTEM = "SYSTEM", "System"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="actions",
        on_delete=models.CASCADE,
    )
    action_type = models.CharField(
        max_length=6,
        choices=ActionType,
        default=ActionType.SYSTEM,
    )
    direction = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["-created_at"]),
        ]
        ordering = ["-created_at"]
