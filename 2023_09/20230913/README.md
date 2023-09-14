# 2023_09_13

## Template System
- html의 콘텐츠를 변수 값에 따라 바꾸고 싶다면?
```py
def index(request):
  context = {
    'name': 'Jane",
  }
  return render(request, 'articles/index.html', context)

```
## Django Template Language (DTL)
- Template 에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템
DTL Syntax
1. Variable
   - render 함수의 세번째 인자로 딕셔너리 데이터를 사용
   - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
   - dot(.)을 사용하여 변수 속성에 접근할 수 있음
2. Filters
   - 표시할 변수를 수정할 때 사용 |
   - chained가 가능하며 일부 필터는 인자를 받기도 함
   - 약 60개의 built-in template filters를 제공
3. Tags
   - 반복 또는 논리를 수행하여 제어 흐름을 만듦
   - 일부 태그는 시작과 종료 태그가 필요
   - 약 24개의 built-in template tags 를 제공 {% tag %} // {% if %} {% endif %}
4. Commnets
   - {# name #} or {% comment %} {% endcomment%}   
   - 주석임
 : 예시 참조
## 템플릿 상속
  페이지의 공통 요소를 포함하고 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
1. 페이지의 공통요소를 포함
2. 하위 템플릿이 재정의 할 수 있는 공간을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
  
  {%block 이름%} {% endblock 이름%}
  'extend' tag는 최상단. 2개 안됨
  block : 하위 템플릿에서 재정의 할 수 있는 블록을 정의 (block 만 할당받아서 사용 가능함. 이외 내용은  부모를 따라감)
[장고 template](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#for)
## HTML form 요청과 응답
데이터를 보내고 가져오기 
http 요청을 서버에 보내는 가장 편리한 방법

### 'form' element
form : method - 로그인 / 로그아웃 / 게시글 생성 // 기본은 GET

각 tag
- 받아서 넘겨주는 놈
- input tag
  - 기본은 text input의 name 은 반환 key (key = value 로 나옴)
  - submit : 취합해서 서버로 전송
-> 실습 예 정 
- action : 할 일
---
action & method
데이터를 어디(action)로 어떤 방식(method)으로 요청할지
- action 
- method

'input' element
- 사용자의 데이터를 입력 받을 수 있는 요소
-  'name' attribute (속성)
   -  데이터를 제출했을 때 서버는 name속성에설정된 값을 통해 사용자가 입력한 데이터에 접근할 수 있음

QueryString Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보낸ㄴ 방법
- 문자열은 앰퍼샌드 & 로 연결된 key=value 쌍으로 구성.
- 기본 URL 과 ? 로 구성됨
  
사용자 입력 데이터 받아 그대로 출력하는 서버 만들기.

HTTP request 객체 
- form으로 전송한 데이터 뿐만 아니라 모든 요청 관련 데이터가 담겨 있음

## URL dispatcher ( 운항 관리자, 분배기)
URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결

## Variable Routing
URL 일부에 변수를 포함시키는 것 , 변수는 view 함수의 인자로 전달할 수 있음
- 작성법
-  <path_converter : variable_name>