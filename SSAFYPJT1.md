# 관통 프로젝트

강의 시간에 배운 내용을 모두 포함 (관통)

도전과제는 두 개

관통 ver1 : 금융 데이터 활용 금융상품 비교 app
pyt 1 > 2 ... 10 
관통 ver2 : Open API와 외부 데이터를 활용한 영화추천 서비스
pyt 1 > 2 ... 10 

> (필)
> 선택은 04PJT까지 자유롭게 변경 가능
> 그 후로는 최종 프로젝트를 진행하기 위한 내용이 포함 


requests를 깔아둡시다 (完)

> JSON
JavaScript Object Notation의 약자 ' 자바스크립트 객체 표기법'
데이터를 저장하거나 전송할 때 많이 사용되는 경량의 텍스트 기반의 데이터 형식
통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 방법 중 하나.

특징 <P>
데이터는 중괄호{}로 둘러싸인 키-값 쌍의 집합으로 표현<P>
키 = 문자열 / 값 = 다양한 데이터 유형
값 쉼표로 구분.<P>
Python은 아무튼 JSON을 활용하는 기능이 있음.
- Parsing 데이터를 의미있는 구조로 분석, 해석

- json.loads() : JSON 형식의 문자열을 파싱 - Python dictionary로 전환 

### 관통 ver1 - pjt 도전과제

파이썬으로 API 데이터 수집

목표
- 파이썬으로 정기 예금 데이터 수집 및 미션 수행 (금감원)

특징 
- 외부 서버를 활용한 데이터 수집
- 요구사항에 맞게 JSON 형태 데이터를 가공.

### 관통 ver2
파이썬을 활용한 데이터 수집 1 

목표 
- 파이썬으로 도서 및 아티스트 데이터 가공 및 미션 수행

특징 
- 샘플 데이터 제공
- 요구 사항에 맞게 JSON 형태 데이터 가공 .
pjt 이름은 
프로젝트 번호 + jtp  01_pjt

```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "75280bc41cbd3ffdbd916b4df9ec0fa2"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        #금융회사가 속한 권역 코드 020000(은행), 030200(여신전문), 
        #        030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url, params = params).json()
    result = response['result'].keys()
    return result
pprint.pprint(get_deposit_products())
```
대충 불러오는 방법입니다. 사실 아무것도 모르겠읍니다.
불러오는 것이 익숙하지 않고, 문제 이해가 아직 어렵다.

# 01-pjt

> ## Ver. 1

### 예금 정보를 API로 받아보자.
---
#### ver 1,problem A / 1번
사실상 처음이기에 너무나도 어려웠다. API 설명에 따라 단순히 url과 다른 요소들을 이용하여 정보를 받아오는 것만 해도 약 2시간이 걸렸는데,이런 과정에서 금감원의 API 설명이 참 불친절하다는 생각도 들었다. 이런 불편함을 기억하고 훗날 뭔가 만들게 된다면 역시 제일 중요한 것은 잘 사용하기 위한 가이드라인이 아닐까 싶었다.
```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "본인의 API KEY 로 수정합니다."
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        #금융회사가 속한 권역 코드 020000(은행), 030200(여신전문), 
        #        030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url, params = params).json()
    result = response['result'].keys()
    return result
pprint.pprint(get_deposit_products())
```
- 특히 def get_deposit_products()부터 response까지는 이해하기보다는 따라하며 일단 실행시켜보는 느낌으로 진행했다.
다만 api를 이용하기 위한 방법과
- .json() , requests.get(url) 등의 정보를 가져오는 방법을 배울 수 있었고 Keys(),의 개념과 이를 실제로 사용하며 조금 더 익숙해지는 기회였다.
---
#### ver 1 .problem B /2번
```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "본인의 API KEY 로 수정합니다.
"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        #금융회사가 속한 권역 코드 020000(은행), 030200(여신전문), 
        #        030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    
    response = requests.get(url, params = params).json()
    
    result = response['result']['baseList']
    
    return result
```


##### 새로 배운 것

 이번주에 배운 딕셔너리에 대해 훈련할 수 있는 좋은 기회였고, 오히려 1번보다 간단하게 해결할 수 있었다.

##### 문제 외적으로 어려웠던 점 : 

처음에 1번에서 URL을 잘못 이해한 이유로, 완전히 잘못된 문제를 풀고 있어서 순간 매우 당황했지만 주변 동료들과 강사님의 도움으로 해당 URL 문제를 해결하였고 다시 문제를 풀어나갈 수 있었다. 다들 감사합니다. 

- 쉽게 풀리는 문제도 가끔은 필요할 듯 싶다.
  
##### 어려웠던점
 dict['a']['a']이런 딕셔너리 안의 딕셔너리 안의 딕셔너리 안의.... 딕셔너리가 아직은 전혀 익숙하지 않아 힘들었다.

---
 #### ver 1 .problem C / 3번
 ```python
 def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        #금융회사가 속한 권역 코드 020000(은행), 030200(여신전문), 
        #        030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }

    #   금융상품코드  fin_prdt_cd  //  WR0001B 정기예금,
    # 금리 intr_rate
    # 기간 save_trm
    # 금리유형 intr_rate_type
    # 금리유형명 intr_rate_type_nm
    # 최고우대금리 intr_rate2
    
    json_response = requests.get(url, params = params).json()
    optionlist = json_response['result']['optionList']
    result = []
    for r in optionlist:
        new_option = {'금융상품코드' : r['fin_prdt_cd'],
                          '저축 금리' :r['intr_rate'],
                          '저축 기간' : r['save_trm'],
                          '저축금리유형' :r['intr_rate_type'],
                          '저축금리유형명' :r['intr_rate_type_nm'],
                          '최고 우대금리' :r['intr_rate2']
                         }
        result.append(new_option)

    return result
pprint.pprint(get_deposit_products())
 ``` 

##### 접근 방향

필요한 정보를 수집 - 문제를 푸는 과정에 쉽게 찾을 수 있었다. 
        금융삼품코드, 금리, 기간, 금리유형, 금리유형명, 최고우대금리

for과 요소 하나하나를 통해 (for에 list 사용하듯...) **하나하나** 만드려고 했지만 너무 일이 거창해질 것이라며 도와주신 강사님 덕분에 지금까지 짜본 코드 중 **많이** 깔끔한 코드가 하나 탄생한 기분이다. 
Python의 강점인 딕셔너리를 사용하기 위한, 만들기 위한 훈련이었던 것 같다.

##### 어려웠던 점<p>
for문을 이용한 (for문 이하에서 ) '딕셔너리' 만들기
append()를 사용하기 위한 result의 위치 생각.

##### 얻은 것<p>
   - for문을 이용한 딕셔너리의 제작<p>
   - for문 사용훈련
   - append의 작동방식을 생각해봄


-----

 #### ver 1 .problem D / 4번

```python
def get_deposit_products():
    # 본인의 API KEY 로 수정합니다.
    api_key = "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        #금융회사가 속한 권역 코드 020000(은행), 030200(여신전문), 
        #        030300(저축은행), 050000(보험), 060000(금융투자)
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }

#       금융상품코드  fin_prdt_cd  //  WR0001B 정기예금,
#     금리 intr_rate
#     기간 save_trm
#     금리유형 intr_rate_type
#     금리유형명 intr_rate_type_nm
#     최고우대금리 intr_rate2
    
    json_response = requests.get(url, params = params).json()
    baselist = json_response['result']['baseList']
    optionlist = json_response['result']['optionList']
    
#     newop = [] # 제일 안쪽  필요없어보임.

    result = [] #제일 밖, 출력할 것
    
    for base in baselist:
        insidebase = [] #3개중 2번째 
        for r in optionlist:
#             temp_op = [] 어차피 insidebase에 순서대로 들어가니까 필요 X 
            if base['fin_prdt_cd'] == r['fin_prdt_cd']:
                new_option ={
                          '저축 금리' :r['intr_rate'],
                          '저축 기간' : r['save_trm'],
                          '저축금리유형' :r['intr_rate_type'],
                          '저축금리유형명' :r['intr_rate_type_nm'],
                          '최고 우대금리' :r['intr_rate2']
                            }
#                 newop.append(new_option)
#                 temp_op.append(new_option)
                insidebase.append(new_option)
        tempbase = {
            '금리정보' : insidebase,  #new_option
            '금융상품명' : base['fin_prdt_nm'],
            '금융회사명' : base['kor_co_nm']
            }
        result.append(tempbase)
    return result
pprint.pprint(get_deposit_products())
```
##### 시작 이전

먼저 진행하는 분들의 수많은 한숨이 시작 전 부터 나를 겁먹게 만들었던 문제.

##### 접근 방향
- 3번 문제에서 사용한 option을 만드는 문장을 재사용하기
- 큰 틀을 잡고 접근하기 (밖에서 안으로 들어감)
-    그림 그려보기.

##### 어려웠던 것
-  for가 많아지며 눈으로 쫓아가기 힘들었다.
-  base 와 option 두개를 생각해야 하는 것이 어려웠다.
-  딕셔너리 > 리스트 > 다시 딕셔너리에 넣는 여러가지 구조가 어려웠다 

##### 배운점 
- 조립은 분해의 역순과 닮아있는게 아닐까. . .
- 생각하고, 손으로 여러번 실험하며 얻은 구동원리의 "느낌"
- 강사님의 코드를 보며 더욱 더 간단하고 가독성 좋은 코드의 필요성과 쓰고싶다는 느낌을 받았다.
- for문과 다른 요소의 위치에 따라 결과가 매우 많이 변할 수 있다는 것을 알 수 있었다.
