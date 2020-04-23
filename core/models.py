from django.db import models

# Create your models here.
class TimeStampedMode(models.Model):
    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # 이 모델이 데이타베이스에 추가 되는 것을 원치 않아서 abstract = True 모델이긴 하지만 데이터베이스에 나타나지 않느 model을 의미함
    class Meta:
        abstract = True
