import requests

def fetch_video_details_by_channel(api_key, channel_id, max_results=10):
    url = (
        f"https://www.googleapis.com/youtube/v3/search?part=snippet"
        f"&channelId={channel_id}&maxResults={max_results}&order=date&type=video&key={api_key}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()

    videos = []
    for item in data.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        videos.append({
            'video_id': video_id,
            'title': title,
            'description': description,
            'comments': ["Comments not fetched"]
        })
    return videos

def fetch_video_details_by_search(api_key, search_query, max_results=10):
    url = (
        f"https://www.googleapis.com/youtube/v3/search?part=snippet"
        f"&q={search_query}&maxResults={max_results}&order=date&type=video&key={api_key}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        return []
    data = response.json()

    videos = []
    for item in data.get('items', []):
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        description = item['snippet']['description']
        videos.append({
            'video_id': video_id,
            'title': title,
            'description': description,
            'comments': ["Comments not fetched"]
        })
    return videos
