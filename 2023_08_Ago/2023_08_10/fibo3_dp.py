def fibo(n):
    global cnt 
    cnt += 1
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
cnt = 0
print(fibo(100), cnt)

dp = [0] * (100+1)
dp[0] = 0
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1] + dp[i-2]
# 대충 몇번하건간에 여기서 쓱 싹 하면 테이블 내부에서 한번에 돌아감
# 걍 불러오기가 됨