CREATE TABLE examples ( 
-- examples 테이블 생성
ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
LastName VARCHAR(50) NOT NULL,
FirstName VARCHAR(50) NOT NULL
);
PRAGMA table_info('examples');
-- 테이블 스키마(구조) 확인

-- ALTER TABLE ADD COLUMN  -- 필드 추가 
-- ALTER TABLE RENAME COLUMN -- 필드 이름 변경
-- ALTER TABLE DROP COLUMN -- 필드 삭제
-- ALTER TABLE RENAME TO -- 테이블 이름 변경
----------------------------------------
-- 필드 만들기
-- ADD COLUMN 키워드 이후 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약조건 작성
ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL;
  -- Country라는 100자 제한을 가진 필드 생성
  ----------------------------------------
-- RENAME
-- 단일문을 사용하여 한번에 여러 필드를 추가할 수 없다.
ALTER TABLE examples
RENAME COLUMN Country TO pais;