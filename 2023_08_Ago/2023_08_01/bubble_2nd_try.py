# bubble.

T = 1
for tc in range(1,T+1):
    nums = list(map(int, input().split()))
    # print(nums)
    N = len(nums)
    for phase in range((N-1),0,-1):
        # N 이 6이라면... PHASE : 5
        # 0 - 1, 1 - 2, 2 - 3, 3 - 4, 4 - 5 : 0~4
        #PHASE : 4
        # 0 -1 , 1 -2, 2 - 3, 3 - 4 : 0 ~ 3
        for j in range(0, phase):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    print(nums)
    #55 21 11 67 100 12 
    #[11, 12, 21, 55, 67, 100]
# 이젠 뒤집어봅시다
    print('역방향에서 정렬시작할걸요?')
    for phase in range(0,N-1, 1): #range 마지막 1은 생략해도 뭐..
        # phase = 0 
        # 뒤 기준 n-2 0까지 1 - 0 까지 n-1 ~ 1 
        # phase 1 일때 :   2 -1 까지 n-2 ~ 2
        for j in range(N-1, phase, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
                
    print(nums)