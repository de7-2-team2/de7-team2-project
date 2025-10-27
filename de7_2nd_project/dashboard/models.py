from django.db import models

# 지역테이블 시군구테이블
class region(models.Model):
    r_name = models.CharField(max_length=100)
    area = models.FloatField()

    def __str__(self):
        return self.r_name

class city(models.Model):
    c_name = models.CharField(max_length=100)
    region = models.ForeignKey(region, on_delete=models.CASCADE)

    def __str__(self):
        return self.c_name

# 품목 테이블
    
class item(models.Model):
    i_name = models.CharField(max_length=100)

    def __str__(self):
        return self.i_name

# 인증 농가 테이블
class farm(models.Model):
    f_name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.ForeignKey(city, on_delete=models.CASCADE)
    land_area = models.DecimalField(max_digits=10, decimal_places=2)
    # 생산량
    production = models.DecimalField(max_digits=10, decimal_places=2)
    # 인증 날짜, 인증종료날짜
    cert_date = models.DateField()
    cert_end_date = models.DateField()
    # 품목 테이블 ForeignKey
    items = models.ManyToManyField(item)
    # 인증 유효 여부
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.f_name