my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)

# my_set.remove(10) #KeyError: 10
my_set.discard(10) #''
print(my_set.discard(10)) # None

element = my_set.pop()
print(element)
print(my_set)

my_dict = {'name' : 'Maria',
'age': 20
}
print(my_dict['name'])
print(my_dict.get('name'))

# 찾고자 하는 키가 없을 때 
# print(my_dict['age']) #KeyError 여기서 중단됨
# get은 찾고자 하는 키가 없을 때 원하는 반환값을 얻을 수 있다.
print(my_dict.get('age')) # None 중단 안됨.
print(my_dict.get('name'), 'Unknown') #Unknown
print(my_dict.keys()) # dict_keys(['name', 'age'])
for key in my_dict.keys():
    print(key)

print(my_dict.pop('country', 'Country 없음'))

# .setdefault(key[,default])
print(my_dict.setdefault('country', 'Argentina'))
print(my_dict.setdefault('age', 50)) # age가 있으니까 50 안됨 #출력 20
# 반환 > 없다면 > 딕셔너리에 키 추가, default(예시의 경우 arg 반환)
