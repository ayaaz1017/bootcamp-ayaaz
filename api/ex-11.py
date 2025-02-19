import requests

HN_TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
HN_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

def fetch_hacker_news():
    response = requests.get(HN_TOP_STORIES_URL)

    if response.status_code == 200:
        top_stories = response.json()[:10]  # Fetch top 10 stories
        print("📰 Hacker News Top Posts 📰\n")
        
        for story_id in top_stories:
            story = requests.get(HN_ITEM_URL.format(story_id)).json()
            print(f"🔗 {story.get('title', 'No title')} - {story.get('url', 'No URL')}")
            print("-" * 40)
    else:
        print("❌ Error fetching Hacker News posts.")

fetch_hacker_news()
