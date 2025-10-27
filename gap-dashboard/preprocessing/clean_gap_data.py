import pandas as pd
import os

file_names = ['2020.csv', '2021.csv', '2022.csv', '2023.csv', '2024.csv', '2025.csv']
data_frames = []
all_columns = []

# 인코딩 및 컬럼 불일치 문제 해결을 위한 반복 처리
for file in file_names:
    print(f"Reading file: {file}")
    try:
        # 한국어 CSV에서 발생하는 인코딩 오류 해결을 위해 'utf-8' 인코딩을 사용
        # (만약 utf-8로도 깨짐이 발생한다면 'cp949'를 시도해볼 수 있습니다.)
        df = pd.read_csv(file, encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file} with utf-8. Trying cp949: {e}")
        try:
            df = pd.read_csv(file, encoding='cp949')
        except Exception as e:
            print(f"Error reading {file} with cp949: {e}. Skipping file.")
            continue

    # 컬럼 이름 정제 (공백 제거)
    df.columns = df.columns.str.strip()

    # '2020.csv'에는 '생산자단체명' 컬럼이 추가되어 있어, 이를 제거하여 다른 파일들과 컬럼을 맞춥니다.
    if '생산자단체명' in df.columns:
        df = df.drop(columns=['생산자단체명'])

    # '2021.csv'에는 '개인_단체 구분명' 컬럼이 있어, 이를 '개인/단체 구분명'으로 통일합니다.
    if '개인_단체 구분명' in df.columns:
        df = df.rename(columns={'개인_단체 구분명': '개인/단체 구분명'})

    # 최종 컬럼 리스트 정의 및 데이터프레임 리스트에 추가
    if len(all_columns) == 0:
        all_columns = list(df.columns)
    
    # 컬럼 순서 재배열 및 없는 컬럼은 NaN으로 채우기
    df = df.reindex(columns=all_columns)

    data_frames.append(df)

# 모든 데이터프레임을 하나로 합치기
if data_frames:
    combined_df = pd.concat(data_frames, ignore_index=True)

    # 합쳐진 파일 저장 (엑셀 등에서 한글 깨짐 방지를 위해 'utf-8-sig' 인코딩 사용)
    output_file_name = 'combined_gap_data.csv'
    combined_df.to_csv(output_file_name, index=False, encoding='utf-8-sig')

    print(f"\n총 {len(combined_df)} 행의 데이터가 {output_file_name} 파일로 저장되었습니다.")
else:
    print("처리된 데이터가 없습니다. 파일 경로 및 인코딩을 확인해 주세요.")