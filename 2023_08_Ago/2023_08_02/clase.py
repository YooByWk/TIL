n = 2  #행 
m = 4  #열
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
for i in range(n):
    for j in range(m):
        print(arr[i][j]) #0 1 2 3 4 5 6 7

for j in range(m):
    for i in range(n):
        print(arr[i][j]) #0 4 1 5 2 6 3 7

# 지그재그 찾아보쇼..
for i in range(n):
    for j in range(m):
        if i % 2: # 홀수 행
            pass

arr2 = [[0,1], [4,5,6,7]]
for i in range(n):
    for j in range(len(arr2[i])):
        print(arr2[i][j])

arr3 = [[0]* m for _ in range(m)]
print(arr3) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr3_2 = [[0] * m ] * n # 얕은복사의 피해자가 될수있읍니다. #하나 만들고 참조 여러개.
arr3[0][0] = 1  # [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr3_2 [0][0] =1  # [[1, 0, 0, 0], [1, 0, 0, 0]]
print(arr3)
print(arr3_2)

max_v = 0
for i in range(n):
    row_total = 0 
    for j in range(m):
        row_total += arr[i][j]
    if max_v < row_total:
        max_v = row_total