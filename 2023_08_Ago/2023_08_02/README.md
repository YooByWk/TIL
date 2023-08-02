# 2023_ 08_02

# 배열

## 2차원 배열
- 1차원 List를 묶어놓은 리스트
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수) 필요
- 데이터 초기화를 통해 변수선언과 초기화가 가능하다.<p>
| 행 ㅡ열

```py
1 2 3
4 5 6
7 8 9
n = int(inpuit())
arr [list(Amap(int, input().split())) for _ in range(N)]

123
456
789
arr = [list(map(int, input()))for _ in range(N)]
```
### 2차원 배열의 접근
- 배열순회
    n x m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
```py
    # 행 우선조회
   # i 행 좌표
   # j 열 좌표
   for i in range(n):
    for j in range(m):
     f(Array[i][j]) #필요한 연산 수행
# 열 우선조회 
    for j in range(m):
        for i in range(n):
            f(Array[i][j])

# 지그재그 순회
    for i in range(n):
        for j in range(m):
            f(Array[i][j + (m - 1 - 2 * j)*(i % 2)])
            # j 증가하고... m은 고정이고 ...  i%2는 짝수에선 앞이 0 되게...
            #모르겠습니다
```
## 델타를 이용한 2차배열 탐색
- 진짜 모르겠어요 
- 네? 뭐라고요?
- 2차원 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
-  i j 기준
```py
# NxN 배열
di[] 
dj[]
아니 그냥 일단 좌표 처럼 그려봅시다
```
## 전치행렬
```py
i : 행 좌표 len(arr)
j : 열 좌표 len(arr[0])
arr = [[1,2 3],[4,5,6,],[7,8,9]] # 3* 3 행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j],a[j][i] = arr[j][i], arr[i][j]
```           

---
복습 1

아니네...