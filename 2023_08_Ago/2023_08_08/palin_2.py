import sys
sys.stdin = open('input2.txt')
T = 10
for t in range(1, 1+T):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    # print(arr)
    res = 0
    maxR = 0
    for r in range(100):
        for d in range(1,101): # 실험해볼 길이
            # my_str = ''
            for i in range(100-d+1):
                my_str = ''
                for c in range(i, i+d):
                    my_str += arr[r][c]
                if my_str == my_str[::-1]:
                # temp = my_str
                    # print(temp)
                    if len(my_str) > maxR:
                        maxR = len(my_str)


    for c in range(100):
        for d in range(1,101):
            # my_str = ''
            for i in range(100-d+1):
                my_str = ''
                for r in range(i,i+d):
                    my_str += arr[r][c]
                if my_str == my_str[::-1]:
                    # temp = my_str
                        # print(temp)
                    if len(my_str) > maxR:
                        maxR = len(my_str)
    print(f'#{t} {maxR}' )


