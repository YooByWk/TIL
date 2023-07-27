# 2023_07_27

## Class 상속

기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것 

필요한 이유
상속으로 기존 클래스의 속성과 메서드를 재사용
새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용, 중복코드 줄임

계층구조. 
상속을 통해 클래스간의 계층구조 형성 가능
부모 클래스와 자식 크랠스간의 관계를 표현하고 더 구체적인 클래스를 만들 수 있다.

유지 보수 용이성
상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면되므로, 유지 보수가 용이해짐.
코드의 일관성을 유지하고, 수정이 필요한 범위를 최소화.

```python
class A(B):
    # 이런 느낌 같은데
```
다중상속도 있읍니다. - 적어놓은 순서대로
```python
super()
```
 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수.

### 다중상속

- 두 개 이상의 클래스 상속
- 상속 받은 모든 클래스의 요소 활용 가능
- 중복된 속성이나 메서드가 있는 경우 **상속 순서**에 의해 결정

클래스 줄 간격 두줄이 국룰;; 

### 상속관련 함수와 메서드
- mro()
- Method Resolution Order
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 기존의 인스턴스 > 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 > 자식 > 부모 로 확장 

버그  
진짜 버그임.

## 디버깅
1. print 함수 활용 (특정 함수 결과, 반복/조건 결과 나눠서 생각 )
2. 개발 환경에서 제공하는 기능
3. Python tutor (단순)
4. 뇌컴파일 눈디버깅;;

## Error 

### 문법에러 Syntax Error
구문이 올바르지 않은 경우
#### 예시
Invalid syntax  
assign to literal  
EOL  
EOF  

### 예외 Exception
프로그램 실행 중에 감지되는 에러 

#### 내장 예외 Built-in Exceptions
예외 상황을 나타내는 예외 클래스들  
- 이미 파이썬에서 정의되어 있음 특정 예외 상황에 대한 처리를 위해 사용됨

    1. ZeroDivisionError  
    2. NameError
    3. TypeError
        - 인자 초과
        - 인자 타입 불일치
        - 타입 불일치
        - 인자 누락
    4. ValueError
    5. IndexError  인덱스 범위 이탈
    6. KeyError 딕셔너리에 키 없는 경우
    7. ModuleNotFoundError 모듈 못찾음
    8. ImportError import 하려는 이름 찾을 수 없을 때 
    9. KeyboardInterrupt 사용자가 ctrl-c or del 누를 때  (무한루프 강종)
    10. IndentationError 잘못된 들여쓰기...

#### 예외처리
try-except
try 블록 안에는 예외가 발생할 수 있는 코드를 작성
except 블록 안에는 예외가 발생했을 때 처리할 코드를 작성
예외가 발생하면 프로그램 흐름은 try 블록을 빠져나와 해당 예외에 대응하는 except 블록으로 이동.
```python
try: 
    result = 10 / 0
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.') # 0 으로 나눌 수 없습니다.


try:
    num = int(input('숫자입력 : '))
except ValueError: 
    print('숫자가 아닙니다.')
```
복수 예외 처리 연습 >> 
** 에러의 클래스를 생각해보자** 
* 하위 클래스부터 상위로 거슬러 올라가는*  // 안그러면 상위에서 다 걸려버린다.  <br>
---
**EAFP**
*"Easier to Ask for Forgiveness than Permission"*
*예외처리를 중심으로 코드를 작성하는 접근 방식 (try - except)*
```python
try:
    result = my_dict['key']
    print(result)
except KeyError:
    print('키없음')

```
---
**LBYL**
*"Look Before You Leap"*
*값 검사를 중심으로 코드를 작성하는 접근 방식( if- else)*
```python
if 'key' in my_dict:
    result = my_dict['key']
    print('result')
else:
    print('key 가 존재하지 않음')
```

LBYL , 미리 쓱 싹... EAFP 로직 외 문제? 상 EAFP를 ...
아직 알고리즘 푸는 동안은 빠짐없이 다 짜보기. . .


as 키워드를 활용하여 에러 메시지를 except 블록에서 사용 가능. (변수같은건가) as는 뭐지

as? 
as?
as?
as? 
que es  as?


공식문서를 한번 봅시다. 
1번부터 9번까지 다 써봅시다 


```python
__del__(self):
    print('객체 소멸') # 객체 죽이기

```


[돌아가기](../../2023년7월2023Julio.md/##20230727)

[이전](../2023_07_26/README.md)


[다음](../2023_07_28/README.md)