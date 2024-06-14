from django.contrib import admin
from actions.models import Action


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "direction",
        "description",
        "user",
        "action_type",
        "created_at",
    ]
    list_display_links = ["id", "direction"]
    list_filter = ["direction", "action_type", "created_at"]
    search_fields = ["direction", "description"]
    ordering = ["created_at"]
    show_facets = admin.ShowFacets.ALWAYS
