T= 10
for t in range(1,1+T):
    N = int(input()) #  찾아야 하는 회문의 길이
    arr = [input() for _ in range(8)]
    # print(arr)
    # 찾을 문자열 만큼 자르기
    # 8, 4 면 총 5개 0123 1234 2345 3456 4567
    count = 0
    for r in range(8):
        for d in range(8-N+1): # 이제 우리 N개로 자를 수 있어!
            my_str = ''
            for c in range(N):
                my_str += arr[r][c+d]
            if my_str == my_str[::-1]:
                count += 1
    for c in range(8):
        for d in range(8-N+1):
            my_str = ''
            for r in range(N):
                my_str += arr[r+d][c]
            if my_str == my_str[::-1]:
                count += 1
    print(f'#{t} {count}')



