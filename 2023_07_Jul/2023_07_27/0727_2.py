try:
    num = int(input('100으로 나눌 값 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자 쓰라고요')
except ZeroDivisionError:
    print('0으로 나누는 인성 무엇')
# except (ValueError, ZeroDivisionError ):
#     print('좀;;;')


except BaseException:
    print('asdf'
    )
except ZeroDivisionError:
    print('nahhh') # 위에서 이미 죽어버려서 안됨.. . . #하위 클래스라서 흐려졌음
except:
    print('에러임 ')