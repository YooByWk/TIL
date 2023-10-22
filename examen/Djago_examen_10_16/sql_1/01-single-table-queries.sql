-- 01. Querying data


-- 테이블 employess에서 Lastname  필드의 모든 데이터 조회
SELECT 
  LastName
-- 필드
FROM
  employees;

-- 테이블

-- 한줄로 써도 됨

-- 2.
-- 테이블 employess에서 Lastname, FirstName  필드의 모든 데이터 조회 // 다중 필드 조회
SELECT 
  LastName, FirstName
FROM
  employees;
  
-- 1- 3.
-- 모든필드 조회
SELECT 
  *
FROM
  employees;

-- 1 - 4.
-- 테이블 employess에서 Lastname  필드의 모든 데이터 조회
-- + 조회 시, FirstName 이 아닌 '이름' 으로 출력 될 수 있도록 변경
SELECT 
  FirstName AS '이름'
FROM
  employees;


-- 1-5.
                                                          
SELECT
  Name, 
  Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks;

-- 02. Sorting data

-- 데이터 정렬
-- 2-1
SELECT 
  FirstName
FROM
  employees
  --  위의 select 에서 ; 지워주고
ORDER BY -- 정렬한다는 명령어
  FirstName ASC; -- 오름차순

SELECT 
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC; -- 내림차순
-- 2 - 3 
SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC, -- 여기는 내림차로
  City ASC; -- 여기는 오름차로
-- 이 경우 country로 우선 내림차 정렬된 후, 같은 country 의 요소는 city 기준으로 오름차로 정렬된다.


SELECT
  Name, Milliseconds / 60000 AS '재생 시간(분)'
FROM
  tracks
ORDER BY
  Milliseconds DESC;



-- NULL 정렬 예시
-- NULL 값이 존재할 경우 오름차순 정렬 시 결과에 NULL이 먼저 출력
SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;


-- 03. Filtering data

-- DISTINCT : 조회결과에서 중복된 레코드를 제거 / SELECT키워드 바로 뒤에 작성해야 함 / 고유한 값을 선택하려는 하나 이상의 필드를 지정
-- DISTINCT 활용 1 : 테이블 customers에서 Country 필드의 모든 데이터를 오름차순 조회
SELECT DISTINCT -- DISTINCT : 중복없이.
  Country
FROM
  customers
ORDER BY
  Country;


-- WHERE : 조회 시 특정 검색조건을 지정 / FROM 아래에 위치 / serch_condition은 비교연산자 및 논리연산자를 사용하는 구문이 사용됨
-- WHERE 활용 1 : 테이블 customers에서 City 필드 값이 'Prague'인 데이터의 LastName, FirstName, City 조회
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City = 'Prague';


-- WHERE 활용 2 : 테이블 customers에서 City 필드 값이 'Prague'가 아닌 데이터의 LastName, FirstName, City 조회
-- WHERE : 조회 시 특정 검색 조건을 지정 
SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  City != 'Prague';


-- WHERE 활용 3 : 테이블 Customers에서 Company 필드 값이 NULL이고, Country 필드 값이
-- USA인 데이터의 Lastname, FirstName, Company, Country 조회
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL 
  AND Country = 'USA';

-- WHERE 활용 4 : Customers 테이블에서, Company 가 NULL 이거나, Country가 USA인 데이터의 
-- LastName, FirstName, Company, Country 조회.
SELECT
  LastName, FirstName, Company, Country
FROM
  customers
WHERE
  Company IS NULL 
  OR Country = 'USA';

-- WHERE 활용 5 : tracks에서 필드 값이  100000 <= Bytes <= 500000 인 데이터의 Name과 Bytes를 조회.
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  -- 100000 <= Bytes <= 500000; 이거 뭐임  ? 안되는듯.?
  Bytes BETWEEN 100000 AND 500000; -- BETWEEN을 사용합시다.


-- WHERE 활용 6 : track 테이블의 bytes가 100000, 500000 사이를 Bytes 오름차순으로 쓱싹 
SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

-- WHERE 활용 7 :  테이블 customers에서 Contry 필드 값이 'Canada' 또는 'Germany' 또는 'France'인 데이터의 LastName, FistsName, Contry 조회
-- IN : ~~ 이 들어있는?

SELECT
  LastName, FirstName, Country
FROM 
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');
  -- Country = 'Canada'
  -- OR Country = 'Germany'
  -- OR Country = 'France';


-- WHERE 활용 8 : 테이블 customers에서 Contry 필드 값이 'Canada' 또는 'Germany' 또는 'France' 가 아닌 데이터의 LastName, FistsName, Contry 조회
-- NOT IN
SELECT
  LastName, FirstName, Country
FROM 
  customers
WHERE
  Country NOT IN ('Canada', 'Germany', 'France');


-- WHERE 활용 9 : 테이블 Customers에서 LastName필드 값이 son으로 끝나는 데이터의 LastName, FirstName 조회
-- son 으로 끝나는 // 일부분 일치값 : LIKE
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName LIKE '%son';


-- WHERE 활용 10 : 테이블 Customers에서 LastName필드 값이 4자리면서 'a'로 끝나는 데이터의 LastName, FirstName 조회
-- 와일드카드? : _ _ _ 3개 + a // 빈 문자 3개 + 마지막은 a 
-- 조금 더 자세한 조건으로 추정된다.
SELECT
  LastName, FirstName
FROM
  customers
WHERE
  FirstName LIKE '___a';


-- LIMIT : 하나 또는 두개의 인자를 사용 ( 0또는 양의 정수) / row_count는 조회하는 최대 레코드 수를 지정
-- LIMIT 활용 1 : 테이블 track에서 Trackld, Name, Bytes 필드 데이터를 Bytes기준 내림차순으로 7개만 조회
-- 조회, 정렬, 제한
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 7;

-- LIMIT 활용 2 : 테이블 track에서 Trackld, Name, Bytes 필드 데이터를 Bytes기준 4번째 부터 7번째 데이터만 내림차순으로 조회
-- 3개 상쇄, 4개를 출력. DESC (내림차순)
SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY
  Bytes DESC
LIMIT 3, 4;
-- LIMIT 4 OFFSET 3; --명시적 표현 // 가능함


-- 04. Grouping data
-- GROUP BY : 레코드를 그룹화하여 요약본 생성 (집계함수 와 함께 사용) / From 및 Where 절 뒤에 배치 / Group by 절 뒤에 그룹화 할 필드 목록 작성

-- 예시
SELECT
  Country, COUNT(*) -- count : 집계함수 사용!! // 그룹화 된 기준으로 count 하겠다
FROM
  customers
GROUP BY
  Country;


-- GROUP BY 활용 1 : 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Bytes의 평균 값을 내림차순 조회
-- tracks에서 작곡가 필드 그룹화 후 bytes의 평균을 내림차순으로 조회.
-- ORDER BY 에서 이름 SELECT에서 바꾼? 것으로 잘 써주기
SELECT
  Composer, AVG(Bytes)
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Bytes) DESC;


-- GROUP BY 활용 2 : 테이블 tracks에서 Composer 필드를 그룹화하여 각 그룹에 대한 Milliseconds의 평균 값이 10미만인 데이터 조회
-- (단, Milliseconds 필드는 60000으로 나눠 분 단위 평균으로 계산)

-- 에러 ( group by 와 where을 같이 쓸 때 나타남)
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
WHERE
  avgOfMinute < 10
GROUP BY
  Composer;


-- 에러 해결
-- 집계에 관한 것은 where을 사용할 수 없다.
-- 일반적인 조건이 아니므로... 
-- 그래서 Having을 사용한다. 하지만 Having의 경우 만약 Group by가 없다면 where처럼 동작한다.
SELECT
  Composer,
  AVG(Milliseconds / 60000) AS avgOfMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  avgOfMinute < 10;
