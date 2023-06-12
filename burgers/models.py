from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=20)  # CharField은 문자열을 저장하는 명령어
    price = models.IntegerField(default=0)  # IntegerField은 숫자를 저장하는 명령어
    calories = models.IntegerField(default=0)