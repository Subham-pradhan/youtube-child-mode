import joblib
from api_utils import fetch_video_details_by_channel, fetch_video_details_by_search
from content_filter import is_child_safe

model = joblib.load('safe_content_model.pkl')

def get_clean_videos(api_key, channel_id=None, search_query=None):
    if channel_id:
        videos = fetch_video_details_by_channel(api_key, channel_id)
    elif search_query:
        videos = fetch_video_details_by_search(api_key, search_query)
    else:
        raise ValueError("Provide either a channel ID or a search query.")

    clean_videos = []
    for video in videos:
        title = video['title']
        description = video['description']

        title_pred = model.predict([title])[0]
        desc_pred = model.predict([description])[0]

        title_safe = is_child_safe(title)
        desc_safe = is_child_safe(description)

        if title_pred == 1 and desc_pred == 1 and title_safe and desc_safe:
            clean_videos.append(video)

    return clean_videos
