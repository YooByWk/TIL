# 2023_09_07

## emmet 활용..? 
'>' 자식결합자
```html
ul.nav.>li.nav-item*4>a{메뉴 $}
  <!-- 아래의 결과가 나온다. -->
  <ul class="nav">
    <li class="nav-item"><a href="">메뉴 1</a></li>
    <li class="nav-item"><a href="">메뉴 2</a></li>
    <li class="nav-item"><a href="">메뉴 3</a></li>
    <li class="nav-item"><a href="">메뉴 4</a></li>
  </ul>
```
- emmet cheat sheet 구글링?
## Bootstrap Grid system
웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
### Grid system 의 목적 
반응형 디자인을 지원해 웹 페이지를 모바일 태블릿 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움
### Grid system 기본 요소
1. Container : column 들을 담고 있는 공간
2. Column : 실제 컨텐츠를 포함하고 있는 부분
3. Gutter : 컬럼과 컬럼 사이의 여백 영역
- 1 개의 row안에 12칸의 column 영역이 구성
- 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨
#### Grid system 실습 - 상쇄(offset)

##### 번외 : Float
layout 
- 1.**Display**
- 2.**Position**
- 3.**flexbox**
- 4.**grid system**
- 5. *Float*  
  - 위의 1~4의 등장 이전에...
  - 신문같은 layout을 만들고 싶었다...
  - 본래 배치의 목적을 가지고 나온건 아니었으나...
  - 쓰다보니까 이곳저곳에 위치 배열이 되네,,,
  - 다른 것이 많이 나온 요즘은 신문같은 유형의 문서에나 사용하는 편
  - 카테고리 또한 legacy
#### Gutters
Grid system에서 column 사이에 여백 영역 
x축은 padding y 축은 margin으로

## Grid system for Responsive Web
### Responsive web
디바이스 종류나 화면 크기에 상관없이,
어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

Bootstrap grid system에서는 12개 column과 6개 breakpoints를 사용하여 반응형 웹 디자인을 구현
### Breakpoints
웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점 
- 화면 너비에 따라 6개의 분기점 xs,sm,md,lg,xl,xxl
- xs : <576 px
  -class prefix : .col-
- sm : >= 576 px
  -class prefix : .col-ssm
- md : >=768 px
  -class prefix : .col-md
- lg : >=992  px
  -class prefix : .col-lg
- xl : >= 1200 px
  -class prefix : .col-xl
- xxl : >= 1400 px
  -class prefix : .col-xxl
ej. col-sm-4
- 이 사이즈에선 col4 로 합니다.