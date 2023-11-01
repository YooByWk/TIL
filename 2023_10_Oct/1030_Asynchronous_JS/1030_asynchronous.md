# 2023_10_30

# Asynchronous
## Synchronous (동기)
프로그램의 실행 흐름이 순차적으로 진행
> 하나의 작업이 완료된 후에 다음 작업이 실행되는 방식  
> ej. 주문 후 커피가 나올 때까지 기다려야 함

### Synchronous 예시
1. 메인 작업이 모두 수행되어야 마지막 작업이 수행됨
2. 함수의 작업이 완료될 때까지 기다렸다가 값을 반환해야 계속 진행할 수 있음(동기 함수)

## Asynchronous (비동기)
프로그램의 실행 흐름이 순차적이지 않으며, 작업이 완료되기를 기다리지 않고, 다음 작업이 실행되는 방식
> 작업의 완료 여부를 신경 쓰지 않고 동시에 다른 작업들을 수행할 수 있음

### Asynchronous 특징
- `병렬적 수행`
- 당장 처리를 완료할 수 없고 시간이 필요한 작업들은 별도로 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리.
- 예시 : 
  -  메일에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 별도로 처리된다.
  -  브라우저는 웹페이지를 먼저 처리되는 요소부터 그려 나가며 처리가 오래걸리는 것들은 별도로 처리가 완료되는대로 병렬적으로 처리
```js
setTimeout(function () {
  callBack()
}, 3000) 
// 3초를 기다렸다가 콜백 함수를  호출하는 하뭇 
```
#### 구경해보기
[01번 파일.](./01-asynchrounous.html)

![Alt text](image.png)
```js
<script>
 const slowRequest = function (callBack) {
   console.log('1. 오래걸리는 작업 시작. . . ')
   setTimeout(function () {
     callBack()
    } , 3000)
   } // (콜백함수()) 그 시간 이후 함수 출력 // ms 1000 = 1 sec

 const myCallBack = function () {
   console.log('2. 콜백함수 실행됨')
 }

 slowRequest(myCallBack)

 console.log('3. 다른 작업 실행')
</script>
```

##  Single Thread 언어, JavaScript
Thread 란? 
- 작업을 처리할 때 실제로 작업을 수행하는 주체로, multi-thread 라면 수행할 수 있는 주체가 여러개라는 의미
## JavaScript Runtime
- JavaScript가 동작할 수 있는 환경(Runtime)
- JavaScript 자체는 Single Thread 이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요
- JavaScript에서 비동기와 관련된 작업은 '브라우저' 또는 'Node'와 같은 환경에서 처리.
### 브라우저 환경에서의 JavaScript 비동기 처리 관련 요소
1. JavaScript Engine의 Call Stack
2. Web API
3. Task Queue
4. Event loop

### 브라우저 환경에서 JavaScript 비동기 처리 동작 방식
1. 모든 작업은 Call Stack(LIFO)로 들어간 후 처리된다. 
2. 오래 걸리는 작업이 call stack으로 들어오면web api로 보내 별도로 처리하도록 한다.
3. web api에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue (FIFO)에 순서대로 들어간다.
4. Event Loop가 Call Stack이 비어있는 것을 계속 체크하고, Call Stack 이 빈다면 Task Queue에서 가장 오래된 (가장 먼저 처리되어 들어온)작업을 call stack으로 보낸다.

#### Call Stack 
- 요청이 들어올 때 마다 순차적으로 처리하는 Stack (  LIFO    )
- 기본적인 JavaScript의 Single Tread 적옵 초라 

#### EEB API 
- 별첨

#### Task Queue ( Callback Queue)
- 비동기 처리된 Callback 함수가 대기하는 Q ueue (Fifo)

#### Eevet look
- 테스크(작업)이 들어오길 기다렸다가 태스크가 들어오면 이를 처리하고 처리할 태스크가 없는 경우엔 잠드는 자바스크립트 내 루프
- Call stact 과 Task Queue 를 지속적으로 머니터링
- Call Stack이 비어있는지 확인 후 비어있다면 Tasdk Queue 에서 대기 중인 오래된 작업을 Call Stack으로 Push

### 정리 
- JavaScript는 한 번에 하나의 작업을 수행하는Single Thread 언어로 동기적 처리를 진행
- 하지만 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue 를 거쳐, Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨


## AJAX 
( Asynchronous JavaScript + XML)
JavaScript의 비동기 구조와 XML 객체를 활용해 비동기적으로 서버와 통신하여, 웹 페이지의 일부분을 업데이트
JSON : JavaScript의 일종 

### XMLHttpRequest 객체  xhr 객체
서버와 상호작용할 때 사용하며 페이지의 새로고침 없이도 URL에서 데이터를 가져올 수 있음
> 사용자의 작업을 방해지하지 않고 페이지의 일부를 업데이트
> 주로 AJAX 프로그램에 많이 사용됨

###  이벤트 핸들러 : 비동기 프로그래밍의 한 형태
- 이벤트가 발생할 때마다 호출되는 함수(콜백함수)를 제공하는 것
- XMLHttpRequest(XHR)는 JavaScript 를 사용하여 서버에 HTTP 요청을 할 수 있는 객체
- HTTP 요청은 응답이; 올 떄 까지의 시간이 걸릴 수 있는 작업이라 비동기 API 이며, 이벤트 핸들러를 XHR 객체에 연결해 요청의 진행 상태 및 최종 완료에 대한 응답을 받음

## Axios
- JavaScript에서  사용되는  HTTP 클라이언트 라이브러리 
- > 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
- >
- > python : requests
- JavaScript 내장은 아님 
- 비동기 요청에 자주 사용함
- Vue 에서 잘 씀

CDN 으로 쓸 수 있음  // google go 
```
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```
### 구조
- get, post 등 여러  http request method 사용 가능 
- then 메서드를 사용해서 '성공하면 수행할 로직'을 작성
- catch 메서드를 사용해서 '실패하면 수행할 로직' 을 작성
```js
axios ({
  method : 'post',
  url : '/user/12345',
  data : {
    firstName: 'Fred',
    lastName: 'Flintstone'
  }
}) 
 . then 성공 함수
 . cathch 실패 함수
```

[고양이 사진 api  실습2](./02-cat-api.html)

고양이사진은 고양이 사진대로 처리하고, 나머지는 알아서 처리하게 비동기 처리 해 볼것

[고양이사진버튼](./03-cat-api-ad.html)

### 정리 
- axios는 브라우저에서 비동기로 데이터 통신을 가능하게 하는 라이브러리
  - 브라우저를 위해 XMLHttpRequest 생성
- 같은 방식으로 DRF 로 만든 API 서버로 요청을 보내서 데이터를 받아온 후 처리할 수 있도록 함


## Callback 과 Promise

### 비동기 처리의 단점
- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리한다는 것
- 그런데 이는 개발자 입장에서 코드의 실행 순서가 불명확하다는 단점 존재
- 이와같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함
- > 콜백 함수를 사용하자!

### 비동기 콜백
- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함
- > 작업의 순서와 동작을 제어하거나 결과를 처리하는 데 사용

### [콜백지옥  . . .](./99-callbackhell.js)
- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문제
- 코드 작성 형태가 마치 '피라미드'같다 하여 "Pyramid of doom (파멸의 피라미드)" 라고도 부름
- A 끝  B 끝 C 끝 D 끝 . . . . . . . . .

## Promise
JavaScript에서 비동기 작업의 결과를 나타내는 객체
> 비동기 작업이 완료되었을 때 결과 값을 반환하거나, 실패 시 에러를 처리할 수 있는 기능을 제공
- 콜백 지옥 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체 
- 작업이 끝나면 실행 시켜 줄게 라는 약속(promise)
- 비동기 작업의 완료 또는 실패를 나타내는 객체
- Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리 
  - 성공에 대한 약속(then())
  - 실패에 대한 약속(catch())
- 오 ! 
```js
work1()
  .then((res1) => {
    // work 2
    return res2  
  })
  .then((res2) => {
    // work 3
    return res3
  })
  .then((res3) => {
    // work 4
    return res4 
  })
   .catch(error) =>{
    // error 처리
   } 

//  위의  코드는 다음과 같다
// work1.then().then().then().catch()의 느낌이다.
// 앞의 return은 다음으로... 또 다음으로 ... 어딘가의 return이 이상하다면 -> catch로 넘어갑니다.
```

### Axios 재정리!
JavaScript 에서 사용하는 Promise 기반의 HTTP 클라이언트 라이브러리


### then & catch
- 둘 다 모두 항상 promise 객체를 반환
- 계속하여 chaining을 할 수 있다.
- axios로 처리한 비동기 로직이 항상  promise 객체를 반환 
- then을 계속 이어 나가면서 작성할 수 있게 됨

#### then(callback)
- 요청 작업 성공시 callback 
- callback은 이전 작업의 성공 결과를 인자로 전달받는다.
#### catch(callback)
- 요청 작업 실패시 callback
- callback은 이전 작업의 실패객체를 인자로 전달받는다.

#### then chaining 의 목적
- 비동기 작업의 '순차적인' 처리 가능
- 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움

#### then chaining의 장점 
1. 가독성
   - 비동기 작업의 순서와 의존 관계를 명확히 표현할 수 있어 코드의 가독성 향상
2. 에러 처리 
   - 각각의 비동기 작업 단계에서 발생하는 에러를 분할해서 처리 가능
3. 유연성
   - 각 단계마다 필요한 데이터를 가공하거나 다른 비동기 작업을 수행할 수 있어서 더 복잡한 비동기 흐름을 구성할 수 있다.
4. 코드 관리
   - 비동기 작업을 분리하여 구성하면 코드를 관리하기 용이하다

### Promise가 보장하는 것(vs 비동기 콜백)
1. 콜백 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
   - 반면 Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨
2. 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 호출 순서를 보장하며 동작
3. .then()을 여러번 사용하여 여러개의 callback 함수를 추가할 수 있음
   - 각각의 callback은 주어진 순서대로 하나하나 실행하게 됨
   - Chaining은 Promise의 가장 뛰어난 장점

# 참고
## 비동기를 사용하는 이유 - '사용자 경험'
예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기식으로 처리한다면 데이터를 모두 불러온 뒤에서야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 된다.
- 즉 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만든다.
- 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있다.
- 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현된다.