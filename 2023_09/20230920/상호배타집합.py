# 0 ~ 9
# make set - 집합을 만드는 과정
# 각 요소가 가리키는 값이 부모
parent = [i for i in range(10)] # 말이 집합이지 그냥 이리 만들어도 만든거임



# find-set
# 부모 찾기
def find_set(x):
    
    # 자기 자신이라면
    if parent[x]  == x :
        return x
    
    # 한번 더 올라가서 찾아오세요.
    # return find_set(parent[x])
    
    # 경로 압축
    parent[x] = find_set(parent[x])
    return parent[x]

    
    
    
# union-set 
# 같은 집합으로 묶기

def union(x,y):
    # 1. 이미 같은 집합인지 체크
    x = find_set(x) 
    y = find_set(y)
    
    # 대표자가 같다면, 같은 집합이다.
    if x == y:
        print("Union 과정 중 싸이클 발생 ")
        return 
    
    # 2. 다른 집합이라면, 하나의 대표자를 수정해줘야 함
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    # 3. 
    
    # 4. 
    
    
# 그룹!
union(0,1)
union(2,3)
union(1,3)
# 0 - 1 -3 - 2  로 연결된 느낌


# 이미 같은 집합의 원소를 한 번 더 포함 >> 
# 싸이클 발생
union(0,2)

# 대표자검색
print(find_set(0))
print(find_set(1))

# 같은 그룹인지 판별
target_x = 0
target_y = 2

if find_set(target_x) == find_set(target_y):
    print(f' {target_x}와 {target_y}는 같은 집합에 속해 있습니다.')
else:
    print(f' {target_x}와 {target_y}는 같은 집합에 속해 있지않습니다.')
    