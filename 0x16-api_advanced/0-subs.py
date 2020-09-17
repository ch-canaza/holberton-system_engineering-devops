#!/usr/bin/python3
""" Write a function that queries the Reddit API and returns
    the number of subscribers (not active users, total
    subscribers) for a given subreddit """
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    """
    user = {'User-Agent': 'u/ch_canaza'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
