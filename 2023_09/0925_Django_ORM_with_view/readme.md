migrations 함
views 에서만짐
  from .models import Article 추가함

views 파일 싹 다 여기서 만지는 중

ulr 만들어주기
view 함수 만들어주기
html 템플릿 만들어주기
{{ }} 익숙해지기.


Create 로직을 구현하기 위해 필요한 view 함수의 개수는? 
  > throw catch에서 한 번 본 것 같은 느낌인데?!
  > 마찬가지로 2개의 함수가 필요하다
- 사용자 입력 데이터를 받을 페이지를 랜더링 New 
- 사용자가 입력한 데이터를 받아 DB에 저장 Create


CRUD 가 뭐더라
(Create,Read,Update,Delete)
### 느그가 하는 일 말고, 결과나 보여줘 응애

## HTTP request methods
http :네트워크상에서 데이터를 주고 받기 위한 약속 
<hr>
http request methods 
데이터(리소스)에 어떤 요청(요청)을 원하는지를 나타내는 것
GET & POST

### GET : 특정 리소르를 조회하는 요청
GET 으로 데이터를 전달하면 QUERY STRING 형식으로 보내진다.  <br>
ej: 검색
로그인에 나오면 상당히 골때리겠죠?
### POST Method
특정 리소스에 변경(생성, 수정, 삭제)를 요구하는 요청    
Post로 데이터를 전달하면 http body 에 담겨 보내진다.

GET -> 조회 R  
Post -> CUD
방금 get으로 만든건 동작은 하지만 올바른 원리는 아니다.! 
DB 변경은 꽤나 큰 일이기 때문

403 에러 ㅂㄷㅂㄷ
CSRF token missing
: 넌 승인된 인간이 아니다.
여기서 token은 인증된 유저인지 확인
### CSRF 
Cross-Stie-Request-Forgery  
사이트 간 요청 위조
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법

Django 서버는 해당 요청이 db에 데이터를 하나 생성하는(db에 영향을 주는)요청에 대해 djangor가 직접 제공한 페이지에서 데이터를 작성하고 있다는... (추가입력)

### post일때만 token 확인 이유?
POST는 단순 조회를 위한 GET과 달리 특정 리소스에 변경... (추가입력)




## HTTP response status code 
특정 HTTP 요청이 성공적으로 완료되었는지를 3자리 숫자로 표현하는...

예시 : 404 : 나는 그런 주소 없다.

Redirect():  
클라이언트가 인자에 작성된 주소로 다시 돌아가게 ?  
데이터 저장 후 페이지를 주는 것이 아닌 다른 페이지로 사용자를 보내야 한다.

# D (delete)
간단. 간단. 간단. 간단. 간단!


# Update
필요한 view 로직 몇 ? 개 ? : 2개겠지 뭐

1. 사용자 입력 데이터를 받을 페이지 렌더링 edit // 
2. 사용자가 입력한 데이터를 받아 DB에 저장 update // 

>  edit 구현 <br>
> 수정하는 페이지  <br>
> 이후 redirect 
참 쉽죠? 