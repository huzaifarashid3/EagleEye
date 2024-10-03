import streamlit as st

vidoes = []

st.title("EagleEye")
video_files = st.file_uploader("Upload a Video", accept_multiple_files=True)

if video_files is not None:
    for video_file in video_files:
        vidoes.append(video_file)

for video in vidoes:
    st.video(video)