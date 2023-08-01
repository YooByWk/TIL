# 카운팅 정렬 연습입니다.  # 순서가 유지된다는 장점이 있읍니다.
DATA = [0, 4, 1, 3, 1, 2, 4, 1]
# 0, 1, 1, 1, 2, 3, 4, 4
# 0, 1, 2, 3, 4, 5, 6, 7
#    _        _  _  _     # _ 자리 = 값이 변하는 자리
# 1, 4, 5, 6, 8
# 


COUNTS = [] # 이곳에 카운트합니다.
COUNTS = [0] * 10  # IDX가 KEY가 됩니다 #그러려니 합시다
for d in DATA: #data에서 나온 숫자
    COUNTS[d] += 1 #로 인덱스해서 그 자리의 숫자 1 더해줌
# [1, 3, 1, 1, 2, 0, 0, 0, 0, 0] 나오는데 
S = 0 
for S in range(9):
    COUNTS[S+1] += COUNTS[S] # 더하고 합 누적? / 자리 정보
    #[1, 4, 5, 6, 8, 8, 8, 8, 8, 8]
print(COUNTS)

Sortedlist = [-1] * len(DATA) #DATA만큼 정렬할거니까
# -1 초기화 => 디버깅에 좀 편함. 0으로 초기화된건지 오류난건지 모르니까
# -1은 결국 Error // 조건마다 다른 문자나 숫자를 쓰자.
for d in DATA:
    pos = COUNTS[d] - 1 # 위치니까 -1
    Sortedlist[pos] = d # 그 위치에 d 자료를 넣어준다
    COUNTS[d] -= 1      # 다음 자리에 넣어야 하니까 COUNTS[D] -1
    # 맨 위에 하나씩 생각해보면 됨

print(Sortedlist)

