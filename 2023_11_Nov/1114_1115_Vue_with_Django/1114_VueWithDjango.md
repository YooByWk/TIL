# 2023_11_14

# DRF 는 주석을 해제하며 진행

#  MD 쓸 시간 있을까 . . 


```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata articles.json  
python manage.py runserver
http://127.0.0.1:8000/api/v1/articles/
```

![Alt text](image.png)


많은 코드들이 주석처리 - 해제하는 방식의 학습

잘 따라가자. 

# Vue 
# 학습 진행과정


## 시작하기 전에 . . .
- 무결점의 프로젝트를 만드는 것이 아니다.
- front-end 프레임워크와 back-end 프레임워크간의 요청과 응답, 그 과정에서 등장하는 새로운 개념과 문제를 해결하며 하나의 웹 애플리케이션 서비스를 구현하는 과정에 집중해야 한다.


Vue -> Django : 브라우저 측에서 거절됨
> CORS policy 에 의해 차단됨
>

## SOP (Same-origin Policy)
: 동일 출처 정책
- 어떤 출처(Origin)에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호 작용 하는 것을 제한하는 보안 방식
- > 웹 애플리케이션의 도메인이 다른 도메인의 리소스에 접근하는 것을 제어하여 사용자의 개인 정보와 데이터의 보안을 보호하고, 잠재적인 보안 위협을 방지
- > 잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임

### Origin 
- URL의 Protocol, Host, Port 를 모두 포함하여 출처라고 부름 
- Same Origin 예시 
  - 아래 세 영역이 일치하는 경우에만 동일 출처(Same-origin)로 인정
  
![Alt text](image-1.png) 

![Alt text](image-2.png)

## CORS policy의 등장 
- 기본적으로 웹 브라우저는 같은 출처에서만 요청하는 것을 허용하며, 다른 출처로의 요청은 보안상의 이유로 차단됨
  - SOP에 의해 다른 출처의 리소스와 상호작용 하는 것이 기본적으로 제한되기 때문
- 하지만 현대 웹 애플리케이션은 다양한 출처로부터 리소스를 요청하는 경우가 많기 때문에 CORS 정책이 필요하게 되었음 
- > **CORS**는 웹 서버가 리소스에 대한 서로 다른 출처 간 접근을 허용하도록 선택할 수 있는 기능을 제공

## CORS (교차 출처 리소스 공유)
- 특정 출처(Origin)에서 실행 중인 웹 애플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한을 부여**하도록 브라우저에 알려주는 체제 
  - 만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 다른 출처지만 접근해도 된다는 사실을 알려야 함 
  - "CORS policy" : 교차 출처 리소스 공유 정책


- 다른 출처에서 온 리소스를 공유하는 것에 대한 정책
- 서버에서 설정되며, 브라우저가 해당 정책을 확인하여 요청이 허용되는지 여부를 결정
- 다른 출처의 리소스를 불러오려면 그 출처에서 올바른 **CORS header**를 포함한 응답을 반환해야 함.

## CORS Headers 설정하기 
- Django에서는 django-cors-headers 라이브러리를 활용
- > 손쉽게 응답 객체에 CORS header를 추가해주는 라이브러리



# 2023_11_15 

# DRF Authentication 어제에 이어서.

- Permissions 권한 
   - 요청에 대한 접근 허용 또는 거부 여부를 결정 

# 인증과 권한 
- 인증이 먼저 진행되며 수신 요청을 해당 요청의 사용자 또는 해당 요청이 서명된 토큰(token)과 같은 일련의 자격 증명과 연결
- 그런 다음 권한 및 제헌 정책(throttling policies)은 인증이 완료된 해당 자격 증명을 사용하여 요청을 해용해야 하는 지를 결정

## DRF 에서의 인증
- 인증은 항상 view 함수 시작 시, 권한 및 제한 확인이 발생하기 전, 다른 코드의 진행이 허용되기 전에 실행됨
- > 인증 자체로는 들어오는 요청을 허용하거나 거부할 수 없으며, 단순히 요청에 사용된 자격 증명만 식별한다.

## 승인되지 않은 응답 및 금지된 응답
- 인증되지 않은 요청이 권한을 거부하는 경우 해당되는 두 가지 오류 코드가 응답
  - 1. HTTP 401 Unauthorized
    - 요청된 리소스에 대한 유효한 인증 자격 증명이 없기 때문에 클라이언트 요청이 완료되지 않았음을 나타냄
  - 2. HTTP 403 Forbidden (Permission Denied)
    - 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
    - 401과 다른점은 서버는 클라이언트가 누구인지 알고 있음

## 인증체계설정방법
1. 전역 설정
2. View 함수 별 설정

## DRF가 제공하는 인증 체계
1. BasicAuthentication
2. TokenAuthentication
etc.
2번을 쓸 예정

## TokenAuthentication 
- 간단한 token 기반 HTTP 인증 체계
- 기본 데스크톱 및 모바일 클라이언트와 같은 클라이언트-서버 설정에 적합
- > 서버가 사용자에게 토큰을 발급하여 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거침 


# Dj-Rest-Auth 
> pip install dj-rest-auth
>
> 온갖 인증 라이브러리

## Dj-Rest-Auth 의 Registration 기능 추가 설정
1. 패키지 추가 설치
2. `pip install 'dj-rest-auth[with_socilal]'`
3. + settings.py


# ??? 
클라이언트가 Token으로 인증받는 방법 
1. 'Authorizaiton' HTTP Header 포함
2. 키 앞에는 Token 적고, 공백으로 key와 구분
   

> 정리 : 발급 받은 Token을 인증이 필요한 요청마다 함께 보내야 함
>
> 아직까지는 모두가 전부 같은 일을 할 수 있음. 

## 권한 정책 설정

- IsAuthenticated 권한설정
  - ㅇ.ㅇ

# vue

index.js

## 인증 여부 추가 기능 구현 

- beforeEach 이동 전 마다 뭔가 뭔가 하는 뭔가 뭔가

- computed로 로그인 여부 파악
  - token의 값이 변할 때만 계산하도록.