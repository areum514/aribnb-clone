from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """" Custom User Model"""

    GENDER_MALE = "M"
    GENDER_FEMALE = "W"
    GENDER_CHOICES = ((GENDER_MALE, "Male"), (GENDER_FEMALE, "Female"))

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_CHOICES = ((LANGUAGE_KOREAN, "korean"), (LANGUAGE_ENGLISH, "english"))

    CURRENCY_USD = "usb"
    CURRENCY_KRW = "krw"
    CURRENCY_CHICES = ((CURRENCY_KRW, "KRW"), (CURRENCY_USD, "USD"))

    # 여기서 만든 것을 장고가 form 으로 만들어줘 그리고 장고는 database에 Migration과 함께 이 form에 필요한 정보를 요청할 거야
    """admin.py에다가 
    @admin.register(models.User)
    class CustomUserAdmin(admin.ModelAdmin):
        pass
    """
    # # in django document you can search what tpye of model fields you will use!
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    bio = models.TextField(blank=True)  # null=True ignore that empty~
    birthdate = models.DateField(blank=True, null=True)

    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, null=True,default=LANGUAGE_KOREAN)

    currency = models.CharField(choices=CURRENCY_CHICES, max_length=3, null=True,default=CURRENCY_KRW)

    superhost = models.BooleanField(default=False)
