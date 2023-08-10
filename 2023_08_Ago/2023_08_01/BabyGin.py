#  경우의 수 . . . 
# [6, 6, 7, 6, 7, 6]
# [0, 1, 2, 3, 4, 5]  idx를 기준으로 모든 경우의 수를 다 해보자

# 순열

Alist = [1,2,3,4 ]
n = len(Alist)
cnt = 0
for i0 in range(n):
    for i1 in range(n):
        if i0 != i1:
            for i2 in range(n):
                if i2 != i0 and i2 != i1:
                    for i3 in range(n):
                        if i3 != i2 and i3 !=  i1 and i3 != i0:
                            print(i0,i1,i2,i3)
                            cnt += 1
                            print(cnt)
                            print(Alist[i0],Alist[i1], Alist[i2],Alist[i3])
#웩
#Greedy가 항상 통하지는 않는다. . .
# Baby-gin

