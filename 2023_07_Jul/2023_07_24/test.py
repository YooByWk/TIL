print('banana'.find('z')) # -1

url = 'https://wikidocs.net'
print(url.rstrip('.net')) # 'https://wikidocs'

num = [1, 2, 3]
nums = [4, 5, 6]
num.append(nums) #[1, 2, 3, [4, 5, 6]]
num.extend(nums) # [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3]
# 할당
list1 = numbers # [100, 2, 3]


#슬라이싱
list2 = numbers[:] #[1, 2, 3]

numbers[0] = 100
#얕복 깊복 으악

chars = 'ssafy'
Nc = chars.capitalize()
print(Nc)

# T = ''.join([1, 2]) #TypeError: sequence item 0: expected str instance, int found
# print(T) 
T= ''.join(['1', '2']) #'' Adios 하고 12로.
print(T)
print(type(T)) # str 

numbers = [1, 2, 5, 7, 9]
print(numbers[1:4]) # [2, 5, 7]
print(numbers[1:10]) # [2, 5, 7, 9] 
print(numbers[1:10:2]) # [2, 7]
print(numbers[1:10:-1]) # []
print(numbers[4:1:-1]) # [9, 7, 5]
print(numbers[-1 : -4 : -1]) # [9, 7, 5]

#print(numbers[10]) 이건 안됨

a = 'adasd'
k = ''.join(reversed(a)) # 하나의 스트링으로 바꿔준다.
print(k)

def reverse_string(X):
    # 
    K = list(X)
    K.reverse()
    return ''.join(K)
    #
    new_string reserved(X)
    return ''.join(X)
    #
    new_str = ''
    for c in X:
        K = c + X
    return K
    #
    return X[::-1]


result = reverse_string("Hello, World!")
print(result)

#ws 2 

def remove_dup(ori):
    new_lst = []
    for n in ori:
        if n not in new_lst:
            new_lst.append(n)
    return new_lst

result = remove_dup([1, 2, 2, 3, 4, 5, 4])

#ws3
def sort_tuple(original):
    new_tuple = tuple(sorted(original))

    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))

# ws 5
new_lst = []
while numbers: 
    n = numbers.pop(0)
    if n % 2 == 0:
        new_lst.extend([n])