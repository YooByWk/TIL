# 2023_08_01

## 카운팅 정렬
- n이 비교적 작을때
- O(n+k), 비교환 방식
[0, 4, ,1, 3, 1, 2, 4, 1]을 카운팅
=> [1, 3, 1, 1, 2] 이렇게 카운팅
### 1단계
1. Data에서 각 항목들의 발생을 셈함
2. 정수 학목들로 인덱스되는 counts에 저장 
3. 누적? 합? 암튼 ? 더함 ? 왼쪽 더?함// 왼쪽 원소 없으면 컷
 ```py
for 1 4
cnts += cnts i-1
```
4.
5. counts[1] 을 감소시키고 Temp에 1을 삽입한다. (temp는 data와 크기가 같음)
5. 설명...  누적합으로 위치... data[j] // cnts(data[j]) -= 1 
6. counts[2] 감소. temp에 2 삽입
counts != DATA
7. counts[0] 감소, temp 0 삽입
8. (오른쪽부터 왼쪽으로 가는건가...?)
9. 인덱스 엉망 안됨.
10. 리스트 만들어서 메모리 사용은 늘어나긴 하는데, 계산이 편해지긴 함
```py
def Counting_sort(A,B, k):
    A = [] # 입력배열
    B = [] # 정렬배열
    C = [] # 카운트배열
    
    C = [0] * (k+1)
    for i in range (0, len(A)):
        C[A[i]] += 1
    for i in range (1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[c[a[i]]] = A[i]



```

### Baby-gin Game? 
0 ~ 9 카드 // 6장 선택 
연속 3 숫자, run  
3장 카드 동일 번호 triplet  
6장 카드가 run + triplet = baby-gin

6자리 숫자 입력 , Baby-gin 찾으십쇼.

```py
num = 456789 # baby-gin 검사 
c= [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트
for i in range(6):
    c[num % 10] += 1
    num 

ex>
i = 0 
tri = run =  0
while i < 10:
    if c[i] >= 3 : #triplete 조사 후 삭제!
        c[i] -= 3
        tri += 1
        continue; # 이곳의 핵심
    if c[i] >= and c[i+1] >= and c[i+2] >= 1 : run 조사후 삭제 
        c[i] -= 1
        c[i+1] -=1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2 : print('baby-gin')
else: print('lose')
```


## 완전검색 Exaustive Search.

or Brute-force, generate-and-test 기법

모든 경우의 수 테스트, 최종 해법 도출

가능한 경우의 수가 상대적으로 작을 때 유용하다.
  
수행속도 보다는 해답을 찾아냅시다.  
자격 검정평가 등에서 주어진 문제를 풀 때 우선 완전 검색으로 접근하여 해답을 도출한 후 성능 개선을 위해 다른 알고리즘을 사용하고 해답을 확인하는 것이 바람직하다. 

### 순열을 만들어 봅시다.  Permutation
 
서로 다른 것들 중 몇개를 뽑아서 한줄로 나열하는것  
서로다른 n개 중 r을 택하는 순열은 nPr
```py
#{1,2,3} 순열
for i1 in range(1, 4):
    for i2 in range(1,4):
        if i2 != i1 : 
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1,i2,i3)

```
## Greedy 알고리즘
최적해를 구하는데 사용되는 근시안적인 기법  
여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 최종적 해답에 도달

- 각 선택의 시점에서 이루어지는 결정은 지역적으로는 최적이나 그 선택들이 수집된 것이 최적이라는 보장은 없다.
-  일반적으로 머릿속에 떠오르는 생각을 검증없이 하면 greedy에...

-> 거스름돈 줄이기. 
