
## 2023_07_21

어제 많이 급했나봅니다. 

### 관통프로젝트 PJT 1 시작.

url 
요청을 보내는 서버의 주소

requests.get(url)
해당 서버(url)에 데이터를 달라고 요청을 보내는 함수

.json()
내부의 데이터를 JSON (python의 dict와 비슷)형태로 변환해주는 함수

#### API 
클라이언트가 원하는 기능을 수행하기 위해 서버측에 만들어 놓은 프로그램.
 - 기능 예시 : 데이터 저장 조회 수정 삭제<p>
  
서버 측에 특정 주소로 요청이 오면 정해진 기능을 수행하는 Api 를 미리 만들어 둔다.
- 클라이언트는 서버가 미리 만들어 놓은 주소로 요청을 보낸다.

오픈 API 
외부에서 사용할 수 있도록 무료로 개방(open) 된 API

너무 많은 계정에서 동시에 요청을 보내면 서버가 견디지 못함.<P>
이런 문제를 해결하기 위해 OPEN API는 API KEY를 활용하여 사용자를 확인한다.<P>
-사용자 인증 혹은 회원가입을 하면 서버에서 API KEY를 발급해줌.<P>
-서버에 요청할 때 마다 해당 API KEY를 함께 보내 정상적인 사용자인 것을 확인 <P>
API KEY를 가진 사용자가 1231278489123번 요청 보낸다면  >> 죽은 서버, 죽은 서비스<P>
일부 오픈 API는 사용량이 제한됨.<P>
- 공식 문서의 일일/ 월간 사용량 제한을 반드시 확인 <P>
- 요금 나올수도 있음 ㅋㅅㅋ<P>
- 날씨데이터 수집하러갑시다.<P>
[관통프로젝트 정리](SSAFYPJT1.md)  *죽었음*

> JSON
JavaScript Object Notation의 약자 ' 자바스크립트 객체 표기법'
데이터를 저장하거나 전송할 때 많이 사용되는 경량의 텍스트 기반의 데이터 형식
통신 방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 방법 중 하나.

Python은 JSON을 활용하는 기능을 가지고 있다.

- Parsing 데이터를 의미있는 구조로 분석, 해석
- json.loads() : JSON 형식의 문자열을 파싱 - Python dictionary로 전환 

 ---


[돌아가기](../../2023년7월2023Julio.md/##20230721)

[이전](../2023_07_20/README.md)


[다음](../2023_07_22/README.md)
