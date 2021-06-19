from django.db import models
from django.urls import reverse
# Create your models here.
# 모델 : 데이터베이스를 sql없이 다루려고 모델을 사용
# 우리가 데이터를 객체화해서 다루겠다.
# 모델 = 테이블
# 모델의 필드 = 테이블의 컬럼
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터값
# 인스턴스 = 테이블의 레코드
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 필드의 종류가 결정하는 것
    # 1. 데이터베이스의 컬럼 종류
    # 2. 제약 사항(제약사항)
    # 3. from 의 종류 결정
    # 4. from에서 제약 사항 결정

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
#모델을 만들었다 => 데이터베이스에 어떤 데이터드르을 어떤 형태로 넣을지 결정했다!
# 마이그레이션 ==> 데이터베이스에 모델의 내용ㅇ르 반영 (테이블 생성)
# makemigrations => 모델의 변경사항을 추적해서 기ㅣ록