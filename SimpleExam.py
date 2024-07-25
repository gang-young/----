import streamlit as st
from datetime import datetime


def home():
    st.title('간단한 퀴즈를 풀어보세요!')
    st.write("초등학생도 풀 수 있는 쉬운 퀴즈입니다!.")
    
    

    st.image('https://img.freepik.com/premium-vector/quiz-logo-with-speech-bubble-icon_149152-811.jpg', use_column_width=True)
    
if __name__ == "__main__":
    home()

text = st.text_input("이름을 입력해주세요!")
if st.button("시험 시작!") :
    st.session_state.text = text
    st.switch_page("pages/1_객관식.py")

