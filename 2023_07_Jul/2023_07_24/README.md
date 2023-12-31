너무 늘어져서 문서 분리

2023_07_24

데이터 구조  Data Structure.
-자료구조

## method

객체에 속한 함수 

> 객체의 상태를 조작하거나 동작을 수행한다.
특징<o>
- 메서드는 클래스 내부에 정의되는 함수
- 클래스는 파이썬에서 **타입을 표현**하는 방법. *은연중에 사용해옴*
- ej) help 함수를 통해 str을 호출해보면 class 였다는 것을 확인 가능.
-  class는 OOP 수접에서 자세히 다룰 예정
-  메서드는 어딘가 존재하는 함수

데이터 타입 객체.메서드()
```python
'hello'.capitalize() # 첫글자 대문자화

```
## 시퀀스 (문자열)
### 메서드
```python
s.find(x)  # x의 첫 위치 반환 없으면 -1
print('banana'.find('z')) # -1

s.index(x)  # x의 첫번쨰 위치 반환, 없으면 오류

s.isalpha() # 알파벳 문자여부  (유니코드상 Letter / 한글 포함)

striong1 = "Hello"
string = '123'
print(string1.isalpha()) # True
print9string2.isalpha() #False

s.isupper() #대문자여부
#문자열이 모두 대문자/소문자로 이루어져 있는지 확인 

s.istitle #타이틀형식여부
#타이틀 형식 :

s.capitalize() 
# 첫 문자가 대문자이고 나머지가 소문자인 문자열의 복사본을 반환.

s.title() 
# 단어가 대문자로 시작하고 나머지 문자는 소문자가 되도록 문자열의 제목 케이스 버전을 돌려줍니다.
```
아무튼 공식문서 가서 보자.

### 문자열 조작 메서드 (새 문자열 반환)
- [ ] [BNF 표기법 알아보기](https://ko.wikipedia.org/wiki/%EB%B0%B0%EC%BB%A4%EC%8A%A4-%EB%82%98%EC%9A%B0%EB%A5%B4_%ED%91%9C%EA%B8%B0%EB%B2%95)
- [ ] [EBNF 표기법도 알아보기](https://ko.wikipedia.org/wiki/EBNF)
```python
s.replace(old, new [,count])
# [,count]선택인자. 얘는 파이썬 문법 아님...

s.strip([chars])
#문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
text = "           Hello world      "
new_text = text.strip()
print(new_text) #'Hello, world!'

.split(sep=None, maxsplit= -1)
#지정한 문자를 구분자로 문자열을 분리하여 문자열의 단어를 리스트로 반환

separator.join([iterable])
# iterable 요소들을 원래의 문자열을 구분자로 이용하여 하나의 문자열로 연결. * 중?요? <-> split
# separator을 중간중간에 삽입함
words = 'hello world'
text= '-'join(words)
print(text) # 'Hello-world'

t1= heLLo, woRld!
.capitalize() #Hello, world!
.title() # Hello, World!
.upper() # HELLO, WORLD!
.swapcase() #Hello, WOrLD! 스왑
 
# 메서드는 이어서 사용 가능 
new = t1.swapcase().replace('l', 'z') #HEzzO, WOrLD! (chained)



```
### 리스트 값 추가 삭제 메서드

```python
num = [1, 2, 3]
nums = [4, 5, 6]
L.append(x)
num.append(nums) #[1, 2, 3, [4, 5, 6]]
L.extend(m)
num.extend(nums) # [1, 2, 3, 4, 5, 6]
L.insert(i, x)
# 지정한 인덱스  I 위치에 x를 삽입.
L.remove(x)
# 리스트에서 첫 번째로 일치하는 항목을 삭제
L.pop(i)
# 리스트에서 지정한 인덱스의 항목을 제거하고 반환
# 작성하지 않을 경우 마지막 항목을 제거
# append의 반대라고 생각하면 편함 (i 없을때)
L.clear()
# 리스트의 모든 항목을 삭제
L.index(x, start, end)
# x의 인덱스 반환
L.reverse()
# 거꾸로 정렬 - 그냥 역순으로 '변경'
L.sort() # 반환 없음
# 오름차순 정렬 (원본에 변동 有)
# 내림차순
my_list.sort(reverse = True) [p3, 2, 1]
사실 reverse = False 가 들어있...나?
L.count(x)
# 리스트에서 항목 x가 등장하는 횟수를 반환

++
isdecimal()
isdigit() #isdecimal과 비슷하나, 유니코드 숫자 인식(1 동그라미안에있는거)
isnumeric() #분수 지수 루트 기호도 숫자로 이닉  

sorted는 함수임. #반환 함 / 원본 안바뀜
```
우리는 시험을 못해서 index를 해요.


[돌아가기](../../2023년7월2023Julio.md/##20230724)

[이전](../2023_07_23/README.md)


[다음](../2023_07_25/README.md)