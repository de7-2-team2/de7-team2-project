from django.db import models
# 1. 지역 (시도)
class Region(models.Model):
    name = models.CharField(max_length=100)  # 시도명
    area = models.FloatField(null=True, blank=True)  # 면적 (면적 대비 생산량, 지역별 GAP 인증률, 면적대비 품목 다양도 계산할 때 사용)

    def __str__(self):
        return self.name


# 2. 시군구
class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.region.name} {self.name}"


# 3. 읍면동
class Town(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='towns')

    def __str__(self):
        return f"{self.city.name} {self.name}"


# 4. 품목
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# 5. 인증기관
class Agency(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


# 6. 농가
class Farm(models.Model):
    FARM_TYPE_CHOICES = [
        ('개인', '개인'),
        ('단체', '단체'),
    ]

    name = models.CharField(max_length=100)  # 농가명
    owner = models.CharField(max_length=100)  # 대표자명
    farm_type = models.CharField(max_length=10, choices=FARM_TYPE_CHOICES, default='개인')  # 개인/단체
    address = models.CharField(max_length=200)  # 주소
    town = models.ForeignKey(Town, on_delete=models.CASCADE, related_name='farms')
    num_farmers = models.IntegerField(default=1)  # 등록 농가 수 (단체의 경우)
    num_fields = models.IntegerField(default=1)  # 등록 필지 수
    land_area = models.FloatField()  # 재배면적
    production_plan = models.FloatField(null=True, blank=True)  # 생산계획량
    # 재배 품목,manytomany:자동으로 중간 연결테이블 생성(M:N관계-> 한 농가는 여러개 품목 재배가능, 같은 품목을 여러 농가에서 재배가능)
    items = models.ManyToManyField(Item, related_name='farms')  

    def __str__(self):
        return f"{self.name} ({self.owner})"


# 7. GAP 인증정보
class Certification(models.Model):
    cert_number = models.CharField(max_length=100, unique=True) #인증번호
    cert_start = models.DateField() #유효기간 시작
    cert_end = models.DateField()   #종료
    # 인증 유효 여부(현재 날짜 <= cert_end-> True) 넣는다고 하면 admin에서 수동관리하거나 저장할때 자동으로 계산하는 방법 둘 중 한개 사용해야 함 
    # valid = models.BooleanField(default=True) 
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='certifications')
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='certifications')

    def __str__(self):
        return f"GAP-{self.cert_number} ({self.farm.name})"
