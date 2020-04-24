from django.db import models
from core import models as core_models

# Create your models here.
class Reservation(core_models.TimeStampedMode):
    """Reservation model definition"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"
    STATUS_CHICES = [
        (STATUS_PENDING, "pending"),
        (STATUS_CONFIRMED, "confirmed"),
        (STATUS_CANCELED, "canceled"),
    ]

    status = models.CharField(
        max_length=12, choices=STATUS_CHICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    checK_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.room} - {self.check_in}"
