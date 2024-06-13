from django.contrib import admin
from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "slug",
        "status",
        "priority",
        "created_at",
        "updated_at",
    ]
    list_display_links = ["id", "title", "slug"]
    list_filter = ["status", "priority", "created_at"]
    search_fields = ["title", "body"]
    ordering = ["created_at", "updated_at"]
    show_facets = admin.ShowFacets.ALWAYS
