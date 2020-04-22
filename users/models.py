from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """ Custom User Model"""

    avatar = models.ImageField(null=True)

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, "Male"), (GENDER_FEMALE, "Female")]

    gender1 = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    gender = models.IntegerField(choices=GENDER_CHOICES, default=0, blank=True)
    # gender = models.BooleanField(choices=GENDER_CHOICES, default=0)
    bio = models.TextField(default="", blank=True)  # null=True ignore that empty~
    # 여기서 만든 것을 장고가 form 으로 만들어줘 그리고 장고는 database에 Migration과 함께 이 form에 필요한 정보를 요청할 거야
    """admin.py에다가 
    @admin.register(models.User)
    class CustomUserAdmin(admin.ModelAdmin):
        pass
    """
    # # in django document you can search what tpye of model fields you will use!
