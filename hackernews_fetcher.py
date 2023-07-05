#!/usr/bin/python

import requests
import os.path
import json

save_path = os.path.dirname(os.path.realpath(__file__))

def get_top_stories():
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')
    story_ids = json.loads(response.text)[:5]
    stories = []
    for id in story_ids:
        response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
        story = json.loads(response.text)
        title = story.get('title', '')
        url = story.get('url', '')
        story_type = story.get('type', '') 
        stories.append({'title': title, 'url': url, 'type': story_type})
    return stories

if __name__ == "__main__":
    top_stories = get_top_stories()

    # Save news data along with an index for cycling through articles
    path = os.path.join(save_path, "articles.json")

    # Save stories in a JSON file
    with open(path, 'w') as file:
        json.dump({'index': 0, 'articles': top_stories}, file)