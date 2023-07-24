
### 2023_07_19

### 함수!
    특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
    재사용성 / 가독성 / 유지보수성

#### 내장함수
파이썬이 기본적으로 제공하는 함수
별도의 import 필요 X
```python
#사실 얘도!?
print() #return이 없는 함수.
len()
abs() # abs 함수 호출의 반환 값을 result에 할당함.
return #은 함수의 종료 / 결과를 호출부분에 반환.
---

#함수 호출
function_name(arguments) #암튼 실행함

def make_sum(pram1, pram2):
    #pram - 매개변수 (parameter)
    #인자 - argument 
    """ << docstring (주로 함수 설명)
    이것은 두 수를 받아 두 수의 합을 반환하는 함수임.
    >>> make_sum(1, 2)
    3
    """ 
    return pram1 + pram2
```
[python documentation](https://docs.python.org/ko/3/) 무려 자습서도 있음

```python
# 함수 정의
def greet(name):
    """입력된 이름 값에 
    인사를 하는 메세지를 만드는 함수
    """
    message = 'Hello, ' + name
    return message
# 함수 호출
result = greet('Alice')
print(result)

```
매개변수 - parameter
- 함수를 정의할 때 함수가 받을 값을 나타내는 변수<p>
인자 - argument
- 함수를 호출할 때, 실제로 전달되는 값

```python
def add_numbers(x, y): #x, y 매개변수
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numbers(a, b) #a, b 인자
```
>Positional Arguments (위치인자)
- 함수 호출 시 인자의 위치에 따라 전달되는 인자
-  위치인자는 함수 호출 시 반드시 값을 전달해야 함.

> Default Argument Values.
- 함수 정의에서 매개변수에 기본 값을 할당하는 것
- 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당.

```python
def greet(name, age = 30):# age가 기본인자. (인자 전달 안하면 기본값이 할당)
    print(f'안녕하세요, {name}님! {age}살이시군요!')
```
> Keyword Arguments( 키워드 인자)

매개변수와 인자를 일치시키지 않고 특정 매개변수에 값을 할당할 수 있음

인자의 순서는 주용하지 않으며, 인자의 이름을 명시하여 전달

  *단 호출 시 키워드 인자는 위치 인자 뒤*
  
```python
  #키워드 인자
def greet(name, age):
    print(f'안녕하세요, {name}님! {age})

greeting('Alice', 25) # 안녕하세요, Alices님! 25
greeting(25, 'Alice') # 안녕하세요, 25님 Alice
greeting(age = 25, name= 'Alice') # 안녕하세요, Alices님! 25
greeting(age=25, 'Dave')
#positional argument follows keyword argument. 문법에러.
```
Arbitrary Argument Lists (임의의 인자 목록)
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*' 붙여 사용
- 여러개의 인자를 **tuple**로 처리
```python
def calculate_sum(*args):
    print(args)
    total = sum(args)
    print(f'합계: {total})
    """
    (1, 2, 3)
    합계: 6
    """


``` 
Arbitrary Keyword Argument Lists(임의의 **키워드 인자** 목록)
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 정의 시 매개변수 앞에 ** 
-  dictionary로 묶어 처리 {A:B}
```python
def print_info(**kwargs):
    print(kwargs)

print_info(name ='Eve', age = 30)
#{'name' : 'Eve', 'age' : 30}
```
함수 인자 **권장** 작성순서
위치 > 기본 > 가변 > 키워드 > 가변 키워드
호출 시 인자를 전달하는 과정에서 혼란 줄임<p>
단, 절대적 규칙은 아님.

```python
print(*objects,sep= ' ',end='\n', file=sys, stdout, flush=False)
 # 프린트문 줄바꿈 하는 이유가 여기 있었네
 # 그래서 \n(기본인자)을 바꾼다면
 print('hello',end= ' ') #\n 대신 ' '공백 
```
Python의 범위
- 함수는 코드 내부에 local scope 생성/
- 그 외의 공간 global scope로 구분
    -scope
        -global scope :코드 어디서든 참조가능
        - local scope : 함수가 만든 scope(함수 내부에서만 참조 가능)
    - variable
        - global variable : global scope에 정의된 변수 
        - local variable : local scope에 정의된 변수
  ej. 변수의 수명주기
```python
  def func():
    num = 20 
    print('local',num) # local 20
func() 
print('global', num) # NameError : name 'num' is not defined.
```
수명주기 (lifecycle)
1. built-in scope
   -파이썬 내장
2. global scope
   - 모듈 호출 시점
3. local scope
   -함수가 호출 될 때 생성 , 함수 종료까지 유지
이름 검색 규칙 (Name Resolution)
파이썬에서 사용되는 이름은 특정한 이름공간(namespace)에 저장되어 있음
아래 순서로 찾아나감 LEGB Rule 이라고 부름
1. local scope (현재 작업범위)
2. Enclosed scope 한단계 위 범위
3. Global scope 최상단
4. Buil-in scope. 모든 것(정의하지 않고 사용 가능한 모든 것)
   함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 불가함. 

LEGB Rule ej.

sum이라는 이름을 global scope에서 사용하게 되면서 기존 built-in scope의 sum 사용 못하게 됨
```python

print(sum) # <built-in function sum>
print(sum(range(3))) # 3

sum = 5

print(sum) # 5
print(sum(range(3))) # TypeError: 'int' object is not callable

#다른 예시
#### LEGB Rule 예시 2

a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) # 10 2 500

    local(500)
    print(a, b, c) # 10 2 3


enclosed()
print(a, b) # 1 2

```
global 키워드
- 변수 스코프 전역범위로
- 일반적으로 함수 내에서 전역변수를 수정하려는 경우
- 매개변수에 X
- (가급적 사용X 권장 / )
```python
num = 0 # 전역 변수


def increment():
    global num # num를 전역 변수로 선언
    num += 1


print(num) # 0
increment()
print(num) # 1
```
#### 재귀함수!
- 1개 이상의 base case, 수렴하도록 작성
- 무한호출 조심 / 반복 호출이 종료조건을 향하게 <p> 
ej. 팩토리얼(5!)
f(4) = 4 * f(3)
f(3) = 3 * f(2)
f(2) = 2 * f(1)
f(1) = 1
```python
def factorial(n):
    #종료 조건 n이 0이면 1을 반환
    if n == 0:
        return 1
    #재귀 호출 : n과 n-1의 팩토리얼을 곱한 값 반환
    return n * factorial(n-1)

#계산예시
result = factorial(5) # 여기가 최종결과 장소
print(result) # 120
```

유-용 내장 함-수
1. map
2. zip(*literable) (zip(a,b,c,...,etc))
 : 임의의 iterable을 모아 튜플을 원소로 하는 zip object 반환
```python
map(funcion, iterable) #iterable : 반복가능 객체
#그리고 맵 오브젝트로 반환



```
lambda 함수 - 익명함수
```python

lambda 매개변수 : 표현식(,범위)

def addition(x,y):
    return x + y

result = addition(3, 5)
print(result) #8

addition = lambda x, y : x + y
result = addition(3, 5)
# (설명용 예시)

```

> Packing & Unpacking

- Packing 
  <p>여러개의 값을 하나의 변수에 묶어 담는 것

  괄호 디졋 
```python
packed_values = 1, 2, 3, 4, 5
print(*packed_values)  # 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
# a 1개 c 1개 b 나머지 (3개)
```
- Unpacking 
  <p> 패킹된 변수의 값을 개별적인 변수로 분리하여 할당하는 것
```python
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values #알아서 잘라버린듯
print(a, b, c, d, e)  # 1 2 3 4 5

def my_function(x, y, z):
    print(x, y, z)

my_dict = {'x': 1, 'y': 2, 'z': 3}
my_function(**my_dict)  # 1 2 3 #
    # * 리스트 튜플
    # ** 딕셔너리 키 값 쌓
```
### 모듈 Module
Aㅏ...<p>
한 파일로 묶인 변수와 함수의 모음<p>
특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)

ej.
```python
import math
print(math.pi)  # 3.141592653589793    
print(math.sqrt(4))  # 2.0
```
[math module 참고](https://docs.python.org/3/library/math.html)
<p> or 

```python

help(math) #<- 모듈에 뭐 있는지 확인
"""
. (dot)’은
 “점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라“ 라는 의미의 연산자
"""
# 모듈명.변수명
print(math.pi) #math의 pi 쓸것

# 모듈명.함수명
print(math.sqrt(4))

"""
모듈을 import하는 다른 방법
from 절을 활용해 특정 모듈을 미리 참조하고 어떤 요소를 import 할지 명시
"""
from math import pi, sqrt


print(pi)

print(sqrt(4))

# 마지막에 import된 이름으로 대체됨

from math import pi, sqrt
from my_math import sqrt

# 그래서 모듈 내 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

from math import * #<- 흐즈믈르그
```
모듈 만들어서 써봤음.

### [파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html)<p>
구경 ㄱ

패키지 : 관련된 모듈들을 하나의 디렉토리에 모은 것
```python
from my_package.math import my_math
# mpcg 패키지의 math 패키지의 my_math 모듈
```
내부 패키지 : 걍 쓰세요<p>
외부 패키지 : pip 사용 후 import 필요<p>
pip 파이썬 패키지 관리자<p>
PyPI에 저장된 외부 패키지들을 설치

패키지 :<p> 모듈의 이름 공간을 구분하여 충돌 방지<p> 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할.
\
정의 , 호출은 다른 것 (재귀)



[돌아가기](../../2023년7월2023Julio.md/##20230719)

[이전](../2023_07_18/README.md)


[다음](../2023_07_20/README.md)