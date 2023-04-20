import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/my_photo.png', width=300)

with col2:
    st.title('Eugene Kosinov')
    content = """Hi, I`m Eugene! I am a beginner Python programmer and student. I am a cybersecurity specialist 
    studying unix systems and I am fond of information security. I study in the city of Kyiv at the National Aviation 
    University. I'm trying to find myself and develop as many useful skills as possible and Python programming is one 
    of them.
    """
    st.info(content)
