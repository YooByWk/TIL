# 2023_11_08

# Passing Props

		컴포넌트가 여러개라면 개별적으로 동일한 데이터를 관리해야 할까??
		-> 사진 변경 해야 할 때 모든 컴포넌트에 대해 변경 요청을 해야 함...
		이상하잖아???
> 공통된 부모 컴포넌트에서 관리하자
asdasdasd d2coing

- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림 (Emit event)

# Props

> 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성

- One-way Data Flow
  - 모든 Props는 자식 속성과 부모 속성 사이에 *하향식 단방향 바인딩*을 형성(one-way-down binding)

## Props 특징

- 부모 속성이 업데이트되면 자식으로 흐르지만 그 반대는 안됨
- 즉 자식 컴포넌트 내부에서 props를 변경하려고 시도해서는 안되며 불가능
- 또한 부모 컴포넌트가 업데이트 될 때마다 자식 컴포넌트의 모든 props가 최신 값으로 업데이트 됨
  > 부모 컴포넌트에서만 변경하고 이를 내려 받는 자식 컴포넌트는 자연스럽게 갱신  
  > 단방향 이유 :
  > 하위 컴포넌트가 실수로 상위 컴포넌트의상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는것을 방지하기 위함


## Props 선언

부모 컴포넌트에서 보낸 props 를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요.

## Props 작성

- 부모 컴포넌트 Parent에서 자식 컴포넌트 ParentChild에 보낼 props 작성
- `prop이름="prop값"

1. 문자열 배열을 사용한 선언
   - defineProps() 를 사용하여 선언
2. 객체를 사용한 선언
   - 객체 선언 문법의 각 객체 속성의 키는 props의 이름이 되며, 객체 속성의 값은 값이 될 데이터의 타입에 해당하는 생성자함수(Number, String) 여야 함
   - 객체 선언 문법 사용 권장

- defineProps() 도 리턴이 있어요 !
- ````js
      const props = defineProps({
              myMsg : String,
              dynamicProps : String,
            })
  ````

## Prop 데이터 사용

- 템플릿에서 반응형 변수와 같은 방식으로 활용
- prop

## Props 세부사항
1. Props Name Casing 
   - 선언 및 템플릿 참조 시 -> camelCase
   - 자식 컴포넌트로 전달 시 -> kebab-case
2. Static Porps & Dynamic Props
   - 지금까지 작성한 것은 Static props
   - v-bind를 사용하여 동적으로 할당된 props를 사용할 수 있음

# Component Events
- 부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림 (Emit event)
- > 부모가 prop 데이터를 변경하도록 소리쳐야 한다
  
## $emit()
자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
- $ 표기는 Vue 인스턴스나 컴포넌트 내에서 제공되는 전역 속성이나 메서드를 식별하기 위한 접두어

### emit 메서드 구조
`$emit(event, ...args)`
- event : 커스텀 이벤트 이름
- args : 추가 인자

### 이벤트 발신 및 수신 (Emitting and Listening to Events)
- $emit을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신
- ```html
  <button @click="$emit('somEvent')"> 클릭 </button>
  ```
- 그러면 부모는 v-on을 사용하여 수신할 수 있다.
- ```html
  <ParentComp @some-event="somCallback"/>
  ```
### Event Name Casing
- 선언 및 발신 시 -> camelCase
- 부모 컴포넌트에서 수신시 -> kebab-case


### 다른 실습은 안에 있다. comp 3 개 확인하시라.

## 정적 & 동적 props 주의사항
- 첫 번째는 정적 props로 문자열로써의 "1"을 전달
- 두 번째는 동적 props로 숫자로써의 1을 전달

## Prop 선언을 객체 선언 문법으로 권장하는 이유
- prop에 타입을 지정하는 것은 컴포넌트를 가독성이 좋게 문서화하는데 도움이 되며, 다른 개발자가 잘못된 유형을 전달할 때에 브라우저 콘솔에 경고를 출력하도록 함
- 추가로 prop에 대한 유효성 검사로 활용 가능

## emit 이벤트도 객체 선언 문법으로 작성 가능
- props 타입 유효성 검사와 유사하게 emit 이벤트 또한 객체 구문으로 선언 된 경우 유효성을 검사할 수 있음
```js
const emit = defineEmits({
	// 유효성 검사 없음
	click : null,
	// subnmit 이벤트 유효성 검사 
	submit : ({email, password}) => {
		if (email && password) {
			return true
		} else {
			console.log('이벤트가 옳지 않음')
			return false
		}
	}
})
const submitForm = function (email, password) {
	emit('submit', {email,password})
}
```


#### 엥 Emit 등록 안해도 돌아간다고!?
> 유효성 검사 하려고 객체 쓰긴 하는디  
> 이름은 나중에 지어줘도 됨. 왜냐면 함수 호출하면서 emit도 쓰고, 이름도 쓰고 있으니까.   
> props는 값이 필요하지만, emit event는 그냥 호출이니까.  
> 하지만, 권장하지 않는다. 


# watch 관련 
```
// getter
watch(
  () => x.value + y.value,
  (sum) => {
    console.log(`x + y: ${sum}`)
  }
)
```
ref의 자료가 아니라면 watch(x, (new,old)=> {doSomeThing})의 X 자리에 못들어간다.
> 이런 경우에는 getter 라는 ()=> 그 값 
>
> 이런 구조를 사용해서 넣는다.