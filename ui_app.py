import streamlit as st
from video_filter import get_clean_videos

# Your API Key
api_key = "AIzaSyDte8q6lIqVhJF0NobBz1fTvzFYCRQW0fY"

st.set_page_config(page_title="Child Mode YouTube Viewer", layout="centered")

st.title("👶 Child Mode YouTube Viewer")
st.write("Filter and show only safe YouTube videos for kids")

channel_id = st.text_input("📺 Enter YouTube Channel ID (Optional)")
search_query = st.text_input("🔍 Enter Search Query (Optional)")

if st.button("Get Safe Videos"):
    if not api_key:
        st.warning("API Key is missing.")
    elif not channel_id and not search_query:
        st.warning("Please enter either Channel ID or Search Query.")
    else:
        with st.spinner("Fetching and filtering videos..."):
            try:
                videos = get_clean_videos(api_key, channel_id=channel_id, search_query=search_query)
                if videos:
                    for vid in videos:
                        st.markdown(f"### {vid['title']}")
                        st.write(vid['description'])
                        st.video(f"https://www.youtube.com/watch?v={vid['video_id']}")
                        for comment in vid['comments']:
                            st.markdown(f"- {comment}")
                else:
                    st.info("No safe videos found.")
            except Exception as e:
                st.error(f"Error: {str(e)}")
