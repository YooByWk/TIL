
### 2023_07_20

제어문

> 조건문 - Conditional Statement
주어진 조건식 평가 > True 일때만 일함
if / elif / else

```python
if abc:
    블록 1
elif abc:
    블록 1
else: #위 두개가 모두 False일때

    블록 1 
```
> 반복문 Loop Statement<p>
주어진 코드 여러번 반복
1. 특정 작업 반복<p>
2.주어진 조건이 참인동안

for / while

'for' statement
임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복<p>
기본 구조
```python
for 변수 in iterable:
    블록
    블록
```
iterable - 반복가능한 객체. (시퀀스 객체 + dict + set)
 
<p> for문 원리 
- 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록 실행
-  반복 변수 리스트 2번째 항목 할당, 코드블록 실행
-  ... 마지막으로 반복변수에 리스트 마지막 할당, 코드블록 실행 

```python
items = ['apple', 'banana', 'coconut']
for item in items:
    print(item) # apple // banana // coconut    

문자열 순회
country = 'corea'
for char in country: # c // o // r // e // a
    print(char) #문자열도 시퀀스다.

range 순회
for i in range(5):
    print(i) # 0 // 1 // 2 // 3 // 4

인덱스로 리스트 순회
리스트의 요소가 아닌 인덱스로 접근하여 해당 요소 변경
numbers = [4, 6, 10, -8, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers) # [8, 12, 20, 16, 10]

중첩 for 문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)
# (A, c) // (A, d) // (B, c) // (B, d)

elements = [['A', 'B'], ['c', 'd']]

중첩 리스트 순회 #2차원 리스트
for elem in elements:
    print(elem)

"""
['A', 'B']
['c', 'd'] 바깥 리스트만 접근가능
"""
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    for item in elem:
        print(item)

"""
A       내부 리스트까지 접근함
B
c
d
"""
```

'while' statement
- 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 == 조건식이 거짓(False)가 될 때 까지 반복


while statement의 기본 구조
```python
while 조!건!식!:
    블록 #if처럼 생겼네요
a = 0 
while a < 3:
    print(a)
    a +=1
print('GG')
# 0 // 1 // 2 // GG
---
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')
"""
양의 정수를 입력해주세요.: 0
0은 양의 정수가 아닙니다.  
양의 정수를 입력해주세요.: -1
음수를 입력했습니다.       
양의 정수를 입력해주세요.: 1
잘했습니다!
"""
```
**while은 반드시 종료조건**<p>

for / while<p>
파이썬 반복문에 사용되는 키워드
for<p>
iterable의 요소를 하나씩 순회하며 반복
while<p>
주어진 조건식이 참인 동안 반복
적절한 반복문 활용하기


for<p>

    반복 횟수가 명확하게 정해져 있는 경우에 유용예를 들어 리스트, 튜플, 문자열 등과 같은 시퀀스 형식의 데이터를 처리할 때
        
 while<p>

    반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 때 유용
    예를 들어 사용자의 입력을 받아서 특정 조건이 충족될 때까지 반복하는 경우

반복제어! 
break - 반복 즉시 중지
continue - 다음 반복으로 건너뜀

남용 X

주의 : 명확하게 작성하도록 노력하시오 
```python 
number = int(input('양의 정수를 입력해주세요.: '))

while number <= 0:
    """
    종료 조건과 break
    """
    if number == -9999: 
        print('프로그램을 종료합니다.') #while adios
        break

    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')

    number = int(input('양의 정수를 입력해주세요.: '))

print('잘했습니다!')

"""
양의 정수를 입력해주세요.: -9999
프로그램을 종료합니다.
잘했습니다!
"""
```
 -아직도 반복문임-
 List Comprehension (효율적 리스트 생성법)
 ```python
 [expression for 변수 in iterable]
list(expression for 변수 in iterable)

# List Comprehension
사용 전

numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)  # [1, 4, 9, 16, 25]
사용 후

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]

print(squared_numbers)  # [1, 4, 9, 16, 25]
# 가독성 vs 간결

new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# 홀수 정수, 짝수 문자열, elif 안됨 if if if if if if if if  됨 

new_list3 = []
for i in range(0,10):
    if i % 2 == 1:
        new_list.append(i) #i를 range만큼 넣음.
    else: 
        new_list.append(str(i)) #위 new list3랑 같지만 가독성 더 좋음
---

# 리스트 만들기 3가지 방법의 비교 
# ej : 정수 1, 2, 3을 가지는 새로운 리스트 만들기
# 상황별로 걍 편하게 쓰세요
# 속도만 따지면 '대부분'의 상황에서는 compre가 빠르다.
# 하지만 다른 함수, 내장함수에 따라 map이 더 빠른 경우도 많았다.
# Python 3.X (후반에) for loop 성능에 비약적 향상이 있었다.
# 극단적 차이는 X.
# 가독성이 매우 중요하다.

numbers = ['1', '2', '3']
# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

#2. map
new_nmbers_2 = list(map(int, numbers))
print(new_numbers_2)

# 3. list comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)

"Simple is better than complex"
"keep it simple, stupid"
 ```
pass - 아무것도 안함. 진짜로 아무것도 안함 
1. 미완성부분 -추후 구현, (컴파일중 오류 피하기)
2. 조건문 패스
3. 무한루프에서 조건이 충족되지 않을 때 pass

Enumerate.
enumerate
```python
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'인덱스 {index} : {fruit}')
```
```python 
# enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'인덱스 {index} : {fruit}')
# 인덱스 0 : apple
# 인덱스 1 : banana
# 인덱스 2 : cherry
# enumerate
result = ['a', 'b', 'c']
print(enumerate(result))  # <enumerate object at 0x0000020114BC4BC0>
print(list(enumerate(result))) # [(0, 'a'), (1, 'b'), (2, 'c')] - tuple

for index, elem in enumerate(result): # tuple 언패킹
    print(index, elem) # 0 a // # 1 b // # 2 c
```
문장 - 실행 가능한 동작을 기술하는 코드 (조건문 반복문 함수정의)
 - expression(평가대상임)으로 만:?든?:다


[돌아가기](../../2023년7월2023Julio.md/##20230720)

[이전](../2023_07_19/README.md)


[다음](../2023_07_21/README.md)