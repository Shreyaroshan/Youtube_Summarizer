import streamlit as st
from streamlit_lottie import st_lottie
import requests
from youtube_transcript_api import YouTubeTranscriptApi
import ollama

# Set Streamlit page config
st.set_page_config(page_title="Smart Summarizer", layout="wide")

# Function to load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to extract YouTube video ID
def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

# Function to fetch YouTube transcript
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([item['text'] for item in transcript])

# Function to summarize using Ollama + LLaMA 3
def get_summary_with_ollama(text):
    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "system", "content": "Summarize the following YouTube transcript in bullet points."},
            {"role": "user", "content": text}
        ]
    )
    return response['message']['content']

# Load Lottie animation
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_bdlrkrqv.json"
lottie_animation = load_lottieurl(lottie_url)





# Sidebar Navigation
st.sidebar.title("🔖 Menu")
option = st.sidebar.radio("Go to", ["Summarizer", "About"])

# Summarizer Page
if option == "Summarizer":
    st.title("🎥 YouTube Summarizer")
    st_lottie(lottie_animation, height=250)
    url = st.text_input("Enter YouTube Video URL:")
    if st.button("Summarize"):
        video_id = get_video_id(url)
        if video_id:
            try:
                with st.spinner("Fetching transcript and summarizing with LLaMA 3..."):
                    transcript = get_transcript(video_id)
                    summary = get_summary_with_ollama(transcript)
                    st.subheader("🔎 Summary:")
                    st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("❗ Invalid YouTube URL")

# About Page
elif option == "About":
    st.title("ℹ️ About This App")
    st.write("""
        This is a customizable YouTube Summarizer App built with:
        -  YouTube Transcript API
        -  Ollama + LLaMA 3 (Local LLM)
        -  Streamlit for Web UI
        -  Lottie Animations for better UX
    """)
    st_lottie(lottie_animation, height=200)
