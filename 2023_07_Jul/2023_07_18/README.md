>> ### 2023.07.17~18 

> int - 정수 자료형<p>

2진수   :binary      : 0b<p>
8진수   :octal       : 0o<p>
16진수  :hexadecimal : 0x <p>

> float - 실수 자료형

float 는 실수에 대한 근삿값
 - 유한 정밀도
   - 메모리 한정 -> 한 숫자 저장 제한 = 가장 가까운 값!
  ```python
  # 0.6666666666666666
print(2 / 3)
  # 1.6666666666666667
print(5 / 3)
```
지수 표현 방식 
```python
# 314 ∗ 0.01
number = 314e-2

# float
print(type(number))

# 3.14
print(number)
``````
        <class 'float'>
        3.14
```python        
# 실행 해보기 2
a = 3.2 - 3.1 
b = 1.2 - 1.1 

print(a)
print(b)

print(abs(a - b) <= 1e-10) 
 
import math
print(math.isclose(a, b))

0.10000000000000009
0.09999999999999987
True
True
```
음! 봐도 모르겠군! 
대충 두개가 비슷한듯.

> Sequence Types
1. 순서(Sequence) 
   - 값들이 순서대로 저장됨 (정렬 X)
2. 인덱싱 (Indexing)
    - 각 값에 고유한 인덱스, 인덱스를 사용, 특정위치 값 선택, 수정 가능함
3. 슬라이싱 (Slicing)
    - 인덱스 범위 조절하여 부분값 추출 가능
4. 길이 (Length)
    - len()함수로 저장된 값의 개수(길이) 구할 수 있음
5. 반복 (Iteration)
    - 반복문을 사용, 저장된 값들을 반복적으로 처리할 수 있음

> str 문자열
 
문자들의 순서가 있는 변경 불가능한 시퀀스 자료형

' ' 혹은 " "로 표현 <P>
- 중첩 따옴표
```python
# 문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.
print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.')
```
> Escape sequence
>
backslash + 특정 문자 = 특수 기능
일반적 파이썬 문법 잠시 탈출

| 예약 문자 | 내용(의미) | |:------------------: |:------------------: | 

| \n | 줄 바꿈 | <p>
| \t | 탭 | <p>
| \ | 백슬래시 |<p> 
| \’ | 작은 따옴표 |<p> 
| " | 큰 따옴표 |<p>
- [ ] 여기 수정하기... 표 양식으로 
> String Interpolation
> 

  f/F 접두어 + {expression}
  ej.
  ```python
  bug = 'roaches'
  counts = 13
  area = 'living room' #끔찍
  #Debugging roaches 13 living room -출력
  print(f'Debugging {bugs} {counts} {area}')
  #편안합니다. 아래 두 개에 비하면
  print('Debugging {} {} {}'.format(bugs, counts, area)) #예전에 쓰던것 1 // 보는법은 알아두기

  print('Debugging %s %d %s' % (bugs, counts, area)) #고대인의 방법 // 보는법은 알아두기
  ```
  ㅖ. 

```python
my str_'hello'
#인덱싱
print(my_str[1]) # e 
#슬라이싱
print(my_str[2:4]) # ll
#길이
print(len(my_str)) # 5 
# 이런 모양 이런 느낌
my_str[0:0:0] #[시작,끝,간격]
my_str[::-1] #반대로나옴
```
근데 리스트는 가변
> ### tuple  튜플 얘는 불변...
- 소괄호로 (표 기)
- 어떤 자료형이든지 OK 심지어
- 인덱싱, 슬라이싱 OK 단 변경 X 
- 안전하게 여러 값 전달! 그룹화! 다중 할당!
  
>Non-sequence Types

> dict 딕셔너리

     key values 쌍으로 이루어진 순서와 중복이 없는 변경 가능한 자료형
> 
> key는 변경 불가한 자료형
 - key(str, int, float, tuple, range...)
 - value는 모든 자료형
 - {} 중괄호로 ! key : value 모양
  ```python
  my_dict_1 = {'key' : 'value'}
  print(my_dict['key']) #'value'
  my_dict_1['key'] = 'valllllue'
  for key, value in information.items():
      print(key, value)
  #키-밸류 다 불러오기
  ```
> set 세트 (집합)

- 중괄호
- set{1, 2, 3}
```python
  # 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}
#| 는 버티컬바 쉬프트 + \
# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```
>OTHER TYPES 

- None : 값이 없어...

- Boolean  True / False

> Collection
> 
|컬렉션 |변경 가능 여부|나열여부||
|:---:|:---:|:---:|:---:|
| str | X | O | 시퀀스 |
| list | O | O | 시퀀스 |
| tuple | X | O | 시퀀스 |
| set | O | X | 비시퀀스 | 
| dict | O | X | 비시퀀스 |
변경가능에서  dict의 key는 예외.

### 2023.07.18

입학식

 ```python
 #진법 변경  / bin...
 print(bin(12)) # 2진법 #0b1100
print(oct(12)) # 8진 0o14
print(hex(12)) # 16진 0xc
# 실수 연산 해결책 -메모리 한계로 대충 숫자가...
a = 3.2 - 3.1 # 0.10000000000000009 쯤
b = 1.2 - 1.1  # 0.0999999999999987 쯤
# 1. 임의의 작은 수 활용
print(abs(a - b) <= 1e-10>) # True
# 2. math 모듈 활용 
import math
print(math.isclose(a, b)) # True

 ``` 
 f-string 추가

 ``` python
 greeting = 'hi'
print(f'{greeting:^10}' )#     hi     양쪽에 5,4칸씩 공백 추정
print(f'{greeting:<10}') # hi         오른쪽에 9칸 공백 추정
print(f'{greeting:>10}') #         hi 왼쪽에 9칸 공백 추정 

print(f'{3.141592:.4f}') # 소수 4번째까지만 
 ```

편법같은 느낌으로 
set 이용해서 리스트 중복요소 제거 가능.

얕은 복사 조오오금
``` python
list_1 = [1, 2, 3]
list_2 = list_1
list_1[0] = 100
print(list_1)
print(list_2)

#list_2에 list_1을 할당 (값이 아닌 list_1의 메모리 주소를 list_2에 할당)
#list_2[0]이 list_1[0]과 같은 자리에 할당됨
# 따라서 list_2[0]가 list_1[0]과 같은 값이 됨
# 얕은 복사 / 가변 데이터의 특징

x = 10 # 1. x 에 10 할당
y = x  # 2. y 에 x(에서 정의된) 10 할당
x = 20 # 3. x 가 20으로 재할당  ㅌㅌ
print(x) # 20
print(y) # 10

```
Type Conversion
    1. 인터프리터가 알아서 변경
    2. 직접 변경

1번 = 암시적 형변환
- Boolean 과 Numeric Type 에서만 가능
```python
print(3 + 5.0) # 8.0
print(True + 3) # 4 (True = 1, False = 0)
print(True + False) # 1  + 0 
#문자 + 문자 = Err
```
2번 = 명시적 형변환
 - 개발자가 직접 변경함.
 - str -> integer : 형식에 맞는 숫자만 가능
 - integer -> str : 모두 가능
 ```python
 print(int('1')) # 1
 print(str(1) + '등') # 1등
 print(float('3.5')) #3.5 
 print(int(3.5)) # 3 

 print(int('3.5')) 
 #ValueError! float 으로 해야겟지?
 dict{'key' : 'value'} # (key 변경 불가)

d = {'a': 1, 'b': 3, 'c':4}  #d를 리스트로 바꾸자 
lst = list(d) #['a', 'b', 'c']
set_d = set(d) # {'a', 'c', 'b'}

lst = [] #비어있음
lst = list() #암튼 비어있음

s = '' #빈 문자열
d = {} #빈 dict
# s = {} 허용 안합니다 위랑 중복;;;
s = set()

y = 10
y -= 4 # (y = y-4) '6' 
 ```

복합연산자
+=  |a = a + b <p>
-=  |<p>
*=  |<p>
/=  |<p>
//= |<p>
%=  |<p>
**= |<p>


#### 비교 연산자 (대소비교 : <,>도 여기임)
==
!=
is
is not
is 비교 연산자

메모리 내에서 같은 객체를 참조하는지 확인
==는 동등성(equality), is 는 식별성(identity)
is는 되도록이면 None, True, False 비교할때 사용
```python
a = [1, 2, 3] #b와 id가 다르다!
b = [1, 2, 3]
print(id(a), id(b))
r1 = a == b
r2 = a is b
print(r1, r2) #True, False(id 다름)
c = a
print(id(a), id(c)) #a 와 c의 id가 같음. 
print(a==c, a is c) #저장된 위치? 같음 아마도.
```
#### 논리 연산자
    and | 논리곱
    or  | 논리합
    not | 논리부정
비교 연산자와 함께 사용 가능 

- 단축평가<p>
    and
    - 첫 피연산자 False = 전체 False (두번째 무시)
    - 첫 피연산자 True = 두 번째에 결정 (두번째 결과가 전체 표현식의 결과)
  
    or (p.113)
  
```python
#숫자 0은 False 이외 True
print(3 and 5) # 5
print(3 and 0) # 0 
a = 3
if a:
    print('T')
print(0 or 3)

vocales ='aeiou'
print(('a' and 'b') in vocales) #False 
# a and >> True >> and b (True x True) > b > b in vocales > False.
print(('b' and 'a') in vocales) # True
if 'a': #문자열은 True인건가 // 빈 문자열은 False
    print('T') 
```
#### 멤버쉽 연산자

in <p> 왼쪽 피연산자가 오른쪽 피연산자 시퀀스에 속하는가 <p>
not in <P>왼쪽이 오른쪽에 없는지
```python
chars = 'apple'
s = 'aeiou'
for c in chars:
    if c not in s:
        print(c) #자음만 출력된다.
```
#### 시퀀스형 연산자
``````
+ 결합
* 반복
``````

[돌아가기](../../2023년7월2023Julio.md/##20230718)

[이전](../2023_07_17/README.md)


[다음](../2023_07_19/README.md)