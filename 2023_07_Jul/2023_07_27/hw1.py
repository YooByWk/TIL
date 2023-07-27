# hw_8_2.py

# 아래 함수를 수정하시오.
def check_number(x):
    try:
        # num = int(input('숫자를 입력하세요 '))
        print(f'숫자를 입력하세요 : {x}')
        if x == 0:
            print('0입니다.')
        elif x > 0:
            print('양수입니다.')
        else:
            print('음수입니다.')
    except ValueError:
        print('잘못된 입력입니다.')
    
    except TypeError:
        print('잘못된 입력입니다.')


for i in range(-1,2):
    check_number(i)
check_number('ㅁ')

