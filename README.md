# LLM Chatbot Demo（Streamlit 雲端部署版）

本專案展示一個基於大型語言模型（LLM）的即時聊天機器人，建置於 Streamlit 平台，提供使用者透過瀏覽器與語言模型進行自然語言互動。專案原先以 Qwen2.5-1.5B-Instruct 為目標模型進行實作，惟因雲端平台記憶體限制，最終以超小模型完成線上部署，並保留完整系統架構以利未來升級為較大模型。

---

## 專題目標

- 建立可即時互動的 AI 聊天系統  
- 實作生成式 AI 模型部署流程  
- 探討模型效能與雲端資源之取捨  
- 實踐 Prompt Engineering 與多輪對話設計  

---

## 技術架構

使用技術：

- Python  
- Streamlit  
- HuggingFace Transformers  
- PyTorch  


系統流程：
- 使用者 → Streamlit UI → Qwen2.5 LLM → 回傳結果

## 模型說明

本系統最初選用 Qwen2.5-1.5B-Instruct 作為設計模型，以測試中大型語言模型於實務部署之可行性；然由於 Streamlit Cloud 免費方案之記憶體限制，最終改以超小模型（如 distilgpt2）完成線上部署，確保系統可穩定啟動與展示。

此過程突顯：
> 模型效能、系統穩定性與部署環境間之取捨關係。


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