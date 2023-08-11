# 2023_08_11

## 1974 스도쿠 검증
9개 읽음 : 1~9 까지 하나만 나오는가 어떻게 할 것?  
count배열로? 
-> 다 저장하고 set으로 보는건 어ㄸㅐㅇㅛ

```py
def sudoku(arr):
    for i in range(9):
        cnt = [0] * 10 
        for j in range(9):
            cnt[arr[i][j]] += 1
        for k in range(1,10):
            if cnt[k] == 0:
                return 0 # 




T = int(input())
for t in range(1,T+1):
    sdk = [list(map(int, input().split()))for _ in range(9)]
    ans = sudoku(sdk)
    print(f'#{t} {ans}') # 정답 표기
'''
    for i in range(9):
        cnt = [0] * 10 
        for j in range(9):
            cnt[arr[i][j]] += 1
            for k in range(1,10):
                if cnt[k] == 0:
                    ans = 0  
                    break
        if ans = 0:
            break
                이러지 말고, 나가기 힘들잖아.
'''
``` 
*나름 생각했던거랑 비슷하네요.*

## 1234 비밀번호

스택... 사실 우린 거기에 들어있는걸 지운적이 없어...

```py 
str_N, str_num = int(input())
N = int(str_N)
stack =  [0] * N
top = -1 

for t in str_num:
    if top == -1 or stack[top] != t: #스택이 비어있거나, top 원소와 다르면 
        top += 1                    # push(t)
        stack[top] = t 
    else:
        top -= 1 
    #ans = ''
    # for i in range(top+1):
    # ans += stack[i]
    # print(f'#{tc} {ans}')
    ans = ''.join(stack[:top+1])
    print(f'#{tc} {ans}')

```

## 1859 백만장자 프로젝트
오른쪽부터 오도록 하자
비교를 잘 해야 시간초과가 안나온다.
gg..

## 5432 쇠막대기
너는 내가 직접 해결했다 쇠막대기!
(
()
)
잘 봅시다. 막대기인지, 레이저인지


### 돌맹이
```py 
res = -0 
arr[r][c] = 1
for dr, dc in [(1,0),(-1,0),(0,-1),(0,1)]:
    newR = r + dr
    newC = c + dc
    if newR, newC 범우ㅢ비교 and arr[newR][newC] ==2:
        대충 가이드라인