from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# django 가 기본적으로 User 모델을 주지만
# 덮어쓰는 이유는 
# 1. Django 의 권장사항이다.
# 2. 커스텀을 하기 위해 
class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    