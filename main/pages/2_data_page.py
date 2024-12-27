import streamlit as st
import pandas as pd

st.title("게임 캐릭터의 인지도")

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

df = pd.DataFrame({
    '캐릭터': ['전사', '법사', '힐러', '탱커', "랜덤"],
    '선택횟수': [100, 80, 60, 40, 20],
    "승률 (%)": [50, 40, 30, 20, 10],
    "인지도 (%)": [30, 20, 10, 5, 3]
    })

# st.write(df)
# st.line_chart(df)

st.dataframe(df, use_container_width=True)
# edited_data = st.data_editor(df)
# edited_data

st.bar_chart(df.set_index("캐릭터")["선택횟수"])
st.line_chart(df.set_index("캐릭터")["승률 (%)"])

# st.pie_chart(df)
fig = df.plot.pie(
    y="인지도 (%)", # 파이 차트의 값
    labels=df["캐릭터"], # 파이 차트의 라벨
    autopct="%1.1f%%", # 비율을 표시할 형식
    figsize=(6, 6), # 파이 차트의 크기
    legend=False, # 범례 표시 여부
    title="캐릭터 별 인지도", # 파이 차트의 제목
).get_figure()

st.pyplot(fig)