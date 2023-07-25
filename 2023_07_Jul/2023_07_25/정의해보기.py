def my_len(lst): # 길이 구하기
    cnt = 0
    for i in lst:
        cnt += 1
    return cnt

def my_sum(lst): # 리스트 전체 더함
    res = 0
    for i in lst:
        res += i
    return res

def my_min(lst): # 최소
    ahora_min = lst[0]
    ahora_min_index = 0 #어차피 들어가서 초기화 할 것.
    for idx, value in enumerate(lst): #enumerate 자체가 object 임.
        if ahora_min > value:
            ahora_min = value
            ahora_min_index = idx
    return ahora_min, ahora_min_index

def my_max(lst): # 최대
    ahora_max = lst[0]
    ahora_max_index = 0
    for idx, value in enumerate(lst):
        if ahora_max < value:
            ahora_max = value
            ahora_max_index = idx
    return ahora_max, ahora_max_index


# 만약 enumerate 못쓰면 ?
def my_max2(lst): # 최대
    ahora_max = lst[0]
    ahora_max_index = 0
    for idx in range(my_len(lst)):
        value = lst[idx]
        if ahora_max < value:
            ahora_max = value
            ahora_max_index = idx
    return ahora_max, ahora_max_index


ns = [10, 2, 5, 7, 12]
print(my_len(ns))
print(my_sum(ns))
print(my_min(ns))
print(my_max(ns))
print(my_max2(ns))