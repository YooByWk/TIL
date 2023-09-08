# 2023_09_06

## Bootstrap 
CSS 프론트엔드 프레임워크(Toolkit)
- 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함
- reboot -> css 초기화? 
- 사용해볼 것
- 기본 사용법
  ```css
  <p class="mt-5">Hello, world!</p>
  /* {property}{side}-{size}*/
  ```
클래스 이름으로 Spacing 표현 가능
- property
  - m : margin
  - p : padding 
- Sides
  - t : top
  - b : bottom
  - s : left
  - e : right
  - y : top bottom
  - x : left, right
  - blank : 4 sides
- Size
  - 0 : 0 rem 0 px
  - 1 : 0.25 rem 4px
  - 2 : 0.5 rem 8 px
  - 3 : 1 rem 16px
  - 4 : 1.5 rem 24px
  - 5 : 3 rem 48px
  - rem : 상대적..크기?

### Typography
제목, 목록 

#### heading
```
<h1>h1. Bootstrap heading</h1>
```
#### display headings
```
<h1 class="display-1">Display</h1>
```
### Semantic Web 
웹 데이터를 의미론적으로 구조화된 형태로 표현하는 형식

#### HTML Semantic Element
기본적인 모양과 기능 이외에 의미를 가지는 HTML 요소
- 검색엔진 및 개발자가 웹페이지 콘텐츠를 이해하기 쉽도록
  - header
  - nav
  - main
  - article
  - section
  - aside
  - footer