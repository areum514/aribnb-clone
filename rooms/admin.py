from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#modeladmin-options
# Register your models here.
@admin.register(models.RoomTyte, models.Facility, models.HouseRule, models.Amenity)
class ItemAdim(admin.ModelAdmin):
    """Item Admin Definition"""

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):  # StackedInline이것도 있다~ 모양만 다르게 보이는 것 !
    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """RoomAdmin Admin Definition"""

    inlines = (PhotoInline,)
    # more infomation is in dijanfo document!
    fieldsets = (
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths",)}),
        ("Basic Info", {"fields": ("name", "description", "country", "city", "price")}),
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
    ordering = ("price",)
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
        "count_amenities",
        "count_photos",
        "total_rating",
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
    # serch 'QuerySet API'
    def count_amenities(self, obj):
        print(obj.amenities.all())
        return obj.amenities.count()

    # count_amenities.short_description = "hihi"

    def count_photos(self, obj):
        return obj.photos.count()

    raw_id_fields = ("host",)


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):

        return mark_safe(f'<img width=50px src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"
