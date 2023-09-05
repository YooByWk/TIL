# 2023_09_05

css

인터넷 이슈로 듣기 힘들었음
## CSS Box Model
모든 HTML 요소를 사각형 박스로 표현하는 개념
- 내용(content)
- 안쪽 여백 (padding)
- 테두리 (border)
- 외부 간격(margin)
  
## block 타입
- 항상 새로운 행으로 나뉨
- width / height 속성으로 너비와 높이 지정 가능
- 기본적으로 width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간을 모두 사용함
- 대표유형 : h1~6, p, div
## inline 타입
- 새로운 행으로 나뉘지 않음
- width 와 heigth 속성을 사용할 수 없음
- 수직방향 
  - padding, margins, borders가 적용되나 다른 요소를 밀어낼 수 없음
- 수평방향
  -  padding, margins, borders가 적용되어 다른 요소를 밀어낼 수 있음
- 대표적인 유형 : a, img span 

### inline-block
- inline 과 block 요소 사이의 중간 지점을 제공하는 display 값
- block 요소의 특징을 가짐
  - width, height 속성 사용 가능
  - padding, margin 및 border로 인해 다른 요소가 밀려남
- 요소가 줄바꿈 되는 것을 원하지 않으면서(inline) / 너비와 높이를 적용하고 싶은 경우(block)

### none
아무것도 없음.

## Position

1. static
   - 기본값
   - 요소를 Normal Flow에 따라 배치
2. absolute
   - 집나간 자식 , 절대 위치
   - relative 부모가 있는게 좋음
   - 요소를 Normal Flow에서 제거
   - 가장 가까운 relatvie 부모 요소를 기준으로 이동
   - 문서에서 요소가 차지하는 공간이 없어짐
3. relative
   - 외출한 자식
   - 자기 자신을 기준으로 이동
   - 요소가 차지하는 공간은 static일 때와 같음
4. fixed
   - 고정위치 
   - 요소를 Normal Flow 에서 제거
   - 현재 화면영역을 기준으로 이동(vieport)
   - 문서에서 요소가 차지하는 공간이 없어짐
5. sticky
   - 요소를 Normal Flow에 따라 배치
   - 요소가 일반적인 문서 흐름에 따라 배치되다가 스크롤이 특정 임계점에 도달하면 그 위치에서 고정됨
   - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky  요소의 자리를 대체 
###  z-index
정수 값을 사용해 Z축 순서를 지정
더 큰 값을 가진 요소가 작은 값의 요소를 덮음 // 맨 위로 올리기
## CSS Flexbox
요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식
공간배열 정렬.

main axis
- 기준
cross axis
- main에 수직

### Flex Container
- dispaly : flex; 혹은 display: inlein-flex; 가 설정된 부모 요소
- *이 컨테이너의 1차 자식 요소들이 Flex Item이 됨*
- flexbox 속성 값들을 사용하여 자식 요소 flex item을 배치
- 
배치 
flex-direction / flex-wrap
공간분배 
justify-content / align-content
정렬
align-item / align-self

