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