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
    if videos:
        n_cols = 4
        n_rows = len(videos) // n_cols + 1
        rows = [st.columns(n_cols) for _ in range(n_rows)]
        grid = [cell for row in rows for cell in row]
        for cell, video in zip(grid, videos):
            cell.video(video)
        # use st.selectbox to select a video
        video_names = [f"Video {i+1}" for i in range(len(videos))]
        selected_video_name = st.selectbox("Select  video to process:", video_names)

        # dddisplay selected viddoe seperatly
        selected_video_index = video_names.index(selected_video_name)
        st.write(f"Selected Video: {selected_video_name}")
        st.video(videos[selected_video_index])

    else:
        st.write("No videos uploaded yet.")



with crop:
    # TODO:
    # use some annotation tool to crop the frame from the selected video
    st.empty()

with process:
    # TODO:
    # use some model to process the frame
    st.empty()
