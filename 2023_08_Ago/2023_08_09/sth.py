N =5 
arr = [[] for _ in range(N)]
arr[0] = [1]
print(arr)
for r in range(1, N):
    arr[r].append(1)
    for c in range(r-1):
        arr[r].append(arr[r-1][c] +arr[r-1][c+1])
    arr[r].append(1)
for r in range(N):
    print(*arr[r])