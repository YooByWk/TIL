def itoa(int_value):
    temp = int_value
    s = '' 
    while temp > 0:
        one = temp % 10
        s =  chr(one + ord('0')) + s
        temp //= 10
 
    return s # 0 을 기준으로 합니다?
    #ASCII
t = itoa(2567)
print(t, type(t)) 
# int > str

def atoi(str_value):
    value = 0
    for i in range(len(str_value)):
        c = ord(str_value[i]) -0x30 #16진법 30
        value = value * 10 + c
    return value
        
    #4 는 ASCII 52
    
t = atoi('4567')
print(t, type(t))
# str -> int
