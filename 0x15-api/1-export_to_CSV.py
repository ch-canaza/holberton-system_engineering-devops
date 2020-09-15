#!/usr/bin/python3
"""  script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    usere_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            tasks.writerow([user_id, user.get("username"),
                            task.get("completed"), task.get("title")])
