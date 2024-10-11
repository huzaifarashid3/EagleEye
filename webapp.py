import streamlit as st
from PIL import Image
import cv2
import tempfile
from streamlit_cropper import st_cropper

upload = st.expander("Upload Videos", expanded=True)
select = st.expander("Select Video")
crop = st.expander("Crop Frame")
process = st.expander("Process")

videos = []

with upload:
    video_files = st.file_uploader("Upload a Video", accept_multiple_files=True)

    if video_files is not None:
        videos = list(video_files) 

selected_video_index = None 
with select:
    if videos:
        # display viddeos
        n_cols = 4
        n_rows = len(videos) // n_cols + 1
        rows = [st.columns(n_cols) for _ in range(n_rows)]
        grid = [cell for row in rows for cell in row]

        for cell, video in zip(grid, videos):
            cell.video(video)

        # selectbox
        video_names = [f"Video {i+1}" for i in range(len(videos))]
        selected_video_name = st.selectbox("Select a video to process:", video_names)

        # update inex when video selectedd
        if selected_video_name:
            selected_video_index = video_names.index(selected_video_name)
            st.write(f"Selected Video: {selected_video_name}")
            st.video(videos[selected_video_index]) 
    else:
        st.write("No videos uploaded yet.")

with crop:
    if videos and selected_video_index is not None:
        st.write(f"Cropping frame from {selected_video_name}")

        video_file = videos[selected_video_index]
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        vidcap = cv2.VideoCapture(tfile.name)

        # duratiopn of vieo
        fps = vidcap.get(cv2.CAP_PROP_FPS)
        frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps

        # slider
        selected_time = st.slider("Select the time to capture the frame:", 0.0, duration, step=0.1)

        # Set the video position to the selected time
        vidcap.set(cv2.CAP_PROP_POS_MSEC, selected_time * 1000)

        success, frame = vidcap.read()

        if success:
            # covert frame to rgb 
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(frame_rgb)

            cropped_img = st_cropper(img_pil, realtime_update=True, box_color='blue', aspect_ratio=None)

            if cropped_img:
                st.image(cropped_img, caption="Cropped Image")
            else:
                st.write("Could not extract frame from the video.")
        else:
            st.write("Could not read the video frame for cropping.")
    else:
        st.write("Please upload and select a video to crop.")

with process:
    st.empty()
