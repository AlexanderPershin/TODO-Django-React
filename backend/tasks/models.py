from datetime import time
from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Task(models.Model):
    class Status(models.TextChoices):
        INACTIVE = "INACTIVE", "Inactive"
        ACTIVE = "ACTIVE", "Active"
        REFINEMENT = "REFINEMENT", "Refinement"
        COMPLETE = "COMPLETE", "Complete"
        CANCELLED = "CANCELLED", "Cancelled"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"
        CHRITICAL = "CHRITICAL", "Chritical"

    title = models.CharField(max_length=250)
    body = models.TextField(max_length=1000)
    slug = models.SlugField(
        max_length=300,
        unique=True,
        null=True,
        blank=True,
    )

    status = models.CharField(max_length=10, choices=Status, default=Status.ACTIVE)
    priority = models.CharField(
        max_length=10, choices=Priority, default=Priority.MEDIUM
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["status"]),
            models.Index(fields=["priority"]),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            strtime = "".join(str(time()).split("."))
            string = "%s-%s" % (strtime[7:], self.title)
            self.slug = slugify(string)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.owner.username}'s todo {self.title}"
