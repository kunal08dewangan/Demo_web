import streamlit as st

st.title("Heyy!!")
st.subheader("I'm Kunal Dewangan !")
st.markdown("I'm Just A Developer...")
name = st.text_input("Enter your Name : ")
age = st.text_input("Enter Your Age : ")
button = st.button("Enter")
if button:
    st.markdown(f"""
    Name : {name}\n
    Age : {age}""")
