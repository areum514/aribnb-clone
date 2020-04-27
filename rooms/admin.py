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

    # more infomation is in dijanfo document!
    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        ("Basic Info", {"fields": ("name", "description", "country")}),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

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
        "host__superhost",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "country",
        "city",
    )
    # serch django doucument "MOdelAdmin options"
    search_fields = (
        "city",
        "host__username",
    )
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
