from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "is_superuser",
    ]
    list_display_links = ["id", "username", "email"]
    search_fields = ["username", "email", "first_name", "last_name"]
