#  2023_07_25

## 세트 메서드 

```python

s.add(x) # x추가, 있으면 변화 x

s.clear() # 모든 항목 제거
# set() 빈 세트 {} 해버리면 dict니까

s.remove(x) 
#항목 제거
#없으면 오류
s.pop
#세트에서 임의의 요소를 제거하고 반환
#사실 해시테이블상 제일 앞 값을 뽑기는 하지만, 첫번째 무언가가 빠지는 것은 아님
#따라서 임의의 수임.

s.discard(x)
# s에서 x 제거 remove와 다르게 에러 없음
s.update(iterable)
#넣는건가.


```
### 세트의 집합 메서드
```python

set1.difference(set1)
# = set1 - set2 
set1.intersection(set2)
# = set1 & set2
set1.issubset(set2)
# = set1 <= set2
set1.issuperset(set2)
# = set1 >= set2
set1.union(set2)
# = set1 | set2

```
해시 테이블(Hash Table)
- 키 값 쌍 연결 저장방식 // 키를 함수(hash값으로 변환) -> 이 값을 인덱스로 사용하여 저장하거나 검색
- 세트 내의 각 요소는 해시 함수를 통해 해시 값으로 변환되고, 이 해시 값을 기반으로 해시 테이블에 저장됨.
- 마찬가지로 딕셔너리의 키는 고유해야 하므로, 키를 해시 함수를 통해 해시 값으로 변환하여 해시 테이블에 저장
- 따라서 세트와 딕셔너리의 키는 매우 빠른 탐색 속도를 제공하며, 중복값을 허용하지 않음.
- md파일 참조

해시(Hash)
- 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환하는 것
- 일종의 '지문' 같은 역할
- 정수는 값 자체가 해시가 됨
- 문자는 엉/망/해/시 (이유 : 문자열은 가변적 길이를 가짐, 문자열에 포함된 각 문자들의 유니코드 코드 포인트 등을 기반으로 해시 값을 계산한다.)  
    - 이로 인해 문자열의 내용에 따라 다르게 계산됨.
- 해시 가능성은 객체를 "딕셔너리의 키"나 "세트의 요소"로 사용할 수 있게 한다.
    -  이 자료 구조들은 내부적으로 해시 값을 사용하기 때문
**우리는 그냥 잘 쓰면 됩니다.**
- 인풋 폭주하면 해시 충돌도 일어나기도 함.[해시충돌/위키백과](https://ko.wikipedia.org/wiki/%ED%95%B4%EC%8B%9C_%EC%B6%A9%EB%8F%8C)



#### set의  pop 메서드 예시

- 임의의 요소를 제거하고 반환
-  실행할 때마다 다른 요소를 얻는 의미의 무작위가 아니라 "임의"에서 "무작위"
-  By "arbitrary" the docs don't mean "random"

Pero,
문자열은 실행할때마다 반환값이 다르다.
print(has(1)) 정수는 값 자체가 해시가 됨
문자는 엉/망/해/시

## 딕셔너리 dictionary  
> 고유한 항목들의 정렬되지 않은 컬렉션

### 딕셔너리의 메서드


```python
.get(key, [,default])

my_dict = {'name' : 'Maria',
'age': 20
}
print(my_dict['name'])
print(my_dict.get('name'))

# 찾고자 하는 키가 없을 때 
# print(my_dict['age']) #KeyError 여기서 중단됨
# get은 찾고자 하는 키가 없을 때 원하는 반환값을 얻을 수 있다.
print(my_dict.get('age')) # None 중단 안됨.
print(my_dict.get('age'), 'Unknown') #Unknown
////////////////////////////////
.keys()
# 딕셔너리 키를 모은 객체를 반환
for key in my_dict.keys():
    print(key) # 이런게 가능하다.

.values()
# 딕셔너리 값을 모은 객체를 반환

.items()
# 딕셔너리 키/값 쌍을 모은 객체를 반환
# 튜플로 한 쌍.
for key, value in my_dict.items():
    print(key, value) #이런 느낌으로 언패킹

.pop(key[,default])
# 키를 제거하고 연결됐던 값을 반환(없으면 에러나 default 반환)
print(my_dict.pop('age', 'Country 없음'))

.setdefault(key[,default])
# 키와 연결된 값을 반환, 키가 없다면 default와 연결한 키를 딕셔너리에 추가하고, default를 반환

.update([other])
# other가 제공하는 키/ 값 쌍으로 딕셔너리 갱신.
# 기존키는 덮어씀
# 키워드 인자로도 가능하다.
# 딕셔너리 하나 넣기도 가능 
my_dict.update(age=50)
my_update(country = "korea")




a
```
## 복사.
```python
# 변경 불가 데이터 복사
a = 20
b = a
b[0] = 10

print(a) # 20
print(b) # 10
#문제 없쥬?




```
### 유형

#### 1. 할당.  
- 리스트 복사 예시
    - 할당 연산자를 통한(=) 복사는 해당 객체에 대한 객체 참조를 복사한다.
```python


```



#### 2. 얕은 복사.  
- 리스트 얕은 복사 예시
  - 슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재한다.

```python
#

#
a = [1, 2, 3]
c = a.copy()
c[0] = 100 
print(a,c) # [1, 2, 3] [100, 2 ,3]

# 얕은 복사의 한계
a = [1,2, [1, 2]]

b = a[:]
b[2][0] = 999
print(a,b) # [1, 2, [999, 2]] [1, 2, [999, 2]]

a = [1,2, [1, 2]]
c= a.copy()
c[2][0] = 999
print(a, c) [1, 2, [999, 2]] [1, 2, [999, 2]]
#리스트 내부의 리스트는 같은 참조 中

#깊 은 복 사 #

import copy
```
#### 3.  깊은복사 

- 리스트 깊은 복사 예시
    - 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
``` python 
#깊 은 복 사 #

import copy

original_list = [1,2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 999

print(original_list, deep_copied_list) #[1, 2, [1, 2]] [1, 2, [999, 2]] 살았다!




```






[돌아가기](../../2023년7월2023Julio.md/##20230725)

[이전](../2023_07_24/README.md)


[다음](../2023_07_26/README.md)