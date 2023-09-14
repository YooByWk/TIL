# 2023_09_14

## Model을 통한 DB 관리

Django Model
DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 청사진(blueprint)

## model 클래스 살펴보기
최정적으로 DB에 다음과 같은 테이블 구조를 만듦;

```py
# app/models
from django.db import models

# Create your models here.
class Article(models.Model):
    # 모델 클래스를 상속받을것임
    title = models.CharField(max_length=10)
    content = models.TextField()
    # 작성한 모델 클래스는 최종적으로 DB에 다음과 같은 테이블 구조를 만듦
    # django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
    # Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
    # 개발자는 가장 중요한 테이블 구조를 어떻게 설계할지에 대한 코드만 작성하도록 하기 위한 것(프레임워크의 이점)
    # 클래스 변수명 = 테이블의 각 '필드' (열) 이름 
    # model Field = 테이블 필드의 데이터 타입
    # 어떤 타입이 들어갈지 Filed에 명시되어야 한다. // 문자열 정수 etc.
    # model Field 클래스의 키워드 인자 ( 필드 옵션 ) 
    # 테이블 필드의 "제약조건" 관련 설정 // max_length=10
    # 
```
### 제약조건
데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
- 숫자만 저장되게/ 문자가 100자 까지만 저장되게

## Migrations
model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법  
과정 :  
  model calss (설계 초안)> {*makemigrations*} > migration파일 (최종 설계도) > {*migrate*} > db.sqlite3

### 핵심 명령어
```bash
python manage.py makemigrations   # 작성
python manage.py migrate          # 반영
```
DB는 .... python을 이해 못해오  
0001_initial.py 수정하지 마시오 
migrate 후 DB 내에 생성된 테이블 확인 . . . .   
- 앱이름_클래스이름으로 db 생기는 듯  
- 뭔가 데이터 명 : 데이터 타입

### -> 이미 생성된 테이블에 필드를 추가해야 한다면???  
앗 아아..  
- 추가 모델 필드 작성
```python 
# Create your models here.
class Article(models.Model):
    # 모델 클래스를 상속받을것임
    title = models.CharField(max_length=10)
    content = models.TextField()

    # 추가 모델 필드 작성
    # 날짜와 시간을 담는 Field
    created_at = models.DateTimeField(auto_now_add=True) 
    # 기본값은 False 였군요?! auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)
    # 기본값은 False 였군요?! auto_now=True
    # 1) Provide a one-off default now which will be set on all existing rows
    #2) Quit and manually define a default value in models.py.

    # 1 선택

    #     Please enter the default value as valid Python.
    # Accept the default 'timezone.now' by pressing 'Enter' or provide another value.
    # The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.        
    # Type 'exit' to exit this prompt
    # 안고르면 그냥 아래의 이거 넣어버릴거임
    # [default: timezone.now] >>>
    # 걍 enter
    # Django가 나보다 똑똑함;

    # 값이 없는 필드를 추가할 수 없음.
    # 기본값 설정을 해줬음.
```
```python 
# 앱/migrations 0002_
class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]
    # 아까 만든 1번에 의존성 有
```
<p>
- 하고나서 python manage.py migrate 해주기
- db.sqlite3는 새로고침 자동으로 안됩니다.
- 어지간해서는 Django의 추천 기능을 이용하자!
- 계속 누적하면서 가는 이유 : 추후 문제가 생겼을 시 복구하거나 되돌릴 수 있도록... (git commit 하듯)
  
### 추가 Migrations 
model class에 변경사항(1)이 생겼다면, 
반드시 새로운 설계도를 생성(2)  
DB에 반영(3)  
  1. model class 변경
  2. makemigrations
  3. migrate
  <p> ㄴㅇㅅ </p>

## CharField()
길이의 제한이 잇는 문자열을 넣을 때 사용
- 필드의 최대 길이를 결정하는 max_length는 필수인자.
  
## TextField()
글자의 수가 많을 때 사용
- 적당히 많이 들어갑니다.
- DB 종류가 많음 -> 해당 종류에 따라서 
## DateTimeField의 선택인자

- auto_now
  - 데이터가 **저장될 때마다** 자동으로 현재 날짜/시간을 저장
- auto_now_add
  - 데이터가 **처음 생성될 때만** 자동으로 현재 날짜/시간을 저장
---
## Admin site

### Automatic admin interface
Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 확인 및 테스트 등을 진행하는데 매우 유용

### Admin 계정 생성 
- email 은 선택사항이기 때문에 입력하지 않고 진행 가능
- 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
- DB에서 생성된 admin 계정 확인

## DB 초기화
1. migration 파일 삭제
2. db.sqlite3 파일 삭제 <p>
  단 아래 파일 지우지 마시오
  - __init__.py
  - migrations 폴더
### 기타 명령어


```bash
python manage.py showmigrations
python manage.py sqlmigrate articles 0001
```

#### etc. 
1. 첫 migrate시 출력 내용이 많은 EU : <p>
Django 프로젝트가 동작하기 위해 미리 작성되어있는 기본 내장 app에 대한 migration 파일들이 함께 migrate되기 때문.

2. SQLite 
  데이터베이스 관리 시스템 중 하나이며 Django의 기본 데이터 베이스로 사용됨 (파일로 존재하며 가볍고 호환성이 좋음)

### 오늘 할 일
#### CRUD
C : Create 저장 // 생성
R : Read  조회 
U : Update 갱신
D : Delete 삭제

## 장고야!!!!!!!!
- 삭제 된 ID도 숙청하지 않아요.
- 우리식당 재사용 안해요.

<br>
<br>

# [Naver- 안전한 비밀번호 저장](https://d2.naver.com/helloworld/318732)