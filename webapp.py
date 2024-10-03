import streamlit as st


upload = st.expander("Upload Videos",expanded=True)
select = st.expander("Select Video")
crop = st.expander("Crop Frame")
process = st.expander("Process")

videos = []

with upload:
    video_files = st.file_uploader("Upload a Video", accept_multiple_files=True)

    if video_files is not None:
        for video_file in video_files:
            videos.append(video_file)



with select:
    n_cols = 4
    n_rows = len(videos) // n_cols + 1
    rows = [st.columns(n_cols) for _ in range(n_rows)]
    grid = [cell for row in rows for cell in row]
    for cell, video in zip(grid, videos):
        cell.video(video)
    # TODO: 
    # use st.selectbox to select a video

with crop:
    # TODO:
    # use some annotation tool to crop the frame from the selected video
    st.empty()

with process:
    # TODO:
    # use some model to process the frame
    st.empty()
