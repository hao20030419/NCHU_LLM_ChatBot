import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

st.set_page_config(page_title="Qwen2.5 Chatbot", page_icon="🤖")
st.title("🤖 Qwen2.5-0.5B 中文聊天機器人")

if st.button("🔄 清除對話"):
    st.session_state.messages = []
    st.rerun()

@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-1.5B-Instruct", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        "Qwen/Qwen2.5-0.5B-Instruct",
        dtype=torch.float32,
        device_map="auto",
        trust_remote_code=True
    )
    return tokenizer, model

tokenizer, model = load_model()

if "messages" not in st.session_state:
    st.session_state.messages = []

# 顯示歷史對話
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 取得使用者輸入
if prompt := st.chat_input("請輸入你的問題"):

    # 顯示使用者輸入
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 組合對話內容（簡單上下文）
    system_prompt = "你是智慧助理，請用繁體中文回答使用者的問題。"
    dialogue = f"system: {system_prompt}\n"

    for m in st.session_state.messages[-5:]:
        dialogue += f"{m['role']}: {m['content']}\n"
    dialogue += "assistant:"

    # 生成回應
    with st.chat_message("assistant"):
        with st.spinner("Qwen 思考中..."):

            inputs = tokenizer(dialogue, return_tensors="pt")
            inputs = {k: v.to(model.device) for k, v in inputs.items()}

            outputs = model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_p=0.9
            )

            response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            reply = response.split("assistant:")[-1].strip()

            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
