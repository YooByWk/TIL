import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_YOOBYEONGWOOK'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수


    # 지금 이 상태로는 첫 공을 넣은 후 아무것도 하지 못함 따라서 탐색을 시켜야 합니다.
    distance = 9913875892  # 더 큰 거리 비교를 위한 무작위의 큰 수
    # test
    cnt = 1
    for i in range(1, 6, 2):  # 0번 인덱스는 white ball
        if balls[i][0] > 0 and balls[i][1] > 0:
            t_targetBall_x = balls[i][0]
            t_targetBall_y = balls[i][1]
            # targetBall_x = balls[i][0]
            # targetBall_y = balls[i][1]
            # print(i, ' 0 이상 검출 확인용' )
            # test
            t_width = abs(t_targetBall_x - whiteBall_x)  # 임시 좌표로 가까운 공 부터 확실하게...
            t_height = abs(t_targetBall_y - whiteBall_y)  # 가까운 공 탐색
            t_distance = math.sqrt(t_width ** 2 + t_height ** 2)
            # print(t_distance, t_width, t_height, "tdis,twid,thei")
            if t_distance < distance:
                if i != 5:
                    distance = t_distance
                    targetBall_x = balls[i][0]
                    targetBall_y = balls[i][1]
                    # print("타겟이 바뀌는 걸까요..?")


            # 저는 검은공이 무섭습니다. 따라서 확실한 조건을 사용하기로 했습니다.
            # 다른 공이 존재한다면 검은공은 건드리지 않습니다.
            if balls[1][0] < 0  and balls[3][0]  < 0 and balls[5][0] > 0:
                # 위 조건을 뚫지 못한다면, 8번공을 도전할 수 없습니다.
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                print("5번 도전입니다.")

    # 디버깅
    # print(targetBall_x, targetBall_y)
    # test
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]
    # print(targetBall_x, targetBall_y , 'tgt')

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    radian = math.atan(width / height) if height > 0 else 0
    angle = 180 / math.pi * radian

    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180

    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    # test
    ##########################################################
    # 자세히 들여다보니 4번에서 계속해서 아래쪽으로 angle을 잡는것으로 보아, 새롭게 필요하다는 생각이 들었습니다.
    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y < targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270
        # print(radian, "radian")

    # test # 여기까지가 테스트였습니다.
    ##########################################################

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width ** 2 + height ** 2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    # power = distance * 0.5
    power = distance * 0.5
    if power < 47:
        power = 55
    else:
        power = distance * 0.6
    # print(targetBall_x,targetBall_y,'tgt') # 타겟 확인용
    if 63.99999999<  balls[0][0] <64.00001 and balls[4][0] > 1:
        # 첫 직선상태 해결을 위함. 이후 코드는 order에 따라서 1,5 를 중심으로 잡는 것이 좋을 것 같습니다.
        # 다만 개인전의 경우 제 순서는 언제나 1이었기에, 큰 문제가 없었습니다.
        angle = 87
        # 디버그
    # print(distance, "dis")
    # print(angle, "angle")
    # print(power, "power")

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')