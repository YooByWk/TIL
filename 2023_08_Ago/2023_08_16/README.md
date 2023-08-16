# 2023_08_16

발가락 병원진료

## 백트래킹!
**정답일 가능성**이 없다면 되돌아가서 정답 가능성이 있을 곳 탐색

DFS는 **완전탐색**임 <- 백트래킹이랑 다르다
- DFS에 백트래킹 물타기 가능

백트래킹은 불필요한 경로를 조기 차단.
N!의 DFS, 이런거에 깊이우선 탐색 == 처리불가능
백트래킹 적용하면 일반적으로 경우의 수 줄어드나, 최악의 경우에는 여전히 지수함수시간.

### 다음과 같은 절차
1. 상태 공간 트리 깊이 우선 검색
2. 노드가 유망한지 점검
3. 유망하지 않다면 부모 노드로 돌아간다.

### 일반 알고리즘
n-Queen  자주 나올거임.

### 부분집합
- 재귀함수 모양으로...
powerset을 구하는 백트래킹 알고리즘
-> 알면 좋은데 복잡함 ㅋㅋ 
---
```py
arr = list(range(1, 11))  # 부분 집합
selected = [False] * (len(arr) + 1)  # 해당 숫자가 선택됐는지 안됐는지 확인 용도

def powerset(idx):   # idx 는 현재 숫자, 위치
    # 종료 조건을 만들자!!
    if idx == len(arr)+1:   # +1 을 붙인 이유 => selected 크기가 len(arr) + 1 이기 때문
        # 종료 전에 현재 선택된 부분집합을 출력
        print(selected)
        for i in range(len(arr) + 1):
            if selected[i] == True:
                print(i, end=' ')
        print()         # 줄바꿈 용도
        return          # 함수 종료 (break 를 사용하듯이 함수를 종료하기 위한 목적)

    # 현 위치를 선택했을 경우
    selected[idx] = True
    powerset(idx+1)   # 다음 자리 선택

    # 현 위치를 선택하지 않았을 경우
    selected[idx] = False
    powerset(idx+1)   # 다음 자리 선택

powerset(1)      # 시작이 1인 이유 : 0번 index를 selected에서 사용하지 않기 때문
# 부분집합
```


```py
arr = [1, 2, 3]  # list(range(1, 11))
N = len(arr)

def permutation(idx):
    # 종료 조건
    if idx == N:
        print(arr)
        return
    else:
        for swap_idx in range(idx, N):  # 바꿀 위치를 반복
            arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
            permutation(idx + 1)  # 다음 자리 확인
            arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]  # 원상 복구 (처음 모양에서 자리를 바꾸는게 아니라 바뀌어진 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)


permutation(0)
# 순열
```