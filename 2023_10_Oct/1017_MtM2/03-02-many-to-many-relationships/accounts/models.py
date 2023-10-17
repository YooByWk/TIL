from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False,related_name='followers') # 대칭임
    # 자동 양방향 관계 => 강제 맞팔
