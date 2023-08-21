# 2023_08_14 보충수업.
# 변환하기
# 문자열로 받음

# swea 1222
# 계산식을 후위 표기식으로 바꾸자.

T = 10
for t in range(1,T+1):
    # 연산자가 + 하나네요 나이스
    N = int(input()) # 계산식의 총 길이
    tokens = input()
    numbers = '0123456789' # 숫자인지 확인하기 위한 문자열
    # 후위 표기법 
    # 필요한 것은 stack
    stack = []
    postfix_notation = ''
    # 토큰을 하나씩 불러서 스택의 마지막 연산자와 비교해서 stack에  넣을지 말지 정하기.
    # 단 토큰의 숫자는 바로 출력한다. ( 새로운 문자열로 만들 것이다.)
    for token in tokens:
        # token이 숫자라면, 그대로 붙이고
        # token이 연산자라면 stack과 비교할것이지만 +밖에 연산자가 없다.
        # pop 후 push 할 것. ( +와 +는 우선순위가 같기 때문에, 빼고 더하는 식으로 관리한다.)
        if token in numbers: # 토큰 값이 문자열에 있다면 숫자임!
            # 숫자는 바로 출력
            postfix_notation += token
        else: # 연산자라면
            if len(stack) == 0: # 근데 연산자 밖에 없으니까 
                # stack에 연산자가 있으면 pop 후 append
                # stack이 비어있다면 바로 append
                # if stack: 도 False / True긴 하지만 js 는 빈 리스트도 True...
                # 명시적으로 쓰자...
                stack.append(token)
            else:
                tmp = stack.pop()
                postfix_notation += tmp
                stack.append(token)
            # 모든 토큰 확인이 끝나면 stack에 남은 한 개의 연산자를 출력해준다.
    postfix_notation + stack.pop()

    # print(postfix_notation) # 후위연산 끝

    # 계산합시다.
    # 숫자 stack 넣고 연산자 오면 두개 꺼내서 계산하기.
    for token in postfix_notation:
        if token in numbers:
            stack.append(token)
        else: # 숫자가 아닌, 연산자라면:
            value2  = stack.pop()
            value1 = stack.pop()
            result = int(value1) + int(value2)
            # 계산이 끝나면 스택에 push!
            stack.append(result)
    print(f'#{t} {result}')
    