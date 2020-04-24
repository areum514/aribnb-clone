from django.db import models
from core import models as core_models
from users import models as user_models

# Create your models here.
class Review(core_models.TimeStampedMode):
    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanline = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()

    # user를 삭제하면
    name = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.review} - {self.room}"
