import streamlit as st
from src.utils_method import get_query_params



def main() -> None:
    query_params = get_query_params()
    if query_params:
        if "source" in st.query_params:
            source = st.query_params["source"]
            video_file = open(f'video/{source}.mp4', 'rb')
            video_bytes = video_file.read()

        st.video(video_bytes)
    else:
        st.error("Please provide a valid channel name")

if __name__ == "__main__":
    main()

#st.video(video_bytes, format="video/mp4", start_time=0, *, subtitles=None, end_time=None, loop=False, autoplay=False, muted=False)