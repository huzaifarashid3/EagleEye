import streamlit as st

st.title("Eagleeye")
video_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])

if video_file is not None:
    st.video(video_file) 

    st.write("Choose an action:")
    button_style = """
    <style>
    .stButton > button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #45a049; /* Darker Green */
    }
    </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    if st.button("Process Video"):
        st.write("processing")
        st.success("sucess")

    if st.button("Analyze Video"):
        st.write("analyzing")
        st.success("sucess")

    if st.button("Download Video"):
        st.write("preparing")
        st.success("sucess")

    if st.button("Share Video"):
        st.write("shring")
        st.success("success")
