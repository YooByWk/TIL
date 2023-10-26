# addEventListener 활용
```js
// 1. 버튼 선택
const btn = document.querySelector('#btn')
const btn2 = document.querySelector('#btn2')
// 2. 버튼에 이벤트 핸들러 부착
btn.addEventListener('click', function (event) {
  console.log(event)
  console.log(event.target)
  console.log(event.currentTarget)
    // event 이친구는 this가 강제로 addeventlistener 앞을 지정함. 
  console.log(this)
  // 콜백함수를 화살표 함수로 바꾸면 안된다.
  // 화살표 함수는 자신의 뭔가가 없어서 최상단 this를 찾아간다.
  // ㅋ ㅋ ㅋ ㅋ 이벤트 타겟으로 접근해서 함수 작성하면, 화살표 가능
  // 일반함수 가 편?할 듯?


})
// 콜백함수를 외부에 작성해도 된다
const clickfunc = function (evnet) {
  console.log(event)
  console.log(event.target)
  console.log(event.currentTarget)
  console.log(this)
}
btn2.addEventListener2('click', clickfunc)
// 
```

## 버블링 장점
<hr>

```html
 <ul>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
  <!-- 여기에 전부 다 이벤트 리스너 부착하는건 좀 . . . . -->
  <!-- 그렇다면! 버블링을 이용하자! (ul에만 부착) -->
  <!-- 그럼 어떻게 실제 자리 알아요? -> target 이용! -->
  <!--  currentTarget = ul -->
  <!--  target : li 각 요소 -->
  <!-- 이것이 버블링이다 희망편 -->
```

## 클릭횟수

```js
//클릭횟수
// 1. 초기값 할당
let counterNumber = 0

// 2. 버튼 요소 선택
const btn = document.querySelector('#btn')

// 3. 콜백 함수 (버튼에 클릭 이벤트가 발생할때마다 실행할 코드)
const clickHandler = function () {
// 3.1 초기값 += 1
counterNumber += 1

// 3.2  span 요소를 선택
const spanTag = document.querySelector('#counter')

// 3.3 p 요소의 컨텐츠를 1 증가한 초기값으로 설정
spanTag.textContent = counterNumber
}
 
```
# 2.사용자의 입력 값을 실시간으로 출력하기

# 3. 입력 실시간 출력, 버튼 누르면 css 스타일 변경
```js
// input 구현
  // 선택
const inputTag = document.querySelector('#text-input')
const h1Tag = document.querySelector('h1')

const inputHandler = function (event) {
  h1Tag.textContent = event.currentTarget.value
}

inputTag.addEventListener('input', inputHandler)

// click 구현
const btn = document.querySelector('#btn')
const clickhandler = function (event) {
  console.log(event)
  h1Tag.classList.toggle('blue')
  // h1Tag.classList.add('blue') 한번 파래지면 돌아오지 않아요. if 쓰기 싫어요
}
// h1 클래스에 퍼랭이 추가.
  //부착
btn.addEventListener('click', clickhandler)
```

# 4. todo
```js

// 1. 필요한 요소 선택
const inputTag = document.querySelector('.input-text')
const btn =document.querySelector('#btn')
const ulTag = document.querySelector('ul')


const addTodo = function (event) {
  // 2.1 사용자 입력 데이터 저장
  const inputData = inputTag.value
  // 3. 사용자 입력 데이터가 빈 데이터인지 확인
  // trim :  공백 제거 // strip 이랑 같은(py) // 스페이스만 눌러도 막혀버림 wwwwww
  if (inputData.trim()) {
    // 2.2 데이터를 저장할 li 요소를 생성
    const LiTag = document.createElement('li')
    // console.log(LiTag) // 디벅
    // 2.3 li 요소 컨텐츠에 데이터 입력
    LiTag.textContent = inputData
    console.log(LiTag)

    // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
    ulTag.appendChild(LiTag)
    // 2.5 todo 추가 후 input의 입력 데이터는 초기화
    inputTag.value=''

  } else {
    alert('입력하시오.')
    // window.alert('입력하시오.') // 윈도우 명령어임
  }
}

// 2. 버튼에 이벤트 핸들러를 부착
btn.addEventListener('click', addTodo)
```

# 5. 로또 번호 생성기 구현