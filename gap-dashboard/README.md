# 🌾 GAP 농산물 우수관리(GAP) 인증정보 대시보드
: 공공데이터 기반으로 **GAP(농산물우수관리)** 인증 농가 및 품목 현황을 시각화한 AWS 데이터 웨어하우스 프로젝트입니다.
---

## 🎯 프로젝트 개요
**GAP(Good Agricultural Practices)** 인증은 농산물의 안전성과 지속가능성을 확보하기 위한 국가 인증 제도입니다. 본 프로젝트는 공공데이터포털에서 제공하는 GAP 인증 농가 데이터를 정제 → AWS Redshift에 적재 → Superset으로 시각화하는 파이프라인 구축을 목표로 합니다.
---

## 🧱 시스템 구조
   공공데이터 (CSV)
      ↓
   Python(pandas) 데이터 정제
      ↓
   AWS S3 업로드
      ↓
   Amazon Redshift 적재 (COPY)
      ↓
   Superset / Preset 시각화
---

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
---

## 주요 차트:
- 품목별 인증 농가 수 (막대그래프)
- 지역별 농가 분포 (가로 막대그래프)
- 연도별 인증 추이 (라인차트)
- 품목별 생산량 비율 (도넛/파이차트)
---

## 💻 기술 스택
   | 분류 | 사용 기술 |
   |------|------------|
   | 데이터 정제 | Python (pandas, Jupyter Notebook) |
   | 클라우드 스토리지 | AWS S3 |
   | 데이터 웨어하우스 | Amazon Redshift Serverless |
   | 시각화 도구 | Apache Superset / Preset Cloud |
   | 협업 및 버전관리 | GitHub, Notion |
---
