import streamlit as st
import numpy as np
import pandas as pd

st.header("This is a header")
st.subheader("This is a subheader")
st.title("Title : Streamlit Example ")
st.write("Here's our first attempt at using data to create a table:")

"hello, world! with not st.write"

"**bold text**"

# seoul map
df = st.dataframe(data = {
    'latitude': [37.5665],
    'longitude': [126.9780]
    })
# df = pd.DataFrame({
#     'latitude': [37.5665],
#     'longitude': [126.9780]
#     })
st.map(df)

# make a flying donut chart
st.write("Here's a donut chart:")
chart_data = pd.DataFrame(
    np.random.randn(5, 2),
    columns=['a', 'b'])
st.write(chart_data)
st.line_chart(chart_data)

st.caption("This is a caption")

# st.balloons()
st.snow()

# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text(f"{i}% complete")
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

# progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Rerun")