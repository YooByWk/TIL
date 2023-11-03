# 1023 - Introduction of JavaScript

## Histroy

Brandon Eich! -> js 파편화 -> 웹 표준 "ECMAScript"

## ECMAScript

표준화된 스크립트 프로그래미우 언어 명세  
스크립트 언어가 준수해야 하는 규칙 세부사항 제공

> ECMAScript는 JavaScript의 표준이다.(ecma : 언어의 핵심 정의)  
> JavaScript는 ECMAScript 표준을 따르는 구체적 프로그래밍 언어다.

ECMAScript (es6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루었음 중요버전임.

JavaScript의 현재 :

- 다양한 웹브에서 씀, 동적 기능 구현 + Node.js와 같은 서버 사이드 분야, 프레임워크 라이브러리 -> 웹 필수 언어

## DOM
> the Document Object Model

JS : 웹 페이지의 동적 기능 구현

### DOM 특징:

- DOM에서 모든 요소 속성 텍스트는 하나의 객체
- 모두 document 객체의 자식으로 구성됨 (브라우저는 html문서 해석 -> DOM tree 객체 트리 구조화)
- > 객체 간 상속 구조 존재
- 핵심 : 문서의 요소를 객체로 제공, 다른 언어에서 접근 조작할 수 있는 방법을 제공하는 API

### document 객체

- 웹 페이지 객체
- DOM Tree 의 진입점
- 페이지 구성 모든 객체 요소 포함

### DOM 선택

웹 동적으로 변경 == 웹 조작하기 - 선택 후 속성 콘텐츠 조작

#### 선택 메서드

1. document.querySelector() : 한 개
   - 제공한 선택자와 일치하는 element 한 개
   - 'css selecotr'를 만족하는 첫 element 객체 반환 (없다면 null)
2. document.querySelectorAll() : 여러개
   - 제공한 선택자와 일치하는 여러 elemnet 선택
   - ' css selector'를 만족하는 NodeList 반환

### DOM 조작 

#### 클래스 속성 조작 : 'classList' 
- element.classList.add()
  - 지정한 클래스 값을 추가
- element.classList.remove()
  - 지정 클래스 값 제거
- element.classList.toggle()
  - 클래스가 존재하면 제거 후 false / 없다면 추가 후 true-
#### 일반 속성 조작 
- Element.getAttriburte() (1023///49p)
