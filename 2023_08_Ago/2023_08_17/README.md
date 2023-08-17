# 2023_08_17

## Queue 
선입선출 FIFO 구조.

Front 
- 저장된 원소 중 첫 번째 원소


Rear
- 저장된 원소 중 마지막 원소


### *큐의 기본 연산*
- enQueue  ( stack : push)
- deQueue  ( stack : pop)

###   Queue 의 연산 과정
--> 인덱스가 두개라고 생각하면 편해요 
1) 공백 큐 생성 : createQueue() front = rear = -1
2) 원소 A 삽입 : enQueue(A)  rear +=  1 Q[rear] = A
3) 원소 B 삽입 : enQueue(B)  rear += 1 , Q[rear] = B
4) 원소 반환 / 삭제 : deQueue(): front += 1, tmp = Q[front] \ or tmp = Q.pop(0)
5) 원소 C 삽입 : enQueue(c):  rear += 1, Q[rear] = c /\ Q.append(c)
6) 원소 반환 / 삭제 : deQueue()
7) 원소 반환 삭제 : deQueue()

### 구현 

#### 선형큐
- 1차원 배열을 이용한 큐
   - 큐의 크기 = 배열의 크기
   - front : 저장된 첫 번째 원소의 인덱스
  - rear : 저장된 마지막 원소의 인덱스 

- 상태 표현
  - 초기 상태 : front = rear = -1
  - 공백 상태 : front == rear 
  - 포화 상태 : rear == n-1 ( n: 배열의 크기, n-1 배열의 마지막 인덱스)
  
- 삽입 : enQueue(item)
  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
  - 1) rear값을 하나 증가시켜 새로운 원소를 삽입할 자리 마련
  - 2) 그 인덱스에 해당하는 배열원소 Q[rear]에 item을 저장
  
  [큐 예시](prtc1_Queue.py)

- 검색 : Qpeek() 
  - 가장 앞에 있는 원소를 검색하여 반환하는 연산
  -  현재 front 의 한자리 뒤 fornt + 1 에 있는 원소 즉 큐의 첫 번째에 있는 원소를 반환.
  