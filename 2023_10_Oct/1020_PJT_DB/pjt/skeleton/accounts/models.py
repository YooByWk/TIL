from django.db import models
# 어떻게 클래스처럼 . 으로 (폴더)를 접근할 수 있을까 ? 
# __init__.py : 생성자 ( ././class) 처럼 접근 가능하게 만들어준다.
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass