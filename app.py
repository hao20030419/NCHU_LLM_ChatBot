import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(page_title="Qwen Chatbot", page_icon="🤖")
st.title("🤖 Qwen2.5 Chatbot (Cloud Safe Mode)")

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-0.5B-Instruct",
        dtype=torch.float32,
        trust_remote_code=True
    )
    model.eval()
    return tokenizer, model

tokenizer, model = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("🔄 清除對話"):
    st.session_state.messages = []
    st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("請輸入你的問題"):

    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    system_prompt = "你是一位智慧助理，請用繁體中文回答使用者的問題。"

    dialogue = f"system: {system_prompt}\n"
    for m in st.session_state.messages[-5:]:
        dialogue += f"{m['role']}: {m['content']}\n"
    dialogue += "assistant:"

    with st.chat_message("assistant"):
        with st.spinner("Qwen 回應中..."):
            inputs = tokenizer(dialogue, return_tensors="pt", truncation=True)
            outputs = model.generate(
                inputs["input_ids"],
                max_new_tokens=128,
                temperature=0.7,
                top_p=0.9,
                do_sample=True
            )
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            reply = response.split("assistant:")[-1].strip()
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
