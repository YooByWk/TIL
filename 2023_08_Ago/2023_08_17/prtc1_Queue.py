def enQ(data):
    global rear
    if rear == Qsize -1:
        print('Q is full',data)
    else: 
        rear += 1
        Q[rear] = data


def deQ():
    global front
    if front == rear:
        print('Q is empty')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3 
Q  = [0] * Qsize
rear = -1
front = -1

enQ(1)
enQ(2)
# enQ(3)
# 아래랑 
rear += 1
Q[rear] = 3 
# 같아요
print(Q)
print(deQ()) # 1
print(deQ()) # 2
print(deQ()) # 3
enQ(4) # Q is full 4
enQ(5) # Q is full 5

while front!= rear: # 큐가 비어있지 않다면,
    front += 1
    print(Q[front])

