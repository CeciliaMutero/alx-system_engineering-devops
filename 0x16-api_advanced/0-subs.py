#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    try:
        response = requests.get(url, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            subscribers = data.get('data', {}).get('subscribers', 0)
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        return 0
