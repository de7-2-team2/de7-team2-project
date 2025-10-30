# 🌾 프로젝트 주제
GAP 농산물 우수관리(GAP) 인증정보 대시보드
- 주제 개요
   - GAP(Good Agricultural Practices)인증은 농산물의 안정성과 지속가능한 농업 실현을 위한 국가 인증 제도입니다.

- 목표
   - 분산된 농산물 인증 데이터를 자동화된 파이프라인으로 수정, 적재
   - AWS 환경에서 데이터 웨어하우스(Redshift) 구축
   - Superset을 통해 비개발자도 이해할 수 있는 시각화 대시보드 제공

## 🎯 프로젝트 소개
- 주제 선정 배경
   - 농산물의 안정성과 신뢰도에 대한 사회적 관심 증가
   - 공공데이터를 활용한 데이터 기반 의사결정 지원 사례 확대
   - 정부의 스마트 농업 및 데이터 기반 행정 정책관의 연계

- 개발 환경
<img width="697" height="297" alt="image" src="https://github.com/user-attachments/assets/94319319-0fcf-44ee-9269-81d13f3b25c6" />

- 시스템 구조</br>
<img width="775" height="430" alt="image" src="https://github.com/user-attachments/assets/7e46079e-f708-45ee-a82d-620064079f79" />

- 데이터 소스(원본 데이터)
   - 농산물우수관리(GAP) 인증농가 현황
      - https://data.mafra.go.kr/opendata/data/indexOpenDataDetail.do

## ⚙️ 실행 순서
### 1. 데이터 정제
- 파일: data/gap.py
- 역할: 연도별 GAP CSV 파일 병합 및 컬럼 정제
- python data/gap.py

### 2. S3 업로드
- 파일: redshift/upload_to_s3.py
- 역할: 통합 CSV(combined_gap_data.csv) → S3 버킷 업로드
- python redshift/upload_to_s3.py

### 3. Redshift 적재
- 파일: redshift/load_data.py
- 역할: S3 → Redshift 데이터 적재 (COPY 명령어 사용)
- python redshift/load_data.py

### 4. Superset 시각화
- 데이터베이스 연결: Redshift
- 데이터셋: raw_data.farm, raw_data.item

## 주요 차트:
- 품목별 인증 농가 수 (막대그래프)
- 지역별 농가 분포 (가로 막대그래프)
- 연도별 인증 추이 (라인차트)
- 품목별 생산량 비율 (도넛/파이차트)

## 💻 기술 스택
   | 분류 | 사용 기술 |
   |------|------------|
   | 데이터 정제 | Python (pandas, Jupyter Notebook) |
   | 클라우드 스토리지 | AWS S3 |
   | 데이터 웨어하우스 | Amazon Redshift Serverless |
   | 시각화 도구 | Apache Superset / Preset Cloud |
   | 협업 및 버전관리 | GitHub, Notion |
