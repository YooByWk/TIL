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