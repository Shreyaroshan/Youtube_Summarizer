# 🎥 YouTube Summarizer with LLaMA 3 & Streamlit

An interactive web app that summarizes YouTube videos by fetching transcripts and generating concise bullet-point summaries using a locally hosted **LLaMA 3** model via **Ollama**. Built with **Streamlit** for a seamless user interface and enhanced with Lottie animations.

---

## 🚀 Features

* ✅ Fetches transcript of YouTube videos automatically
* ✅ Generates AI-powered bullet-point summaries using **LLaMA 3 (local)**
* ✅ Interactive web interface with tabs, sidebar, and animations
* ✅ Works fully offline with local Ollama LLM integration
* ✅ Helps users preview content before watching, especially useful with **500+ similar videos per topic** on YouTube

---

## 🛠️ Tech Stack

* **Frontend & UI:** Streamlit, Streamlit-Lottie
* **Backend & Logic:** Python, YouTube Transcript API, Ollama (LLaMA 3 Model)
* **Deployment:** Runs locally as a Streamlit app

---

## 📝 How to Run

1️⃣ **Clone the Repository**

```bash
git clone https://github.com/your-username/youtube-summarizer.git
cd youtube-summarizer
```

2️⃣ **Set up Virtual Environment & Install Requirements**

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

3️⃣ **Install & Run Ollama (for LLaMA 3)**

* Download & Install [Ollama](https://ollama.com/)
* Pull the LLaMA 3 model

```bash
ollama pull llama3
```

* Keep Ollama running in background

4️⃣ **Run the Streamlit App**

```bash
streamlit run summarizer_app.py
```

---

## 🎨 Customization

* Modify `.streamlit/config.toml` for custom themes
* Replace Lottie animation URLs with your choice from [LottieFiles](https://lottiefiles.com/)

---

## 📄 Sample Output

> **Input:** YouTube Video URL
>
> **Output:**

```
- Summary point 1
- Summary point 2
- Summary point 3
```


