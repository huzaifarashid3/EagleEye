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

# Upload Section
with upload:
    video_files = st.file_uploader("Upload a Video", accept_multiple_files=True)

    # Only append videos if they exist
    if video_files is not None:
        videos = list(video_files)  # Store the uploaded files directly into videos

# Select Section
selected_video_index = None  # Initialize as None
with select:
    if videos:
        # Display videos in a grid layout
        n_cols = 4
        n_rows = len(videos) // n_cols + 1
        rows = [st.columns(n_cols) for _ in range(n_rows)]
        grid = [cell for row in rows for cell in row]
        
        for cell, video in zip(grid, videos):
            cell.video(video)

        # Create a selectbox to choose a video
        video_names = [f"Video {i+1}" for i in range(len(videos))]
        selected_video_name = st.selectbox("Select a video to process:", video_names)

        # If a video is selected, update the selected_video_index
        if selected_video_name:
            selected_video_index = video_names.index(selected_video_name)
            st.write(f"Selected Video: {selected_video_name}")
            st.video(videos[selected_video_index])  # Display the selected video
    else:
        st.write("No videos uploaded yet.")

# Crop Section
with crop:
    # Ensure we have videos and a valid selected index
    if videos and selected_video_index is not None:
        st.write(f"Cropping frame from {selected_video_name}")

        # Load the selected video using OpenCV
        video_file = videos[selected_video_index]
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(video_file.read())

        vidcap = cv2.VideoCapture(tfile.name)
        success, frame = vidcap.read()

        if success:
            # Convert the frame to RGB format
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
