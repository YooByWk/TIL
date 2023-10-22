# 2023_10_22 domingo

## prep. el examen
## de 09_oct_23 a 22_oct_23

# 10월


## 10일 화 : SQL
오전
> 22 관계형 DB  + PK // FK  
>
> DQL 데이터 검색. SELECT
> 
> Table / Field / Record / Database-Schema / primary key(PK) / Foreign Key(FK)  
> R(elatioanal)+DBM(management)S(system)   // join(결합)   
> SQL - DB 저장, 처리 언어 '명령어 대문자 **권장**' // '*' 모든 필드  
> SELECT /// + DISTINCT (고유한 값/ 중복없이)  
> FROM  
> ORDER BY col ASC(오름차) / DESC(내림차) // 오름차-NULL이 최상위   
> 위 세개 실행순서 : FROM -> SELECT -> ORDER BY  
> WHERE (IF) / NULL 은 IS NULL 로 부름 / 구간은 ' smth BETWEEN a AND b; / IN : ~~인 것 (a OR b OR c) 정도? / %son = son으로 끝나는 / '_ _ _ K' : _ 칸 + K 끝 /   
> ORDER BY 보다 선행함 // 정렬은 마지막에 하고, 거기서 슬라이싱한다고 생각하자.    
>  아무튼 실행 순서
>> FROM  (+ join)- WHERE -  GROUP BY - HAVING - SELECT - ORDER BY - LIMIT  
> 작성순서
>> SELECT - FROM - WHERE-   GROUP - HAVING - ORDER - LIMIT

---
오후
> 살려조

> DDL 데이터 구조 및 형식 변경 CREATE DROP ALTER  
> CREATE TABLE : 테이블 생성   
>> 데이터 타입 : NULL / INTEGER / REAL / TEXT / BLOB  
>> **제약조건** : PK, NOT NULL, FK // AUTOINCREMENT 필드 자동 증가 키워드
>> INTEGER PRIMARY KEY AUTOINCREMENT 얘랑 친함 

> ALTER TABLE : 테이블  필드 조작 ..  
> ALTER TABLE ADD COL :   필드 추가  
> ALTER TABLE RENAME COL  : 필드 이름 변경  
> ALTER TABLE REMOVE COL  : 필드 삭제    
> ALTER TABLE RENAME TO  : 테이블 이름 변경    
> ALTER TABLE table_name ADD COLUMN column_def  
> ex : ALTER TABLE examples ADD COLUMN Country VARCHAR(100) NOT NULL;
> <br>
> sqlite - 한번에 여러필드 추가 X
>

> DROP TABLE : 삭 제  
> DROP TABLE table_name; 삭제당함
>

> 타입 선호도 : 유연한 데이터 타입 지원 / 간편 데이터 처리 / SQL 호환
> NOT NULL 제약은 필수가 아님, 하지만 프로그램에 따라 NULL 을 저장할 필요가 없는 경우가 많아 NOT NULL을 정의함, 값이 없다 라는 표현을 테이블에 기록하는 것은  0 이나  빈 문자열등을 사용하는것으로 대체하는 것을 권장

> DML
> INSERT : 테이블 레코드 삽입  
> INSERT INTO tablename c1 c2 c3  VALUES v1 v2 v3   
>
> UPDATE : 레코드 수정 / WHERE 안쓰면 모든 레코드 수정  
> DELETE : ㅇㅇ   / WHERE 안쓰면 모든 레코드 삭제  
>

>  MTq...
> 
>  JOIN  
> JOIN 두개 이상에서 뭔가 뭔가 보기 
>
> INNER JOIN 일치하는 레코드만  
> SELECT ... FROM ... INNER JOIN ... ON ... 
>
> LEFT JOIN   : 오른쪽 테이블 일치 / 왼쪽 모든 레코드   역참조 용인가?
> 
> SELECT ... FROM ... LEFT JOIN ... ON ... 
## 11일 수 : N: 1 (1)

## 12일 목 : N : 1 (2)
3
## 13일 금 : PJT
4
## 16일 월 : N : M 1 
5
## 17일 화 : N : M 2
6
## 18일 수 : DRF
7
## 19일 목 : DRF 
8
## 20일 금 : PJT
9