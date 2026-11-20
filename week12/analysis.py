import pandas as pd


def 정제(df):
    정제된_df = df.copy()

    # 점수가 비어 있는 행을 삭제한다.
    정제된_df = 정제된_df.dropna(subset=["점수"])
    print("빈 점수 삭제 후:", len(정제된_df), "행")

    # 모든 열의 값이 같은 중복 행을 삭제한다.
    정제된_df = 정제된_df.drop_duplicates()
    print("중복 행 삭제 후:", len(정제된_df), "행")

    # 반과 과목 값의 앞뒤 공백을 제거한다.
    정제된_df["반"] = 정제된_df["반"].str.strip()
    정제된_df["과목"] = 정제된_df["과목"].str.strip()
    print("공백 제거 후:", len(정제된_df), "행")

    # 점수가 0~100 범위를 벗어난 행을 삭제한다.
    정제된_df = 정제된_df[정제된_df["점수"].between(0, 100)]
    print("점수 범위 확인 후:", len(정제된_df), "행")

    return 정제된_df


df = 정제(pd.read_csv("scores_2026.csv"))
print(sorted(df["반"].unique()))
print(sorted(df["과목"].unique()))

# 필터링 (프롬프트 B)
수학 = df[df["과목"] == "수학"]
print(len(수학))

반1_90점이상 = df[(df["반"] == "1반") & (df["점수"] >= 90)]
print(len(반1_90점이상))

# 그룹화 (프롬프트 C)
반별_평균 = df.groupby("반")["점수"].mean()
print(반별_평균)

과목반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목반별_평균)

# 과목 × 반 인원 수 확인 (학습지 ④ 표의 명 수)
print(df.groupby(["과목", "반"])["점수"].count())


# 통계 (프롬프트 D)
def 반별평균(df):
    표 = (
        df.groupby("반")["점수"]
        .agg(["count", "mean", "median", "max"])
        .rename(columns={
            "count": "개수",
            "mean": "평균",
            "median": "중앙값",
            "max": "최댓값",
        })
        .round(2)
    )
    print(표)
    return 표["평균"]


반별평균(df)

# 반환값에서 1반 꺼내기 확인
print(반별평균(df)["1반"])

# 검증 ② 합계 일치 — 그룹으로 나눠도 총합은 변하지 않아야 한다
print(df.groupby("반")["점수"].sum().sum())
print(df["점수"].sum())

print(df.groupby("반")["점수"].count().sum())
print(len(df))

# 검증 ④ 스팟 체크 — 1반 · 수학 점수를 직접 확인
print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"])

# 미니 데이터 — 손계산과 비교
미니 = 정제(pd.read_csv("mini.csv"))
print(반별평균(미니))
