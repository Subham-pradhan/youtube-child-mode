import joblib
from api_utils import fetch_video_details_by_channel, fetch_video_details_by_search
from content_filter import is_child_safe

model = joblib.load('safe_content_model.pkl')

def get_clean_videos(api_key, channel_id=None, search_query=None):
    if channel_id:
        all_videos = fetch_video_details_by_channel(api_key, channel_id)
    elif search_query:
        all_videos = fetch_video_details_by_search(api_key, search_query)
    else:
        raise ValueError("Provide either a channel ID or a search query.")

    clean_videos = []
    for video in all_videos:
        title = video['title']
        description = video['description']

        title_pred = model.predict([title])[0]
        description_pred = model.predict([description])[0]

        if title_pred == 1 and description_pred == 1:
            clean_videos.append(video)

    return clean_videos
