# 스페인어 배웠는데 어쩌다 코딩.
## 2023.07.13.JUE/목

# 누더기 
### 첫날!
---

```python
days = list(map(int, input().split()))
print(days)
a = 0
cnt = 0
for d in days:
    a = a + d
    cnt = cnt + 1
print(len(days))
print(a // len(days))
print(a, cnt)
print(days[0:3])
# 온도 평균..? 실험!
```
- 부끄러운 구구단
```python
for i in range (1,10):
    print(3*i) #3단 만들기

for k in range (2, 10):
    for l in range (1,10):
        print(k, "x", l, '=' k * l)
        if l < 10:
            l + 1
        else:
            l = 1
    print('------') # 각 단 (for i ~가 실행된 후) ------가 출력된다! 단 구분
# 구구단
```
천천히 생각하면서 코딩을 해봐야할것같습니다.<br>
위의 if는 전혀 쓸모가 없었다! 어차피 for가 알아서 다 해주니까!
```python
range(0,a+1)
#0부터 a까지!
```
```python
for i in range(1, 11):
    print(i)
    #judge = i<5
    if i < 5:
        print('*****')
```

     1. 프린트 순서 생각해보기
     2. 특정 숫자 넘어갈때도 쓸 수 있을것같다 


```python
n = int(input())
if n == 0:
    print('0입니다!')
elif n % 2 == 0: #홀짝!
    print(str(n)+'은/는 짝수입니다.')
else:
    print(str(n)+'은/는 홀수입니다.')
```
띄어쓰기가 싫어서 str을 넣어봤는데 원리는 아직 모르겠다.

```python
d = int(input()) #저는 미세먼지가 싫어요.
if d >= 151:
    print('매우나쁨')
elif 81<=d<=150:
# 다른 언어는 n>= 81 and n<=150 요래 해야 한다고 합니다. 
    print('나쁨')
elif 31<=d<=80:
    print('보통')
else:
    print('좋음')
```
아무튼 그래요. 근데 음수 넣으면 이상할것같은데...

1.
```python
n = [1, 2, 4 ,5, 6, 0, 1, 0 ,2]
cnt = 0
for i in n:
    if i == 0:
        break #for에서 빠져나감
    else: #0이 아니면 cnt에 1을 더함
        cnt += 1
print(cnt) #cnt 값
```
> break의 위치와 cnt +=1의 위치가 중요함!
>> 더하고 나갈 것인가, 나갈 경우에는 더하지 않을 것인가 <p>
>> 자리는 0부터 시작한다<br>
2.
```python
n = [1, 2, 4 ,5, 6, 0, 1, 0 ,2]
pos = 0
# print(n[cnt:cnt+1])
while n[pos] != 0 :
    pos = pos + 1 
print(pos)
```
        for v. while 
~~근데 내가 할때는 왜 멈춘거지~~ << index도 알아보자.

```python 
numbers = [1, 2, 3, 0]
pos = 0
while True:
    n = numbers[pos]
    if n == 0:
        print(n)
    pos = pos + 1
    #list index out of range 오류 나옴.
    #while이 폭주합니다!
```
---
### 2023.07.14
```python
import random  #모듈 활용?
i = list(range(1, 20))
print(i)
cnt = 0

while True:
    k = random.sample(i , 6)
    k.sort()
    cnt += 1
    print(k)
    print(cnt)
    if k == [1, 2, 3, 4, 5, 6]:
        break
```
        [1, 2, 3, 4, 5, 6]
        33942
로또 반도 안되는 숫자인데 음 . . .

> #### 오후

```python
numbers = [1, 2, 4, 0, 5, 6, 3, 1, 4, 2]
l = len(numbers)
pos = 0
# cnt = 0
# for n in numbers:
#     cnt += 1
# l = cnt 
# pos = 0   // 여기까지가 len이 하는 일
while pos <l :
    n = numbers[pos]
    if n == 0:
        break
    pos = pos + 1
if pos< l:
    print(f'numbers의 {[pos]}에 0이 있음')
else:
    print('no hay 0')
#0 위치찾기

numbers = [3, 4, 2, 8, 10, 2]
print(max(numbers), max(2,3, 4, 1))
newn = sorted(numbers)
print(newn)
```
간단(어려웠던) 실습. 함수의 소중함을 느끼게 만들지도 몰라요
>#### SWEA 1959!
> swea - 사전학습 中
```python
t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    sum = []
    if a < b:
        for i in range(b-a+1):
            k = 0
            for j in range(a):
                k += a_list[j] * b_list[j+i]
                sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
    elif a > b: # a > b
        for i in range(a-b+1):
            k = 0
            for j in range(b):
                k += b_list[j] * a_list[j+i]
                sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
    else:
        for i in range(a):
            k = 0
            k += a_list[i] * b_list[i]
            sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
```
실패 N시간째 진행중
몇몇 케이스가 이상하게 나옴.
> #### SWEA 1959!
```python
t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    
    if a < b:
        n1 = b
        n2 = a
    else:
        n1 = a
        n2 = b`
    sum = []
    
    if a < b:
        for i in range(b-a+1):
            k = 0
            for j in range(a):
                k += a_list[j] * b_list[j+i]
                sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
        print(sum)
    elif a > b: # a > b
        for i in a_list:
            k = 0
            for j in range(b):
                k += b_list[j] * a_list[j+i]
                sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
    else:
        for i in range(a):
            k = 0
            k += a_list[i] * b_list[i]
            sum.append(k)
        sum.sort()
        print(f'#{test_case} {sum[-1]}')
```
퇴실 전 마지막 - 강사님 도움받은 것
sum 값 체크해보기

### 2023.07.16 (Dom, 일요일)
> #### SWEA 1959!
```python
t = int(input())
for test_case in range(1,t+1):
    a, b = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    sum = []
    if a < b:
        for i in range(b-a+1):
            k = 0
            for j in range(a):
                k += a_list[j] * b_list[j+i]
            sum.append(k)
        # sum.sort()
    elif a > b: # a > b
        for i in range(a-b+1):
            k = 0
            for j in range(b):
                k += b_list[j] * a_list[j+i]
            sum.append(k) # 기존에는 매번 집어넣었기에 합계가 아니었음
            #한번 (작은 칸 곱) 끝날때 합계만 리스트에 넣는다는 뜻
        # sum.sort()
    else:
        for i in range(a):
            k = 0
            k += a_list[i] * b_list[i]
        sum.append(k)
    sum.sort()
    print(f'#{test_case} {sum[-1]}')
```
변경사항 : 
```python
sum.sort # 위치 변경
print(f'#{test_case} {sum[-1]}') # 위치 변경
# 마지막에 한번 정리, 출력하면 되는거니까 문제 X 마자막에 한번만.
sum.append(k) # 자리 변경
```
PASS! 

### 2023_07_17
#### SWEA 1984 / D2

```python
TC = int(input())
for tc in range(1,TC+1):
    numbers = list(map(int, input().split()))
    # print(numbers) #실험용
    #for -> if 로 하나씩 대소관계 파악하고 임시저장 > 최대값
    ahora_max = -1    #조건보다 1 작게함 = 항상 얘보다 큰놈만 나옴
    ahora_min = 10001 #조건보다 1 크게함 = 항상 얘보다 작은놈만 나옴
    temporal = 0      #계산 임시 저장용
    for i in numbers:
        if i > ahora_max: # 최대
            ahora_max = i
        if i < ahora_min: # 최소 
            ahora_min = i
        temporal += i  #리스트 요소 하나씩 더해줌
    temporal = int((temporal - (ahora_max + ahora_min)) / (len(numbers)-2)+0.5)
    # 답 계산해주고
    
    print(f'#{tc} {temporal}') #출력

```
함수 안쓰고 Pass 라고 하려했으나 len() 써버림


## 2023_07_19 mie
유용한 함수 
```python
nums = [1, 2, 3]
result = map(str, numbers)

print(result) # <map object at XX>
print(list(result)) [1, 2, 3]

result = []
for number in numbers:
    result.append(str(number))
#둘이 같다. map 그는 신이야
#순회 가능한 데이터구조의 모든 요소에 함수를 적용!
#결과를 맵 오브젝트로 반환

los_chicos = ['juan', 'mario']
las_chicas = ['maria', 'ximena']
pair = zip(los_chicos, las_chicas)
print(pair)
print(list(pair))

#map + lambda
# lambda 매개변수 : 표현식(,범위)
numbers = [1, 2, 3, 4, 5]
result = list(map(lambda x : x* 2,numbers))
print(result) # [2, 4, 6, 8, 10]
#명시적이지는 않음.
```
팩토리얼!
```python
# 5! = 5 * 4!
def factorial(n): #  n = 5
    if n == 0:
        return 1
    t = n * factorial(n-1)
    return t
print(factorial(5)) #pos_argu
# f(5) - f(4) -f(3) f(2) - f(1) 하나씩 하고 역순으로 return 받으며 끝

복사 해보기
def my_p(lst):
    t = lst[::] 
    t = list(lst) #복사-일시적으로 
    t.append(10) #id : x
    print(t)
    return


k = ['a', 'b'] #id : x

my_p(k)
print(k)

---
global 사용 O/X 사례
res = 0 #넓-다.

def double_a(a):
    """
    입력으로 정수를 하나 입력받아서 2를 곱한 결과 출력.
    """
    # global res # 전역으로 
    t = a*2
    res = t # 지역 번수임
    return t # 지역 변수 res= t 소멸

var_a = 10
res = double_a(var_a) # global 안쓰려고 res의 값을 함수 돌려서 받음.
print(res)
```

작업하시오
```python
#ws_3_5.py

import book

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1






def create_user(name, age, address):
    global user_info
    user_info = {'name': name , 'age': age , 'address' : address}
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info #이거 중요
    
 #여기까지 완료. 환영합니다!


def rental_book(info):
    aa = {'name': name, 'age' : age}
    book.decrease_book(age//10)

    print(f'{name}님이 {age//10}권의 책을 대여하였습니다.')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))

# print(many_user) 
# [{'name': '김시습', 'age': 20, 'address': '서울'},
#  {'name': '허균', 'age': 16, 'address': '강릉'}, 
#  {'name': '남영로', 'age': 52, 'address': '조선'}, 
#  {'name': '임제', 'age': 36, 'address': '나주'}, 
#  {'name': '박지원', 'age': 60, 'address': '한성부'}]

#info {name : age}

info3 = list(map(lambda x : {'name': x['name'], 'age' : x['age']}, many_user))
print(info3)

rental_book(info3)


# print(info3)

# print(type(info3))

# info = list(map(lambda x, y : {x['name'] : y['age']}, many_user, many_user)) 

# print(info)
# inffo = list(map(lambda x : {'name' :x['name']})

# A = list(map(lambda x : x['name'], many_user))
# # print(A)
# B = list(map(lambda y : y['age'], many_user))
# info_tst = dict(zip(A,B))
# print(info_tst)

# print(map(rental_book, info_tst, info_tst))


# '''
# def create_user(name, age, address):
#     global user_info
#     user_info = {'name': name , 'age': age , 'address' : address}
#     # print('현재 가입 된 유저 수 :',number_of_people) # 가입유저수
#     print(f'{name}님 환영합니다!')
#     # print(user_info)
#     increase_user()
#     # print('현재 가입 된 유저 수 :',number_of_people)
#     # k.append(user_info) 
#     return user_info

# import book
# def rental_book(nombre, cantidad):
#     rnt_info = {}
#     rnt_info['이름'] = nombre
#     rnt_info['수량'] = cantidad
#     book.decrease_book(cantidad)
#     print(f'{nombre}님이 {cantidad}권의 책을 대여하였습니다.')

# rental_book('홍길동', 3)


---

# book.py
number_of_book = 100

def decrease_book(age):
    global number_of_book
    r = age // 10 
    print(f'남은 책의 수 : {r}')

# decrease_book(15) ?



# ws_3_3.py
import book
def rental_book(nombre, cantidad):
    rnt_info = {}
    rnt_info['이름'] = nombre
    rnt_info['수량'] = cantidad
    book.decrease_book(cantidad)
    print(f'{nombre}님이 {cantidad}권의 책을 대여하였습니다.')

rental_book('홍길동', 3)


# book.py 3-3 
number_of_book = 100

def decrease_book(x):
    global number_of_book
    r = number_of_book - x
    print(f'남은 책의 수 : {r}')

# decrease_book(15) ?


20230719
#ws_3_5.py

import book
number_of_people = 0
number_of_book = book.number_of_book

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    global user_info
    user_info = {'name': name , 'age': age , 'address' : address}
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info #이거 중요하겠지
    
#환영합니다! 포함됨

def rental_book(info):
    name = info['name']
    num = info['age'] // 10
    book.decrease_book(num)
    print(f'{name}님이 {num}권의 책을 대여하였습니다.')


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

many_user = list(map(create_user, name, age, address))
print(many_user)
info = list(map(lambda x : {'name' : x['name'], 'age' : x['age']}, many_user))
# print(type(info))
print(f'info = {info}')

list(map(create_user, name, age, address))
list(map(rental_book, info))
# 문제 해결!
```

```python
# 실습
# 리스트 만들기 0~9
# 방법 1
new_list = []
for i in range(0,10):
    if i % 2 == 1:
        new_list.append(i) #i를 range만큼 넣음.

# 2. list comprehension  (to make new list.)
new_list_2 = [i for i in range(10) if i % 2 == 1]
print(new_list_2)

nums = [1, 2, 3, 4, 5]
sqn = [num**2 for num in number]
print(sqn) # [1, 4, 9, 16, 25]

---
new_list_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
# 홀수 정수, 짝수 문자열, elif 안됨 if if if if if if if if  됨 

new_list3 = []
for i in range(0,10):
    if i % 2 == 1:
        new_list.append(i) #i를 range만큼 넣음.
    else: 
        new_list.append(str(i)) #위 new list3랑 같지만 가독성 더 좋음

----

# 리스트 만들기 3가지 방법의 비교 
# ej : 정수 1, 2, 3을 가지는 새로운 리스트 만들기

numbers = ['1', '2', '3']
# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

#2. map - 어쩔수없이 쓰게됨
new_nmbers_2 = list(map(int, numbers))
print(new_numbers_2) 

# 3. list comprehension - 굳이?
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)



# enumerate 인덱스 뽑아줌
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
4-5 꼭 제출은 아님 놀지만 마슈

누더기눠둬기 0720 실습중
```python
list_of_book = ['장화홍련전','가락국 신화','온달 설화','금오신화','이생규장전','만복자서포기','수성지','백호집','원생몽유록','홍길동전','장생전','도문대작','옥루몽','옥련몽']

rental_book = ['장생전','원생몽유록','이생규장전','장화홍련전','수성지','백호집','난중일기','홍길동전','만복자서포기']
# rental_book = ['유자소전'] # else 실험
# rental_book = ['난중일기'] # 없는 책 실험
# rental_book = []
# 1. 목록 / 대여중 두개 
# 2. rental 이 list에 있으면 
# 대여 불가.
# 모든 도서 있다면 대여 가능 상태
check = True
for i in rental_book: 
    if i in list_of_book: 
        print(f'{i} 은/는 보유하고 있지 않습니다.')
        break
        # 1. 안되는 것
        # 2. 
    else: #없으면
        check = False
        print(f'{i} 은/는 보유하고 있지 않습니다.')
        break 
    if check != False:  # 이부분이 안됨 잘
        print('모든 도서가 대여 가능한 상태입니다.')
```