# 2023_11_09

# Router

## Routing
- 네트워크에서 경로를 선택하는 프로세스
> 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

SSR에서의 Routing :
- 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
- 링크를 클릭하면 브라우저는 서버로부터 HTML응답을 수신하고 새 HTML 로 전체 페이지를 다시 로드


CSR/SPA에서의 Routing
- SPA에서 routing은 브라우저의 클라이언트 측에서 수행
- 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드하지 않음
- 페이지는 1개이지만 링크에 따라 여러 컴포넌트를 렌더링하여 마치 여러 페이지는 사용하는 것처럼 보이도록 해야함

## 만약 routing이 없다면
- 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
  - URL이 1개이기 때문에 새로 고침 시 처음 페이지로 되돌아감
  - 링크를 공유할 시 첫 페이지만 공유 가능
- 브라우저의 뒤로가기 기능을 사용할 수 없음

    
## Vue Router!


    √ Project name: ... vue-project   
    √ Add TypeScript? ... No / Yes  
    √ Add JSX Support? ... No / Yes  
    √ Add Vue Router for Single Page Application development? ... No / `Yes`  
    √ Add Pinia for state management? ... No / Yes  
    √ Add Vitest for Unit Testing? ... No / Yes  
    √ Add an End-to-End Testing Solution? » No  
    ? Add ESLint for code quality? » No / Yes  

### Vue 프로젝트 구조 변화
1. App.vue 코드 변화
- RouterLink : 
  - 페이지를 다시 로드하지 않고 URL을 변경하고 생성 및 관련 로직을 처리
  - HTML의 a태그를 렌더링
-  RouterView :
   -  URL에 해당하는 컴포넌트를 표시
   -  어디에나 배치하여 레이아웃에 맞출 수 있음
2. router 폴더 생성
   - router/index.js
     - 라우팅에 정보 및 설정이 작성되는 곳
     - router에 URL과 컴포넌트를 매핑
     -  
3. views 폴더 생성
   - RouterView 위치에 렌더링 할 컴포넌트를 배치
   - 기존 componets 폴더와 기능적으로 다른 것은 없으며 단순 분류의 의미로 구성됨
   - > 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장
  
## 라우팅 기본
1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)
2. RouterLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)을 사용
## Named Routes
- 경로에 이름을 지정하는 라우팅

### Named Routes 예시
- name 속성 값에 경로에 대한 이름을 지정
- 경로에 연결하려면 RouterLink에 v-bind를 사용해 'to' prop 객체로 전달
```js
<RouterLink :to="{ name : 'home' }"> Home </RouterLink>
```
### Dynamic Route Matching with Params
매개 변수를 사용한 동적 경로 매칭
- 주어진 패턴 경로를 동일한 컴포넌트에 매핑해야 하는 경우 활용
- 예를 들어 모든 사용자의 ID를 활용하여 프로필 페이지 url을 설계한다면? 
- user/1
- user/2
- user/3
- > 패턴의 반복 

1.  UserView 컴포넌트 작성 (생성)
2.  UserView 컴포넌트 라우트 등록 index.js
3.  app 
```js
<RouterLink :to="{ name : 'user', params: {id : userId} }">ㅁㄴㅇㄹ</RouterLink>
```
4. 라우트의 매개 변수는 컴포넌트에서 $route.params로 참조 가능

```js
// js 내부에서 사용이 필요한 경우 emit마냥 이래야 함
import { useRoute } from 'vue-router'
import { ref } from 'vue'

const route = useRoute()
const userId = ref(route.params.id) 

```

## Programmatic Navigation
router의 인스턴스 메서드를 사용해 RouterLink로 a태그를 만드는 것 처럼 프로그래밍으로 네비게이션 관련 작업을 수행할 수 있다.
1. 다른 위치로 이동하기
- router.push()
2. 현재 위치 바꾸기
- router.replace()

35페이지
## Navigation Guard 
Vue router를  통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 네비게이션을 보호   
ex) 인증정보가 없으면 특정 페이지에 접근하지 못하게 함

### 종류


#### router beforeEach
```
router.beforeEach( (to,from ) => {
  return false : 현재 내비게이션을 취소
  retrun Route Location 
})

```
### 컴포넌트 가드 종류
- onBeforeRouteLeave
- onBeforeRouteUpdate
  