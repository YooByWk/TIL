nums = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]]
print(len(nums)) # 4
for r in range(len(nums)):
    print(r, nums[r])
    for c in range(len(nums[0])): # r로 바뀌는것도 가능함
        print(nums[r][c], end = ' ')
    print()
print('============================')

for n in nums:
    for item in n:
        print(item, end = ' ')  #  행 우선에서는 이렇게 간단하게 쓰는 것도 가능하다. 
    print() 
print( '========열우선==========')

for c in range(len(nums[0])):
    
    for r in range(len(nums)):
        print(nums[r][c], end = " ")  #행렬처럼 출력하려고
    print()                            #행렬처럼 출력하려고...

print( '=========행 별로 합 구하고 옆에 써주기.===========')

for n in nums:
    s = 0
    for item in n:
        s += item
        print(item, end = ' ')
    # print()
    print(s)

print ( ' =-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# 열 기준 합 구하기 
curmax = 0
for c in range(len(nums[0])):
    s = 0
    for r in range(len(nums)):
        s += nums[r][c]
        print(nums[r][c], end = ' ')
        if curmax < s:
            curmax = s
    print()
    print(s)
print(curmax)
print ( ' ===============================') 
#행 열 제일 큰 값 // 몰루


print(' =-=-=-=-=-==-=')
sumV = 0
sumV2 = 0
for i in range(len(nums[0])):
    sumV += nums[i][len(nums[0])-1-i] # 반대 대각선
    sumV2 += nums[i][i]
print(sumV2)
print(sumV)
