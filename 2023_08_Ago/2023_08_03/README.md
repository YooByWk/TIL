# 2023_08_03

## 부분집합
```py
def print_subset(bit, arr, n):
    total = 0
    for i in range(n):
        if bit[i]:
            print(arr[i], end= '  ')
            total += arr[i]
    print(bit, total)
arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print_subset(bit, arr , 4)
# 이러고싶지는 않잖아요
arr = [1,2,3]
n = len(arr)
for i in range(1<<n): # 1<< 부분집합의 수
    for j in range(n): # 원소의 수만큼 비트 비교
        if i & ( 1 << j): #  i의 j번 비트가 1인 경우
            print(arr[j], end = ", ") # j 출력
    print()
print()
```

### 비트연산자

&  : 비트 단위로 AND 연산을 한다
|  : 비트 단위로 OR 연산을 한다.
<< : 피연산자의 비트 열을 왼쪽으로 이동시킨다.
>> : 피연산자의 비트 열을 오른쪽으로 이동시킨다. 


<< 연산자 
- 1 <<  n : (2^n)원소가 n개일 경우의 모든 부분집합의 수를 의미
& 연산자
 i & 1<<j : i의 j번쨰 비트가 1인지 아닌지 검사한다.

 ## 이진검색
 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
 -  목적 키를 찾을때까지 이진검색 순환적 반복 수행, 빠름
 -  자료가 정렬된 상태여야 함
  ### 과정
  1. 중앙 원소 고름 
  2. 목표 값 비교
  3. 목표값이 크면 오른쪽, 작으면 왼쪽
  4. 1~3 반복
### 구현 
- 검색 범위 시작점, 종료점
- 자료가 삽입되거나, 삭제가 발생할 때 정렬을 유지해야 함
```py
def binarySearch(a, N, key):
    start = 0 
    end = N-1
    while start <= end: # 탐색 원소가 하나 이상
        middle = (start + end) //2
        if a[middle] == key:
            return true # 탐색 성공
        elif a[middle] > key:
            end = middle - 1
        else:
        start = middle + 1
    return false # 탐색 실패
```

## 인덱스
### 선택정렬
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
- 최소값 찾기
- 맨 앞 위치 값과 교환
- 나머지 대상 반복 o(n2)
``` py
def slectionSort(a, N):
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
```
*정렬 다 연습하기*
## 셀력션 알고리즘
- 정렬 후 원하는 순서 원소 가져오기
```py
def select(arr, k):
    for i in rnage(0,k):
        minIndex= i
        for j in range(i+1, len(arr)):
            minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    retrun arr[k-1]
```