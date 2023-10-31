# 2023_1031


ajax 와 서버
Ajax with follow 
Ajax with like

# Ajax & server
Ajax : 아무튼 비동기적 서버 통신 웹 페이지 일부만을 업데이트 하는 웹 개발 기술

Ajax를 활용한 클라이언트 서버 간 동작
클라이언트 / 서버 
이벤트 발생 XHR 객체 생성 및 요청 -> Ajax 요청 처리 -> JSON 데이터 응답 -> 응답 데이터를 활용해 DOM조작

## 오늘은 코드 중심
## 오늘은 코드 중심
## 오늘은 코드 중심
## 오늘은 코드 중심
## 오늘은 코드 중심
admin 
user1
user2
ssafy1234

## 팔로우 비동기 처리
- 좋아요 비동기 처리
- follow보다 생각할 것이 있어서 좋아요를 우선 함 
- 현재 상황은 단지 "Follow" 한개를 변경하기 위해서 페이지 전체를 새로고침 중.
- 만약 페이지가 스크롤이 존재하고, 버튼은 멀리 있다면? 
  - > 갑자기 가장 첫 페이지 맨 위로 돌아가게 될 것.  
  - > 불-편 

### Axios를 통해 뭔가 뭔가 해야한다.?! form 불필요 부분 숙청
1. Axios cdn
2. form 수정 
```html
전:        
<form action="{% url "accounts:follow" person.pk %}" method="POST">
<script>
// axios 로 method, url 요청 대체함
//  form숙청


// 0. form id 추가
// formTag.addEventListener('sumbit', 장고 서버로 follow 요청을 보내는 콜백함수)
// 1. form 선택
const formTag = document.querySelector('#follow-form')
// 2. 이벤트 리스너 부착
formTag.addEventListener('sumbit', function (event) {
  // 3. submit 이벤트 기본 동작 취소 
  event.preventDefault()
  // 4. Axios 비동기적 팔로우/언팔 요청

  console.log(event) 
}) // 일단 이대로 하면, form 의 새로고침이 사라지고 , submit 이벤트의 기본 동작이 발생한다.
// preventDefault 

// <수정> 

const formTag = document.querySelector('#follow-form')
formTag.addEventListener('sumbit', function (event) {
  console.log(event) 
})
``` 

mdn htlm data attribute
- data-아무거나 
- data-이름2 하이픈 </br>
- data-뭔가뭔가
- js에서 선택하기;
- article.dotaset.이름2;
- article.dataset.뭔가뭔가;
- 속성은 문자열
### django ajax csrf
- 에러 진짜 화나네

### follow view 함수 js 끝
1. redirect를 막아라 
```py
# views.py
from django.http import JsonResponse # 딕셔너리로 받으면 Json 응답

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user

    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            is_followed = False # flag
        else:
            you.followers.add(me)
            is_followed = True # flag
        # return JSON 리턴!
        context ={
            # remove인지 
            # add인지 판단해보자
            # flag
            'is_followed' : is_followed
        } 
        return JsonResponse(context)
    return redirect('accounts:profile', you.username)

```
어질어질하네요.
1번 보면서 해봅시다.

## 좋아요 Ajax 적용 시 유의사항
Ajax 적용은 팔로우와 모두 동일
단, 팔로우와 달리 좋아요 버튼은 `한 페이지에 여러 개`가 존재
1. forEach() // 넌 누구냐
2. querySelectorAll()



# 참고
Ajax 의 필요성
- human-centered design with UX : 인간 중심으로 설계된 사용자 경험
- 