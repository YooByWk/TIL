# Kruskal
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


# 모든 간선들 중 비용이 가장 적은걸 우선으로 고른다.
V, E = map(int, input().split())
edge = [] # 간선 정보
for _ in range(E):
    f, t, w = map(int, input().split()) # 이번에는 세 개 전부 넣어줘야 한다. + 출발지, 도착지
    edge.append([f, t, w])
# w 를 기준으로 정렬
edge.sort(key = lambda x : x[2]) # 두번째 기준으로 정렬

# 사이클을 어떻게 해결할 것인가. 
# 신장트리의 규칙임, 사이클 발생을 union find 로 해결

parents = [i for i in range(V)]

def find_set(x):
    if parents[x] ==x:
        return x
    
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x,y):
    x = find_set(x)
    y = find_set(y)
    
    if x == y : 
        # 사이클 발생
        return
    
    if x < y:
        parents[y] = x
    else: 
        parents[x] = y
    
# 현재 방문한 정점 수
cnt = 0
sum_weight = 0  
for f, t, w in edge:
    # 싸이클이 발생하지 않는다면
    if find_set(f) != find_set(t):
        cnt += 1 
        sum_weight += w
        union(f, t) # 이어준거임. 어제의 내용을 잘 생각하자. 경로 압축!
        # 다 연결됐다면 // MST 구성이 끝나면
        if cnt == V:
            break
print ("최소비용 = ",sum_weight)