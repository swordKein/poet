from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import streamlit as st 
import time
load_dotenv()
#from langchain_openai import OpenAI
#llm=OpenAI()
#result = llm.invoke("내가 좋아하는 동물은 ")
#print (result)


#from langchain.chat_models import init_chat_model
#from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
#chat_model.predict("hi!")
#content = "인생 노을 슬픔 희망"
#result = chat_model.invoke(content + "에 대한 시를 써줘")
#print (result)


st.title("AI 시인 - T1")
st.title("_Streamlit_ is :blue[cool] :sunglasses:")

content = st.text_input("시의 주제를 제시 해 주세요.")
st.write("시의 주제는", content)

#print (result.content)

if st.button("시 작성 요청하기"):
    with st.spinner("시 작성 중...", show_time=True):
        result = chat_model.invoke(content + "에 대한 시를 써줘")
        st.write(result.content)