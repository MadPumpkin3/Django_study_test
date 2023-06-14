from django.db import models

# Create your models here.
class Burger(models.Model):
    name = models.CharField(max_length=20)  # CharField은 문자열을 저장하는 명령어
    price = models.IntegerField(default=0)  # IntegerField은 숫자를 저장하는 명령어
    calories = models.IntegerField(default=0)

    def __str__(self):  # 모델 클래스의 인스턴스를 어떻게 표현할지 나타내는 메소드
        return self.name  # object1로 알 수 없게 적혀있던 부분이 '더블와퍼'로 나타난다.