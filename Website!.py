import streamlit as st

st.title("Heyy!!")
st.subheader("I'm Kunal Dewangan !")
st.markdown("I'm Just A Developer...")
# st.set_page_config(
#     # page_icon = "M.png"
#     page_title = "KD 1st"
# )
st.title("Enter Your Personal Details :-")
name = st.text_input("Enter your Name : ")
age = st.text_input("Enter Your Age : ")
univer = st.text_input("Enter Your University Name : ")
button = st.button("Enter")
if button:
    st.markdown(f"""
    Name : {name}\n
    Age : {age}
    University : {univer} """)
    a = int(input("Enter a No. For their Table : "))
    table(a)

def table(a):
    for i in a:
        print(f"{a} X {i} : {a*i}")
