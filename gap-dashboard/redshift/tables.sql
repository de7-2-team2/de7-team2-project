CREATE SCHEMA IF NOT EXISTS raw_data;

-- 품목 테이블
CREATE TABLE IF NOT EXISTS raw_data.item (
    id INT IDENTITY(1,1) PRIMARY KEY,
    i_name VARCHAR(100) UNIQUE NOT NULL   -- 품목명
);

-- GAP 인증 농가 테이블
CREATE TABLE IF NOT EXISTS raw_data.farm (
    id INT IDENTITY(1,1) PRIMARY KEY,
    gap_cert_no VARCHAR(50) NOT NULL,     -- GAP 인증번호
    cert_org VARCHAR(100),                -- 인증기관명
    type_name VARCHAR(20),                -- 개인 / 단체 구분
    valid_start DATE,                     -- 유효기간 시작일
    valid_end DATE,                       -- 유효기간 종료일
    item_id INT REFERENCES raw_data.item(id),  -- 품목 외래키
    address_name VARCHAR(255),                 -- 전체 주소
    region_name VARCHAR(100),             -- 시도명
    city_name VARCHAR(100),               -- 시군구명
    town_name VARCHAR(100),               -- 읍면동명
    farm_count INT,                       -- 등록 농가수
    field_count INT,                      -- 등록 필지수
    area FLOAT,                           -- 재배면적
    planned_production FLOAT,             -- 생산계획량
    designation_date DATE,                -- 지정일자
    valid BOOLEAN DEFAULT TRUE            -- 인증 유효 여부
);
