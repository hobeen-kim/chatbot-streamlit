import streamlit as st
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

st.title("안녕하세요")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            'role': "assistant",
            'content': "무엇을 도와드릴까요?"}]

for msg in st.session_state.messages:
    st.chat_message(msg['role']).write(msg['content'])

chat = ChatOpenAI(model="gpt-4o-mini", temperature=1)

if prompt := st.chat_input():
    st.session_state.messages.append({
        'role': "user",
        'content': prompt
    })

    st.chat_message("user").write(prompt)
    response = chat.invoke(prompt)
    msg = response.content

    st.session_state.messages.append({
        'role': "assistant",
        'content': msg
    })

    st.chat_message("assistant").write(msg)
