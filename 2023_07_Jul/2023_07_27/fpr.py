#  조건문과 함께 len, sum, min, max 함수 정의하기
lst = [2, 5, 6, 7, 10]
def get_len(numbers):
    count = 0
    for i in numbers:
        count += 1
    return count

def get_sum(numbers):
    k = 0
    for i in numbers:
        k += i
    return k

print(get_sum(lst))




# chr, ord 활용 #ord
print(chr(65)) # A
print(ord('a')) # 97
print(ord('0')) # 48
print(ord('가')) #44032

# 이차원 배열 
a = [
[1, 2, 3],
[3, 4, 5]
]

# 이차원 배열의 입력
r = []
for _ in range(1):
    i = list(map(int, input().split()))
    r.append(i)
print(r)

r = [list(map(int, input().split()))for _ in range(1)]
print(r)

s = [[1] * 3 ]* 3 # s = [1, 1, 1]
print(s)
s[0][1] = 100 # 얕복당함 ㄴㄴ;;
print(s)



# list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
squares = [[x**2 for x in row] for row in matrix]
print(squares)

