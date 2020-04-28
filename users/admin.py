from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    # list_display = ("username", "gender", "superhost")
    # list_filter = ("superhost", "gender")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    list_display = (
        "username",
        "avatar",
        "gender",
        "bio",
        "birthdate",
        "language",
        "currency",
        "superhost",
        "is_staff",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
