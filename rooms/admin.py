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

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )

    list_filter = (
        "instant_book",
        "city",
        "country",
    )
    # serch django doucument "MOdelAdmin options"
    search_fields = ("city", "host__username")


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
