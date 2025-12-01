import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Mini LLM Chatbot", page_icon="🤖")
st.title("🤖 Mini LLM Chatbot（Streamlit Safe Mode）")

# 載入超小模型
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

generator = load_model()

# 初始化對話狀態
if "messages" not in st.session_state:
    st.session_state.messages = []

# 清除對話
if st.button("🔄 清除對話"):
    st.session_state.messages = []
    st.rerun()

# 顯示歷史對話
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 使用者輸入
if prompt := st.chat_input("請輸入你的問題"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 系統提示
    system_prompt = "You are a helpful AI assistant."

    input_text = system_prompt + "\nUser: " + prompt + "\nAssistant:"

    with st.chat_message("assistant"):
        with st.spinner("AI 回應中..."):
            result = generator(input_text, max_length=120, num_return_sequences=1)
            reply = result[0]["generated_text"].split("Assistant:")[-1].strip()
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})