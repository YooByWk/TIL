from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
#  참고 . 터미널 에러
# UserWarning: Starting a Matplotlib GUI outside of the main thread will likely fail. 
# PLT 를 만드는 곳과, 그리는 곳이 달라서 오류가 날 수 있으니 경고한다.
# 공식문서 matplotlib.org쪽
# 백엔드를 Agg로 설정하여 해결
plt.switch_backend('Agg')

# io : 입출력 연산을 위한 Python 표준 라이브러리
# ByteIO : 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 : 임시 저장 공간
# 파일 시스템과 유사하지만, 실제로 파일로 만들지는 않고, 메모리 단에서 작업 가능함.
from io import BytesIO #

# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
import base64

# 그래프를 그려보겠습니다.
def index(request):
        
    x = [1, 2, 3, 4]
    y = [2, 4, 8, 16]
    
    # 다른 View 함수에서 plt 를 이미 그린 상태에서 
    # 다시 그리는 경우를 대비하여, 초기화를 진행하는 것이 좋다.
    plt.clf()
    
    plt.plot(x,y)
    plt.title("Test Graph")
    plt.ylabel('y label')
    plt.xlabel('x label')
    
    # # plt.show() # Que occurrira? >>>> no lo hagas. va a presentar una nueva pagina.
    # context = {
    #     'plt' : plt.plot(x,y)
    # }
    
    
    # 비어있는 버퍼를 생성
    buffer = BytesIO()
    
    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')
    
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    
    # 버퍼를 닫아줌
    buffer.close()
    
    # 이미지를 웹 페이지에  보내주자 ( 표시하기 위해 )
    # template이 읽을 수 있도록 URI 형식(주소 형식) 으로 만들어진 문자열을 생성
    context = {
        # 저장된 이미지의 경로
        'chart_image' : f'data:image/png;base64,{image_base64}',
    }
    
    return render(request, 'index.html', context)


import pandas as pd
csv_path = 'firstapp/data/austin_weather.csv'
# 경로 맨 앞에 아무것도 없이 적으면 베이스 경로를 의미한다. 
def example(request):
    df = pd.read_csv(csv_path)
    # 이러면 전체 데이터가 그냥 넘어감
    # 표로 만들어야 하니 -> html 에서 되면 좋겠지만, 직접 해야죠...
    context ={
        'df':df
    }
    return render(request, 'example.html', context)
