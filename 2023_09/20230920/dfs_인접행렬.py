# 인접 행렬
# 장점 : 구현이 쉬움
# 단점 : 메모리 낭비
#       0도 표시하기 때문.
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0]
]
if graph[0][1] == 1:
    # 갈 수 있음
    pass


# DFS

## DFS stack 버전

def dfs_stack(start):
    visited = []
    stack = [start]
    
    # 스택이 비어있을때 까지
    while stack:
        now = stack.pop()
        # 이미 방문한 지역을 패스
        if now in visited:
            continue
        
        # 아니라면 방문 표시
        visited.append(now)
        
        # 갈 수 있는 곳들을 stack에 추가
        #for next in range(5):

        # 작은 번호부터 조회한다면?? 
        for next in range(4,-1,-1):
        
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            # 조건이 만족 한다면 : 으로 하면 코드가 복잡해질 수 있다.
            # 그래서 할 수 없는것 기반으로 (pass조건) 으로 코딩함
            # 가지치기 하듯 
            
            # 방문한 지점이라면 stack에 추가하지 않는다.
            if next in visited:
                continue
            
            stack.append(next)

    # 출력을 위한 반환
    return visited
print("dfs_stack", end = ' ')
print(*dfs_stack(0))

# dfs_stack 0 3 4 1 2
# 작은 수부터
# dfs_stack 0 1 2 3 4


## DFS 재귀
visited = [0]*5
path = []

# in 으로 하는 것은 O(n)
# visited[3] = O(1)
# Map 크기(길이)를 알고 있을 때 빠르게 할 수 있다.
# append 보다 빠름
# 따로 방문했다는 의미의 path
def dfs_re(now):
    visited[now] = 1 # 현재 지점 방문 표시
    print(now, end=' ')
    
    # 인접한 노드들을 방문한다.
    for next in range(5):
        if graph[now][next] == 0:
            continue
        
        if visited[next]:
            continue

        dfs_re(next)
        
print('dfs 재귀', end = " ")     
   
print(dfs_re(0))
        
# 함수가 어떻게 쌓이는지 알아야 제대로 할 수 있다.        
        
        