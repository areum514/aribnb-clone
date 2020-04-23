from django.db import models

# Create your models here.
class TimeStampedMode(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField()
    updated = models.DateTimeField()

