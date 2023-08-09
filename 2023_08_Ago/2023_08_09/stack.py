# 입력이 불가능한 경우 -1 return
# 입력에 문제가 없는 경우 return top

def isFull():
    if top == SIZE - 1 :
        return True
    else : 
        return False
    

def push(item):
    global top
    # if isFull(): 과 같음
    if top == SIZE -1 :
        print('overflow')
        return -1
    top += 1
    ST[top] = item
    return top

# 스택이 비어 있으면 -1
#  아니면 top 위치에 있는 item 을 return
def pop():
    global top 
    if top == -1 :
        print('underflow')
        return -1
    # if isEmpty():
    result = ST[top]
    top -= 1
    return result
    # top -= 1
    # return ST[top+1]



SIZE = 10
ST = [-1] * SIZE
top = -1
lst = [4,5,6,10]
for d in lst:
    push(d)
print(ST)
print(pop(), top) # 10 , 2 
print(ST)

ST_P = [] 
for d in lst:
    ST_P.append(d)
print(ST_P.pop())