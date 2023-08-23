# 2023_08_23

## SW 문제 해결

### 문제해결과정

1. 문제를 읽고 이해한다
2. 문제를 익숙한 용어로 재정의한다
3. 어떻게 해결할지 계획을 세운다
4. 계획을 검증한다
5. 프로그램으로 구현한다
6. 어떻게 풀었는지 돌아보고 개선할 방법이 있는지 찾아본다

### 복잡도 분석
####  O(Big-Oh)
O- 표기는 복잡도의 **점근적 상한**을 나타낸다<p>
복잡도가 f(n) = 2(^n2)-7n+4 라면, f(n)의 O-표기는 O(n^2)<p>
- 먼저 f(n)의 단순화된 표현은 n^2<p>
단순화된 함수 (n^2)에 임의의 상수 c를 곱한 c(n^2)이 n이 증함에 따라 f(n)의 상한이 된다 (c>0)<p>
**단순히 실행히간이 n^2에 비례하는 알고리즘이라고 말함**

#### Ω
**최소한 이만큼의 시간은 걸린다.**
(잘해봤자 이만큼은 걸린다.)

#### Θ
O- 표기와 Ω- 표기가 같은 경우에 사용

자주 사용하는 O-표기
[O](B.png)
---
효율적 알고리즘 필요한 이유:
10억 개의 숫자를 정렬: 
- O(n^2) 알고리즘은 300년 걸림
- O(nlogn) 알고리즘은 5분

```py
import sys
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", 'w')

text = input()
print(text)
# 디버그용으로 잘 써보세요 
```
### 비트연산
(사실 다른것도 있었지만)
```
& 연산자 : 비트단위로 AND 연산 ej) num1 & num 2
| 연산자 : 비트단위로 OR 연산 ej) num1 | num2
^ 연산자 : 비트단위로 XOR 연산 (같으면 0 다르면1) ej) num1 ^ num2
~ 연산자 : 단항 연산자로서 피연산자의 모든 비트를 반전시킨다 ej) ~num
<< 연산자 : 피연산자의 비트 열을 왼쪽으로 이동
>> 연산자 : 피연산자의 비트 열을 오른쪽으로 이동
i & (1<<j) : i의 j번째 비트가 1인지 확인한다.
```
```py
def decToBin(dec):
   # 비트연산을 사용해보자?
   res =''
   for cnt in range(4):
       t = dec & (1<<cnt)
       if t != 0:
           res = '1' + res
       else:
           res = '0' + res

   return res

print(bin(7))
print(decToBin(7))

def BinTpDec(Bi):
    res = 0
    for c in Bi:
        res = res * 2 + int(c)
    return res
print(BinTpDec('1100'))

def BinTpDec2(Bi):
    res = 0
    for c in Bi:
        # res = res * 2 + int(c)
        res = res << 1 | int(c)  # res라는 변수에 이진법으로 값을 만드는 연산
        # 입력은 문자열로 받아왔지만, 계산은 이진수로 진행중
    return res
print(BinTpDec2('1100'))

def hexTodec(hx): # 이름 잘못됨 hx to dec 임
    res = 0
    for c in hx:
    # 10A 
        if c.isalpha():
            t = ord(c) - ord('A') + 10
            res = res * 16 + t
        else:
            res = res * 16  +  int(c)
    return res

print(hexTodec('10A'))

def hxtobin(hx):
    res = ''
    return decTobin(hexTodec(hx))

    

```