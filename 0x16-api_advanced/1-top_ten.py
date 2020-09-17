#!/usr/bin/python3
"""Function to print posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    user = {
        "User-Agent": "ch_canaza"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=user, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
