# 핵심 로직
islogined = True
# 전처리, 후처리 로직이 너무 길다!
# 중복되는 코드가 너무 많이 발생!!! -> 없애는 방법
# 파이썬의 데코레이터를 활용!!!!


# myFunc 핵심 로직을 구현한 함수
def myFunc():
    print('myfunc')
def check_login():
    # 로그인 되어 있는지 여부 확인
    if islogined:
        return True
    
    print('myfunc')
    # 로직이 끝났다! 안내문
    
def my_decorator(func):
    def wrapper():
        # 전처리
        if not islogined:
            print('로그인하슈')   
            return
    # 후처리
    func()
    print('데코레이터 통과 알림, 로직 끝')
    return

# 핵심 로직 이전의 "전처리 과정"을 충족한다면, 원 함수를 호출한다.

@my_decorator
def myFunc():
    print(myFunc())
    
    
    
    
    
    
def myFunc2():
    pass
    
