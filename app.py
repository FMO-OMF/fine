import streamlit as st
st.title("my first app")
st.write("Hello")
name = st.text_input("name?")
if st.button("HELLO"):
    st.success(f"안녕하세요{name}님")

