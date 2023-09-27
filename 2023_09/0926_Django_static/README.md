# 0926 Django static files


## Static Files 정적 파일
서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- (이미지, js, css 파일 등)

##  Static file 제공하기
1. 기본 경로에서 제공하기 (Template과 조금 유사한가?)
   - app폴더 / static (참으로 Template과 유사하구료)
   - articles/static/articles
2. 추가 경로에서 제공하기 ()


### Django에서 Static 가져오기
static 은 static url 을 사용합니다.   ?
**static tag는 built-in 은 아님니다!?** 따라서 import같은 **load** 해 오세요.  
```django
{%load static%} 
```
css 또한 static 으로 가져와야 합니다. 경로를 쓰는 것이 아니라, static tag를 통해서 경로에 접근해야 한다.


사용자에게 제공 가능한 정적 파일 url = URL + static_url + 정적파일 경로
- 딱히 경로를 변경하지는 않아요.
- 정적 파일을 제공하려면 요청에 응답하기 위한 URL이 필요하다.

### static files 추가 경로
- staticfiles_dirs에 문자열 값으로 추가 경로 설정
settings.py

```py
 STATICFILES_DIRS = [
    BASE_DIR / 'static', 
]
# 이거 만들고 base_dir에(최상위폴더) static 만들어주기
```


#### 비교
- template 기본 경로 . . .(객체순 / 해가며 넘어가는 파이썬의 구조)
  - 'DIRS' : [BASE_DIR / 'templates',], 

<hr>
## Media files 
- 이미지 업로드
- 사용자가 웹에서 업로드하는 정적 파일 (user-uploaded)

### 이미지 업로드
사전작업이 좀 필요함.

### imageField() 
이미지 업로드에 사용하는 모델 필드
> 이미지 객체가 직접 저장되는 것이 아닌 '이미지 파일의 경로'가 문자열로 DB에 저장

### 미디어 파일을 제공하기 전 준비 - 사전작업
1. setting.py 에 MEDIA_ROOT , MEDIA_URL 설정 (셀프서비스입니다)
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정

#### MEDIA_ROOT
미디어 파일들이 위치하는 디렉토리의 절대 경로
settings.py 
MEDIA_ROOT = BASE_DIR / 'media' 

#### MEDIA_URL
MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성 (STATIC_URL과 동일한 역할)  
settings.py  
MEDIA_URL = 'media/'


MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
업로드 된 파일의 url == settings.MEDIA_URL  
위 URL을 통해 참조하는 파일의 실제 위치 == settings.MEDIA_ROOT

-> project 의 setting 설정 후 urls 도 설정해주기

-> 이후 모델 파일도 수정하기
...
<hr>
form은 기본적으로 텍스트 데이터만 받아요.
따라서 추가적 설정 필요

-> CREATE의 form에 
enctype="multipart/form-data"  
추가
-> view 함수에 request.FILES 추가...

--> DB에는 경로로 저장됩니다. 이미지 그 자체로 저장되는건 아님. 
--> DB에 저장된 경로를 활용해, 이미지를 출력하는 것.
### 이유 : 
1. 성능 및 DB 최적화를 위해 
   - 직접 파일을 저장하면 DB 크기가 급격하게 증가
   - 성능저하
   - 파일 자체는 파일 시스템에 별도로 저장 
   - DB에는 그 파일에 대한 문자열 경로만.
2. 유지 보수 관점
   - 만약 DB에 직접 파일을 저장한다면, 이미지 파일을 변경하거나 업데이트 할 때 DB를 직접 조작해야 한다.
   - 하지만 db에는 경로만 저장한 후 파일 시스템에 따로 둔다면, 파일 시스템에서만 파일을 수정하면 된다.

<hr>
이후 또  detail 에 가서 
  <img src="{{article.image.url}}" alt="">
이런 느낌으로.

이후 update도 수정해주시오. (동일과정)

-< 이미지 저장 경로 - models.py>

파이썬문법
```
%Y/%M/%d/
# 해당 년 월 일로 저장됩니다.
```
