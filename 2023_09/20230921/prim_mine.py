# Prim을 구현해보자
'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
# 우선순위 큐 구현해야 함
import heapq # 파이썬은 신이야.

def prim(start): # 정점 기준으로 가중치가 적은 것
    heap = []
#     heapq.heappush(heap, 3)
#     heapq.heappush(heap, 1)
#     heapq.heappush(heap, 2)
#     # 내림차순은 음수로 넣고, 출력에 -를 넣어주면 됨
#     # 튜플은 맨 앞 기준으로 정렬한다.
#     # 그렇다면 가중치 기준으로 정렬시키려면 앞에 넣어야겠지?
#     print(heapq.heappop(heap))

    # MST에 포함되었는지 여부 확인해야 함 
    MST = [0] * V
    # 가중치, 정점 정보
    
    heapq.heappush(heap, (0, start))     # 출발점에서 출발점 가는 것이라 0임 , 0 자리가 가중치 자리

    # 누적합 저장
    sum_weight = 0 
    while heap:
        # 가장 적은 가중치를 가진 정점을 꺼낸다.
        weight, v =heapq.heappop(heap) 

        # 이미 방문한 노드라면 pass
        if MST[v]: 
            continue

        # 방문 체크
        MST[v] = 1
        
        # 누적합
        sum_weight += weight
        
        # 갈 수 있는 노드들을 체크
        for next in range(V):
            # 갈 수 없거나 이미 방문했다면 pass
            if graph[v][next] == 0 or MST[next]:
                continue
            
            # 우선순위가 높은걸 뽑음
            heapq.heappush(heap, (graph[v][next], next))
            
    return sum_weight
    
V, E = map(int, input().split())
# 인접행렬
graph = [[0] *V for _ in range(V)]
for _ in range(E): # 간선의 수 반복
    f, t, w = map(int, input().split())
    graph[f][t] = w
    # 무방향 그래프 // 양방향
    graph[t][f] = w
    # 따라서 양방향으로 만들어준다.
    
print("최소비용 = ", prim(0))
# 디버깅 툴이 중요합니다.