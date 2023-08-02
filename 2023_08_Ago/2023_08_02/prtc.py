#연.문 1
N = 5
nums = [[0]* 5 for _ in range(N)]

# 절댓값
def my_abs(value):
    return value if value> 0 else -value
    #삼항연산자





# M = range(len(nums))
# l = range(len(nums))
# value = 1
# for r in range(N):
#     for c in range(N):
#         nums[r][c] = value
#         value += 1
#         print(nums[r][c], end = ' ')
dr = [0, -1, 0, 1]
dc = [-1, 0, 1 , 0]
nums[2][2] = 1
for r in range(N):
    for c in range(N):
        for d in range(4):
            nR = r + dr[d]
            nC = c + dc[d]
            if 0<=nR<N and 0<= nC < N:
                print(my_abs(nums[nR][nC] - nums[r][c]))
                print(nR, nC, nums[nR][nC])