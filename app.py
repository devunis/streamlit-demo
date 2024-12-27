import streamlit as st
import pandas as pd

st.title("강의실 자리 배치도")
st.write("강의실 자리 배치도입니다.")

class_name = st.text_input("반 이름", placeholder="반 이름을 입력하세요.")
if class_name:
    st.write(f"{class_name}반 여러분 안녕~")

col1, col2, col3 = st.columns(3)

data = [
    "빈자리 내자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리".split(),
    "빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리".split(),
    "빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리 빈자리".split(),
]

# Initialization
try:
    with open("/csv/seats.csv", "r") as f:
        data = [x.strip().split(",") for x in f.readlines()]
except FileNotFoundError:
    st.error("불러오기 실패")
else:
    st.success("불러오기 성공")

df1 = pd.DataFrame([x[:4] for x in data])
df2 = pd.DataFrame([x[4:8] for x in data])
df3 = pd.DataFrame([x[8:] for x in data])

with col1:    
    editor1 = st.data_editor(df1, hide_index=True, key="df1")
with col2:
    editor2 = st.data_editor(df2, hide_index=True, key="df2")
with col3:
    editor3 = st.data_editor(df3, hide_index=True, key="df3")
        
if st.button("자리 배치도 업데이트"):
    data = []
    data.append(editor1.values.tolist()[0] + editor2.values.tolist()[0] + editor3.values.tolist()[0])
    data.append(editor1.values.tolist()[1] + editor2.values.tolist()[1] + editor3.values.tolist()[1])
    data.append(editor1.values.tolist()[2] + editor2.values.tolist()[2] + editor3.values.tolist()[2])
    # export with csv
    with open("/csv/seats.csv", "w") as f:
        for line in data:
            f.write(",".join(line) + "\n")

    st.session_state['data'] = data
    st.success("자리 배치도가 업데이트 되었습니다.")

try:
    with open("/csv/attendance.csv", "r") as f:
        df = pd.read_csv(f)
except FileNotFoundError:
    st.error("불러오기 실패")
    # 출석률 : 총원, 출석인원, 결석인원, 출석률
    df = pd.DataFrame({
        '날짜': ['2024-12-18', '2024-12-19', '2024-12-20', '2024-12-23', '2024-12-24', '2024-12-26', '2024-12-27'],
        '총원': [22, 22, 22, 22, 22, 22, 22],
        '출석인원': [15, 17, 16, 18, 20, 19, 20],
        '결석인원': [4, 0, 2, 0, 0, 0, 0],
        '조퇴인원': [2, 3, 1, 1, 1, 2, 1],
        '지각인원': [1, 2, 3, 3, 1, 1, 1],
    })
else:
    st.success("불러오기 성공")

# 출석률 계산
df["출석률"] = df["출석인원"] / df["총원"] * 100

st.dataframe(df, use_container_width=True)
st.line_chart(df.set_index("날짜")[['출석인원', '결석인원', '조퇴인원', '지각인원']])

with open("/csv/attendance.csv", "w") as f:
    f.write("날짜,총원,출석인원,결석인원,조퇴인원,지각인원,출석률\n")
    for line in df.values:
        f.write(",".join(map(str, line)) + "\n")
# 분단, 자리, 날짜, 이름, 출석여부
