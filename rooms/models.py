from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedMode):
    """Abract Item"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomTyte(AbstractItem):
    """RoomType Model Definition"""

    pass


class Amenity(AbstractItem):
    """Amenity Model Definition"""

    pass


class Facility(AbstractItem):
    """Facility Model Definition"""

    pass


class HouseRule(AbstractItem):
    """HouseRule Model Definition"""

    pass


# Create your models here.
class Room(core_models.TimeStampedMode):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.ImageField()
    beds = models.IntegerField()
    bedrooms = models.ImageField()
    baths = models.ImageField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    # CASCADE 폭포수 여기서 USER를 지우면 그거와 관련된 ROOM을 을 다 지우겠다 폭포수 효과
    # on_delete 는 1대 다만 사용..!
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomTyte, on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity)
    facility = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
