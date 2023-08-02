N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total1 = 0
for i in range(N):
    total += arr[i][i] #대각선 이동

#  오른쪽에서 왼쪽 대각선이동
total2 += arr[i][(n-1)-i]
