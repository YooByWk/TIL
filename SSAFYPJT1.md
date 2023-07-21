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