# 예비군으로 인하여 늦게 함.

# 2023_10_14


## Database

체계적인 데이터 모음 <br>
+ 데이터 저장 / 조작

역할 : (구조적)저장하고 조작. CRUD


### Relational Database
관계형 데이터 베이스  
데이터간 관계가 있...

- 테이블, 행 열 정보 구조화
- **서로 관련된** 데이터 포인터를 저장하고 이에 대한 액세스를 제공

### 관계 
여러 테이블의 (논리적) 연결  
이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 형식으로 조회 가능
- 특정 날짜에 구매한 모든 고객 조회
- 지난 달에 배송일이 지연된 고객 조회 등
- etc.

-> 외래 키 Foreign Key
- 고유한 식별 값

### 키워드

1. Table (alias Relation)
2. Field (Column, Attribute)
3. Record (Row, Tuple)
4. Database (Schema)
5. Primary Key (기본 키)
   - 각 레코드의 고유 값
6. Foregin Key
   - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
   - 다른 테이블의 기본키를 참조
   - 각 레코드에서 서로 다른 테이블 간의 관계를 만드는데 사용

## RDBMS
Databse Management System 
R  = Relational

관계형 데이터 베이스를 관리하는 프로그램

ej. 서비스 종류

1. SQLite
2. MySQL
3. PostgreSQL
   
DBMS 
- DB와 사용자간의 인터페이스 역할
- 이것저것 도움

### DB 정리

1. Table 데이터 기록되는 곳
2. 행에서 고유하게 식별 가능한 기본 키 라는 속성이 있고 외래키를 사용, 각 행에서 서로 다른 테이블 간의 결합

## SQL
Structure Query Language  
데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어
- 테이블의 형태로 구조화된 관계형 데이터 베이스에게 요청을 Query(질의) 하는 것

### 문법
1. 키워드는 대소문자 구분 안함
   - 대문자로 작성을 권장 ( 명시적 구분 )
2. 각 SQL Statements 의  끝에는 ; 필요
   - 세미콜론은 각 SQL Statements 를 구분하는 방법 ( 명령 종료 )


### SQL Statements
기본적 코드블록
```SQL
SELECT column_name FROM table_name;

```
4개의 유형 :
DDL : 데이터의 기본 구조 및 형식 변경 // CREATE DROP ALTER 
DQL : 데이터 검색 // SELECT
DML : 데이터 조작 // INSERT
DCL : 데이터 및 작업에 대한 사용자 권한 제어

### Query
SQL로 작성하는 코드를 쿼리문이라고 함

### Querying data

SELECT statement
- 테이블에서 데이터 조회

```SQL
SELECT
  select_list
FROM
  table_name;

```

[연습용/ 예시](01-single-table-queries.sql)

### Sorting data
ORDER BY syntax
- From clause 뒤에 위치한다.
- 하나 이상의 COl을 기준으로 결과를 
- ASC 오름차
- DESC 내림차 


테이블에서 - 조회하여 - 정렬. 

---

### Filtering data

#### Clause
- DISTINCT
  - 조회 *결과*에서 중복 레코드 제거
  - SELECT 키워드 바로 뒤, 고유한 값을 선택하려는 하나 이상의 필드 지정 ( 해당 필드는 중복 제거 )
- WHERE (*if 같은걸까?*)
  - 조회 시 특정 검색 조건을 지정
- LIMIT
  - 조회하는 레코드 수를 제한
  - 하나 또는 두개의 인자를 사용 ( 0 또는 양의 정수 )
  - row_count는 조회하는 최대 레코드 수를 지정.
  - LIMIT & OFFSET 
    - 부트스트랩 그리드시스템에서 OFFSET 봤을걸요? (상쇄)
      - 부트 / 빈칸 만들때
    - range(N, M): 같은 느낌
    - offset 은 선택사항
    - (N 칸 상쇄 후 M 칸)
    - 


#### Opertator
- BETWEEN
  - 범위
- IN
  - 값이 특정 목록 안에 있는지 확인
- LIKE
  - 값이 특정 패턴에 일치하는지 확인(Wildcards와 함께 사용)
    - '%' 0개 이상의 문자열과 일치하는지 확인
    - '_' 단일 문자와 일치하는지 확인
- Comparison
  - 
- Logical
- IS : NULL 의 친구


#### GROUP BY
레코드를 그룹화하여 요약본을 생성한다.
- 집계 함수와 함께 사용.
- 레코드를 뭔가 뭔가 합산 -> 요약본 생성

Aggregation Functions / 집계 함수
- 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수.
- FROM 과 WHERE 뒤에 배치.
- GROUP BY 절 뒤에 요약할 것 명시

### SELECT statement 순서

1. FROM 
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT 

테이블에서 - 특정 조건에 맞추어 - 그룹화 하고 - 만약 그룹중에 조건이 있다면 맞추고 - 조회하여 - 정렬하고 - 특정 위치의 값을 가져온다.

: 많은 이유 | 대체 공휴일. . . 

SQL2는 알아서 하셈 ㅋ 
