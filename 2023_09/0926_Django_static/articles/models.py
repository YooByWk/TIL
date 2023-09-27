from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # 루트 경로에 하위 폴더가 생성된다.
    
    # image = models.ImageField(blank=True)
    # 빈 문자열이 저장 될 수 있도록 제약조건 설정
    # 기존 테이블 사이에 입력되더라도, 생성시에는 가장 우측(뒤)에 추가된다.
    # 기본적으로는 blank를 false 로 가져가지만, 여기서 True 를 주는 이유는
    # 이미지를 업로드 하지 않는 경우에도 유효성 검사에서 문제가 없게 하기 위함.
    # 주로 이미지는 "선택사항" 이기 때문입니다.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
