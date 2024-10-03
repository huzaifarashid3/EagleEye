import streamlit as st

st.session_state.videos = []

st.title("EagleEye")
video_files = st.file_uploader("Upload a Video", accept_multiple_files=True)

if video_files is not None:
    for video_file in video_files:
        st.session_state.videos.append(video_file)

n_cols = 4
n_rows = len(st.session_state.videos) // n_cols + 1
rows = [st.columns(n_cols) for _ in range(n_rows)]
grid = [cell for row in rows for cell in row]

for cell, video in zip(grid, st.session_state.videos):
    cell.video(video)
