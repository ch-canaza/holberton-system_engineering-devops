#!/usr/bin/python3
'''
    script to export all data in the JSON format.
'''
import json
import requests


if __name__ == "__main__":
    '''
        returns information for all employees in JSON format
    '''
    filename = "todo_all_employees.json"
    users = requests.get('https://jsonplaceholder.typicode.com/users/').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    all_users = {}
    current_user = {}

    for user in users:
        user_id = user.get('id')
        all_users[user_id] = []
        current_user[user_id] = user.get('username')

    for task in todos:
        current_task = {}
        user_id = task.get('userId')
        current_task['task'] = task.get('title')
        current_task['completed'] = task.get('completed')
        current_task['username'] = current_user.get(user_id)
        all_users.get(user_id).append(current_task)

    with open(filename, 'w') as json_file:
        json.dump(all_users, json_file)
