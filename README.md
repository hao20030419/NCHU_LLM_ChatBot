# LLM Chatbot Demo (Qwen2.5-1.5B)

本專案展示一個基於大型語言模型（LLM）的即時聊天機器人，使用 Qwen2.5-1.5B-Instruct 作為核心模型，並透過 Streamlit 建立可互動之網頁介面，提供自然語言對話展示。

---

## 專題目標
- 建立可即時互動的 AI 聊天系統
- 實作生成式 AI 模型部署流程
- 理解 Prompt Engineering 與多輪對話設計

---

## 技術架構

使用技術：
- Python
- Streamlit
- HuggingFace Transformers
- Qwen2.5-1.5B-Instruct
- Torch / Accelerate

系統流程：
- 使用者 → Streamlit UI → Qwen2.5 LLM → 回傳結果

## 安裝方式
安裝必要套件：
```cmd
pip install -r requirements.txt
```

## 執行方式

啟動系統：
```cmd
streamlit run app.py
```


## 功能特色

- ✅ 支援中文自然語言對話
- ✅ 多輪對話上下文處理
- ✅ Prompt 設定助教角色
- ✅ 清除對話按鈕
- ✅ 可部署於雲端平台

## 參考資料
- HuggingFace Transformers
- Streamlit 官方文件
- Qwen 模型說明文件