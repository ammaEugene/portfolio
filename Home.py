import streamlit as st
import pandas as pn

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/20.png', width=300)

with col2:
    st.title('Eugene')
    content = """Hi, I`m Eugene! I am a beginner Python programmer and student. I am a cybersecurity specialist 
    studying unix systems and I am fond of information security. I study in the city of Kyiv at the National Aviation 
    University. I'm trying to find myself and develop as many useful skills as possible and Python programming is one 
    of them.
    """
    st.info(content)

st.write('Below you can find some of the apps I have built in Python.'
         ' Feel free to contact me!')

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pn.read_csv('data.csv', sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')
