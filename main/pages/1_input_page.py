import streamlit as st

st.title("사용자 입력 받기")

col1, col2 = st.columns(2)

with col1:
    nickname = st.text_input("닉네임을 입력하세요.")
    # password = st.text_input("비밀번호를 입력하세요.", hidden=True)
    age = st.number_input("나이를 입력하세요.", min_value=13, max_value=80)
    selected = st.selectbox("학교 입력", ["초등학생", "중학생", "고등학생", "대학생",])
    r_options = ["맛집 탐방", "영화 감상", "음악 감상", "사진찍기"]
    choice = st.radio("취미를 선택하세요.", r_options)
    selected_many = st.multiselect("취미가 여러개라면", r_options)
    checked = st.checkbox("개인정보 제공 동의")
    input_button = st.button("입력 완료!")

with col2:
    if input_button:
        st.write(f"이름이 뭐예요? {nickname}")
        st.write(f"연세가 어떻게 되세요? {age}")
        st.write(f"어디 다니세요? {selected}")
        st.write(f"취미가 뭐예요? {choice}")
        st.write(f"취미가 여러개? {selected_many}")
        st.write(f"개인정보 제공 여부에 {'동의함' if checked else '동의안함'}")
        
        
tab1, tab2 = st.tabs(["탭1", "탭2"])

with tab1:
    st.write("탭1 내용")
with tab2:
    st.write("탭2 내용")














