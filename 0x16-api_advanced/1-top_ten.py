#!/usr/bin/python3
""" queries the Reddit API and prints the titles
of the first 10 hot posts"""
import requests

def top_ten(subreddit):
    """ queries the Reddit API and prints the titles
    of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Python:top_ten:v1.0 (by Sad_Worldliness_7719)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)
            return
    except requests.exceptions.RequestException:
        print(None)
