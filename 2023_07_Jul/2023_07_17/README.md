>> ### 2023_07_17
---
> Numeric Type
  - int, float, complex
<br>
> Sequence Types 

- list, tuple, range

- Text Sequence Type 
    - str
-  Set Types
   -  set 
- Mapping Types
  -  dict<br>
- Etc.
  <p>None, Boolean, Funcion<p>
---
표현식 (순차적으로 평가) > 동작
``` python
degrees = 36.5 #할당문 예시
#변수 에 36.5 할당
number = 10
double = 2 * number
print(double) # 20

number =5 
print(double) # 10

```
> Style Guide
코드의 일관성과 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음

[peps.python.org/pep-0008]([peps.python.org/pep-0008])
<p>

- 변수명은 무엇을 위한 변수인지 확인 위한 직관적 작명

- 공백(spaces) 4칸을 사용하여 코드블록 들여쓰기

- 한 줄의 길이는 79자로 제한, 길어지면 줄 바꿈
문자와 밑줄((Snake_case))을 사용하여 함수, 변수, 속성의 이름 작성<p>
- 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄 추가<p>

```python
a = 1 
b = 2
c = a + b

num1 = 1
num2 = 2
sum_result = num1 + num 2

num = [1, 2, 3, 4, 5] #님아 이건 리스트잖아요
# nums or num_list 요렇게 하는게 더 좋겟 죠?
for number in numbers:
    #요론 예시 때문에
student_grades = [ 24, 74, 6]
is_asd -> True / False  의 느낌

#시간 예시 (상수)
secs = 60    #|
minute = 60  #| 셋다 고정값이니까
hours = 24   #| 대문자로 합시다
#>>>
SECONDS_PER_MINUTE = 60 # 이런 느낌

def sample():
    adadadadadad #정말 깔끔하게 말이죠
    sdfaasdfasdfsdaf

def asdsadasd():
    asdafasf    #우리 좀 깔끔하게 살아봐요
    sadfasdfkj

RESULT=2+3*(4-5)/2 #제발 이러지 마세요
result = 2 + 3 * (4 - 5) / 2  #편안

def sample():
    """
    주로 설명용
    ej. 이 함수는 아무튼 함수입니다. 
    얘도 주석이네 헉 or Ctrl + / <- 일반적
    주석 : 설명 / 임시 비활성 
    이해 / 문서화
    의도 동작 설명
    """ 

```
jupyter notebook 사용 연습<p>
설치 > notion/index 참조<P>
키 > notion/PJT
실행해보면서 문서 만들기 가능<p>
python tutor와 jupyter nothebook은 "학습도구"


[돌아가기](../../2023년7월2023Julio.md/##20230717)

[이전](../2023_07_16/README.md)


[다음](../2023_07_18/README.md)