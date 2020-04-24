from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.RoomTyte, models.Facility, models.HouseRule, models.Amenity)
class ItemAdim(admin.ModelAdmin):
    """Item Admin Definition"""

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """RoomAdmin Admin Definition"""

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
