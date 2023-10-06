# 2023_10_06


# 관통 PJT.
Django 에서 데이터 사이언스 패키지 사용하기!

## ? 캐글? 
 [Kaggle: Your Machine Learning and Data Science Community](https://www.kaggle.com/)

## 이전 PJT와의 차이점!
- 공통점 : Matplotlib, Pandas, Numpy를 구동했다. 
- 이전 : 주피터 노트북에서 구동함! 
  - 콘솔 or vscode etc에서 !
- 이번 : Django 에서 구동! 
  - 웹 사이트에서!

## 알아야 할 내용 
- 데이터 사이언스 3종 패키지 사용방법
- Django 기본 사용 방법
  - 웹 페이지 구성 (template)
  - 데이터 전달(View -> Template)
- 파이썬 BytesIO 패키지(곧 학습 예정)

matplotlib 연습
```py
 import matplotlib.pyplot as plt

# 참고 xyz 같을 때
plt.plot([1,2,3,4])
# plt.show()

# 참고 : 이때까지 그렸던 plot 지우기
plt.clf() 
#  중요합니다.


# 예제 2 : x,y 가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x,y)
plt.show()
# 어지간하면 x축을 통일하시오.
y = [2, 345, 12, 24]
plt.plot(x,y)
plt.show()

# 예제 3 : 제목 + 각 축의 설명
plt.plot(x, y)
plt.title("Test Graph")

# x , y 축
plt.ylabel('y label')
plt.xlabel('x label')

plt.show()
# 한글은 깨집니다.
# 구글링 해보세요.

# 자 가보자 드장고


# 사진을 창이 아닌, 파일로 저장받기
plt.savefig('filename.png')
# show를 지워야 함.
# 안그러면 흰색나옴 // show를 하는 순간 사라지기 때문.
 ```

 ## 장고 사용자가 제일 먼저 만나는 것은 pjt의 urls

 1. pjt setting -> app reg.
 2. pjt urls. -> include, urls setting
 3. make urls.py at app folder
 4. confg. app's urls and import views 
 5. reg. path // see the app/urls.py 
 6. views
 7. template folder / make html. ( acd to views)
 8. 


Es django  la 1a app o la 2a?

```py
def index(request):
        
    x = [1, 2, 3, 4]
    y = [2, 4, 8, 16]
    
    plt.plot(x,y)
    plt.title("Test Graph")
    plt.ylabel('y label')
    plt.xlabel('x label')

    # plt.show() # Que occurrira? # no lo hagas. va a presentar una nueva pagina.
    context = {
        'plt' : plt.plot(x,y)
    }
    
view에서 이런다고 뭐가 나오지 않음. 
```

1. plt 받는 법 -> 이미지 태그 ? 
   이미지 저장하기?
   근데 이거때문에 스태틱, 미디어 이짓 저짓? 에에에
    - 그러지말고 임시저장 하죠? - 버퍼 활용


Django Template 그래프 출력

- View  에서 Template으로 이미지 전달하기

view에서 Template으로 이미지 형식 데이터 직접 전달 불가... 교재 확인

```py 
# io : 입출력 연산을 위한 Python 표준 라이브러리

from io import BytesIO #

# io : 입출력 연산을 위한 Python 표준 라이브러리
# ByteIO : 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼 : 임시 저장 공간
# 파일 시스템과 유사하지만, 실제로 파일로 만들지는 않고, 메모리 단에서 작업 가능함.


# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
import base64


```
이거하세용
순서는 다음과 같을 것 같습니다.
1. plot
2. 이진 data
3. 버퍼(저장)
4. 저장주소 - - 
5. template
6. 짜잔!
   - 외울필요 없읍니다. 이런 과정이구나, 를 이해하세요

## pandas
어떻게 데이터 프레임을 여는가
1. app에 data file