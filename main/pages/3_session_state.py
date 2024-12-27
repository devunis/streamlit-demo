import streamlit as st

st.title("Counter")

if "customer_count" not in st.session_state:
    st.session_state.customer_count = 0

add_guest = st.button("손님 추가요~!")
if add_guest:
    st.session_state.customer_count += 1

f"지금까지 온 손님 수: {st.session_state.customer_count}"

if st.button("오늘 장사 끝! 손님 수 초기화"):
    if st.session_state.customer_count == 0:
        st.error("손님 없이 장사 끝내시겠어요? 망했다...")
    else:
        st.success(f"장사 끝! 오늘 총 손님 수: {st.session_state.customer_count}")
        st.balloons()
    st.session_state.customer_count = 0