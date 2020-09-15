#!/usr/bin/python3
"""extend your Python script to export data in the JSON format
"""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    tasks = []
    for task in todos:
        json_format = {}
        json_format["task"] = task.get("title")
        json_format["completed"] = task.get("completed")
        json_format["username"] = username
        tasks.append(json_format)
        json_tasks_format = {}
        json_tasks_format[user_id] = tasks
    with open("{}.json".format(user_id), "w") as json_file:
        json.dump(json_tasks_format, json_file)
