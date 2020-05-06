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
    email_confirmed=models.BooleanField(default=False)
    email_secret=models.CharField(max_length=120,default="",blank=True)
    """ email과 password를 이용해서 user가 새 계정을 생성하면 email_secret에  아무 숫자나 넣을꺼야
    이 랜덤으로 생성한 숫자들을 이메일에 보내는거야 링크를 통해서 user가 그 링크를 클릭하면  (아마 /verify/(랜덤으로 생성된 숫자)) 이 랜덤한 숫자들을 받을 수 있는 view를 만들어서 
    email_secret값이 이 숫작 ㅏ포함된 user를 찾아볼꺼야 그러면 verify (인증)이 되는 거야   """
    def verify_email(self):
        pass