import streamlit as st

st.title("오늘은 신나는 금요일")
st.header("오늘은 Streamlit을 배워봅시다.")
st.subheader("오늘은 Streamlit을 배워봅시다.")

# st.sidebar.title("사이드바")
# st.page_link("사용자 입력 받기", "main/pages/input.py")
# st.page_link("Counter", "main/pages/session_state.py")
# st.page_link("Data", "main/pages.data.py")

site_name = st.text_input("오늘 내가 만들 사이트는?")
site_name


if st.button(f"{site_name} 접속하기"):
    # pass
    if site_name == "":
        # st.warning("사이트 이름을 입력해주세요.")
        st.error("사이트 이름을 입력해주세요.")
    else:
        st.success(f"{site_name}에 접속중", icon="☑") 
# site_name[::-1]
# if (site_name != "" and site_name == site_name[::-1]):
#     st.write("회문입니다.")
    
# print("site_name:", site_name)

"""
## _summary_
- Streamlit은 Python으로 데이터를 시각화하고 웹앱을 만들 수 있는 라이브러리입니다.
- Streamlit은 Python 코드로 작성된 웹앱을 만들 수 있습니다.
- 마크다운 문법을 사용할 수 있습니다.
- 다양한 데이터 시각화 기능을 제공합니다.
- Streamlit은 Python 코드를 자동으로 실행합니다.
- https://streamlit.io/ 여기서 더 많은 정보를 확인할 수 있습니다.
"""