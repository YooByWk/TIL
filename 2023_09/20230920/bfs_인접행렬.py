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

def bfs(start):
    visited = [0] * 5
    
    # 먼저 방문한 것을 먼저 처리해야 한다
    queue = [start]
    visited[start] = 1
    
    while queue:
        # queue의 맨 앞 요소를 꺼낸다
        now = queue.pop(0)
        print(now, end=' ')
        
        # 인접한 노드들을 queue에 추가
        for next in range(5):
            # 연결이 안되어 있다면 continue
            if graph[now][next] == 0:
                continue
            # 조건이 만족 한다면 : 으로 하면 코드가 복잡해질 수 있다.
            # 그래서 할 수 없는것 기반으로 (pass조건) 으로 코딩함
            # 가지치기 하듯 
            
            # 방문한 지점이라면 queue에 추가하지 않는다.
            if visited[next]:
                continue
            
            # bfs이므로 여기서 방문 체크를 해줘도 상관 없다.
            queue.append(next)
            visited[next] = 1
print("bfs :", end=' ')
bfs(0)