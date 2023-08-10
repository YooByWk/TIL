def dfs(n, V, adj_m):
    stack = []              # stack 생성
    visited = [0] * (V+1)   # visited 생성
    visited[n] = 1          # 시작점 방문 표시
    print(n)                # do[n] 
    while True:
        # 현재 정점 n에 인접하고 미방문 w 찾기.
        for w in range(1, V):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v)
                n = w # 새로운 위치
                print(n)
                visited[n] = 1
                break #  for w, n에 인접인 w, c 찾은 경우
                # push(v)
                # do (W)
                # w 방문 표시
        else: #뒷걸음질 하십쇼.
            if stack: 
             # 스택에 지나온 정점이 남아 있으면,
                n = stack.pop() # pop() 해서 다시 다른 갈림길로 이동
             # 다른 w를 찾을 n을 준비하기. 스택이 비어있으면 끝난거임
            else:
                break
             
             





V, E  = map(int, input().split()) #1번부터 V번 정점, E개의 
arr = list(map(int, input().split()))
adj_m = [[0]*(v+1) for _ in range(v+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
    print(arr)