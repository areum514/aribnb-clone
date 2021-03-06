from django.db import models

# reverse는 url name을 필요로 하는 funcion으로 url 을 return 함
from django.urls import reverse
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models
from cal import Calender


class AbstractItem(core_models.TimeStampedMode):
    """Abract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    """RoomType Model Definition"""

    class Meta:
        verbose_name_plural = "Room Types"


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):
    """Facility Model Definition"""

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    class Meta:
        verbose_name_plural = "House Rules"


class Photo(core_models.TimeStampedMode):
    """Photo Model Definition"""

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="room_photos")
    # Room 이 지워지면 관련된 사진다 지워지게..!!
    # Room이라고 하면 이 class를 밑으로 내려야 되는데 그냥 스트링 선언해주면 알아서 찾아서 매칭해준다...역시 파이션...
    room = models.ForeignKey("Room", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


# Create your models here.
class Room(core_models.TimeStampedMode):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField(help_text="how many bedroom do you need?")
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # CASCADE 폭포수 여기서 USER를 지우면 그거와 관련된 ROOM을 을 다 지우겠다 폭포수 효과
    # on_delete 는 1대 다만 사용..!
    host = models.ForeignKey(
        user_models.User, related_name="rooms", on_delete=models.CASCADE
    )

    room_type = models.ForeignKey(
        RoomType, related_name="rooms", on_delete=models.SET_NULL, null=True
    )
    amenities = models.ManyToManyField(Amenity, related_name="rooms", blank=True)
    facilities = models.ManyToManyField(Facility, related_name="rooms", blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name="rooms", blank=True)

    def save(self, *args, **kwargs):
        self.city = self.city.capitalize()
        super().save(*args, **kwargs)

    # super(ModelName, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rating_average()
            return round(all_ratings / len(all_reviews), 2)
        return 0

    def get_absolute_url(self):
        return reverse("rooms:detail", kwargs={"pk": self.pk})

    def first_photo(self):
        try:
            (photo,) = self.photos.all()[:1]
        except ValueError:
            return None
        return photo.file.url

    def get_next_four_photos(self):
        photos = self.photos.all()[1:5]
        return photos

    def get_calenders(self):
        calender = Calender(2020, 5)
        next_month = Calendar(2019, 12)
        return [this_month, next_month]
