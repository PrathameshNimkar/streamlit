import streamlit as st

st.header('Let us try using a Streamlit Button')

if st.button('Say Hello!'):
    st.write("Why hello there")
else:
    st.write("Good Bye")
