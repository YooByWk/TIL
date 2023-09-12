# 2023_09_12

## 웹 서비스 개발에는 무엇이 필요할까? 
로그인 로그아웃 회원관리 데이터베이스 보안 등 많은 기술이 필요
하지만 만들 필요는 없음

Framework - 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
( 개발에 필요한 기본 구조, 규칙 라이브러리 등을 제공)
- 왜 사용? 
- 기본적 구조 도구 규칙 등 제고 , 개발자는 핵심 개발에 집중
- 생산성 up
- 유지보수 확장 용이
## Django framework!
python 기반의 대표적인 웹 프레임워크

## 클라이언트와 서버
### client
서비스를 요청하는 주체 ( 웹 사용자의 인터넷이 연결된 장치, 웹브라우저)
### Server  서버
클라이언트의 요청에 응답하는 주체 :  (웹페이지, 앱 저장 컴)


## 가상 환경
- python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 *독립적인* 실행환경
### 가상 환경이 필요한 시나리오 
1.
- 한 개발자가 2개의 프로젝트를 진행해야 하는 경우
- A 는 request 패키지 v1
- B 는 request 패키지 v2
- 파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있음 
-  A B 프로젝트 다른 패키지 버전 사용을 위한 독립적인 개발 환경이 필요함 
-  -> 가상 환경이 필요한 시나리오!
2.
- 한 개발자가 2개 진행해야 함
- A는 water라는 패키지 사용해야 함
- B는 fire라는 패키지 사용해야 함
- 파이썬 환경에서는 water 패키지와 fire 패키지를 함께 사용하면 충돌이 발생하기 때문에 설치할 수 없다.
- A / B 충돌 방지를 위해 독립적 개발 환경 필요

### 패키지 목록...
```bash
python -m venv venv

source venv/Scripts/activate

pip freez > requirements.txt

pip install -r requirements.txt

pip list

//SSAFY 공용노션 Python 가상환경 설정.
```
venv 이름 잘 안바꿈
그리고 git 업로드 하지 마십쇼. gitignore에 잘 넣읍시다.

### 장고 루틴


## 참고
LTS (Long-Term Support)
- 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용
- 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요

## Django Project
애플리케이션의 집합
(DB 설정, URL 연결, 전체 앱 설정 등 처리)
### Django application
- 독립적으로 작동하는 기능 단위 모듈
- 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트를 구성

1. app 생성
  - python manage.py startapp articles
    - 앱의 이름은 '복수형' 저장을 권장.
    - 등록 후 생성은 불가능하다.
2. app 등록 
   - settingss.py에 Installed app 맨 윗줄.
app을 만들고... pjt에 포함도 시켜줘야 한다.


## Django 디자인 패턴
### 디자인 패턴
- 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
- (공통적인 문제를 해결하는데 쓰이는 형식화 된 관행)
### MVC 디자인 패턴
Model, View, Controller ( DB, 화면, 내부 로직)
- 애플리케이션을 구조화하는 대표적인 패턴  (데이터, 사용자 인터페이스, 비즈니스 로직을 분리)
   - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해

#### Python - pythonic 
[] = list // python  
[] = array // etc.  
이런 느낌으로... Django 도 pythonic 하네오.

###  MTV 디자인 패턴
Model, Template, view ...
- Django에서 애플리케이션을 구조화하는 패턴
- 기존 MVC패턴과 동일하나 명칭을 다르게 정의한 것...

### 앱 구조
- admin.py  : 
  - 관리자용 페이지 설정
- models.py : 
  - DB와 관련된 Model을 정의
  - MTV 패턴의 M
- views.py : view (MTV)
  - HTTP 요청을 처리하고 해당 요청에 대한 응답을 반환(url,mode,template과 연계)
  - MTV  패턴의 V 

#### Django와 요청& 응답
요청 -> urls.py -> views.py -> models.py | templates.py -> views.py
views.py -> 응답

~~아 우리 백엔드 하고있었구나....~~

바꾼 것 articles views.py
templates / articles / html
urls.py