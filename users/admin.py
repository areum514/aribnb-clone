from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rooms import models as room_model
from . import models


class RoomInline(admin.TabularInline):  # StackedInline이것도 있다~ 모양만 다르게 보이는 것 !
    model = room_model.Room


# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin"""

    inlines = (RoomInline,)
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
        "first_name",
        "last_name",
        "email",
        "email_verified",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
    list_filter = UserAdmin.list_filter + ("superhost",)
