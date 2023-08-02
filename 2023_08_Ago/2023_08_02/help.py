# 3
# 1 2 3
# 4 5 6
# 7 8 9
N  = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
print(arr) 

di = [0, 1, 0, -1] 
dj = [1, 0, -1, 0]

max_v = 0 # 모든 원소가 0 이상이라면. . . 
for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if 0 <= ni < n  and 0 <= nj < n: # 배열 안벗어나면
                 s += arr[ni][nj]
            # 여기까지 주변 원소를 포함
        if max_v < s:
            max_v = s

# 이게 대체 뭘까

for i in range(N):
    for j in range(N):
        s = arr[i][j]
        for p in range(1, m):
            for k in range(4):
                ni, nj = i+di[k]*p, j+dj[k]*p
                if 0 <= ni < n  and 0 <= nj < n: # 배열 안벗어나면
                    s += arr[ni][nj]
                # 여기까지 주변 원소를 포함
        if max_v < s:
            max_v = s