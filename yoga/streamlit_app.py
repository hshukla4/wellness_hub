import streamlit as st

st.title("Wellness Hub AI – Guided Yoga Session")

video_file = open('tadasana_video.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
