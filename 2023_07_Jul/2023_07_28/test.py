# value 5, cnt 3
#재귀함수로  해보기

def sq(num1, cnt): # 재귀로 n제곱 시키기.
    if cnt == 0:
        return 1
    return num1 * sq(num1, cnt-1)

def rec(num):
    if num == 0:
        return 0
    return num + rec(num-1)

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(sq(9,3)) # 729

print(rec(10)) #N 까지 더하는 함수 만들기 55
print(fact(4)) # 24
print('----------------------------------------')
# 리스트 합 재귀함수

lst = [2, 3, 6, 9, 10]

def sumlst(n):
    if n == 0 :
        return lst[0]
    return sumlst(n-1) +lst[n]

print(sumlst(4)) #4까지 더하십쇼. #30

print('----------------------------------------')



def make(a, n):
    if n == 1:
        return a
    return a + make(a, n-1)

print(make('a', 5)) #aaaaa
print('----------------------------------------')


def make1(ch, cnt):
    if cnt == 0 :
        return ch
    return make1(ch, cnt-1) + ch

def make2(cnt):
    if cnt == 0:
        return lst2[0]
    return make2(cnt-1) + lst2[cnt]

lst2 = ['H', 'e', 'l', 'l', 'o']
print(make2(2)) # Hel

print(list(str(123))) # 123을 ['1', '2', '3']으로 바꿈
print('----------------------------------------')
my_dict = {
    '김' : 80,
    '이' : 70,
    '박' : 60
}

def getScore(d):
    S = 0
    for i in my_dict:
        S += my_dict[i]
    return S
print(getScore(my_dict)) # 210
print('-----------------------------------')

def overN(d):
    masqueD = 0
    anadido = 0
    for i in my_dict:
        if my_dict[i] >= d:
            masqueD += 1
            anadido += my_dict[i]
    return print(f'{d} 이상은 {masqueD}명,{d} 이상의 합은 {anadido}, {d} 이상 평균은 {anadido / masqueD}')

overN(80) # 1 이상은 3명 입니다.

