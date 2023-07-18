# 스페인어 배웠는데 어쩌다 코딩.
## 2023.07.13.JUE/목

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