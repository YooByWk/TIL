from django.db import models

# Create your models here.
class Weather(models.Model):
    temp = models.FloatField()          # 온도 (기본값 : K ) 
    feels_like = models.FloatField()    # 체감온도 (기본값 : 켈빈)
    dt_txt = models.DateTimeField()    # 데이터 측정 시간
    