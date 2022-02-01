#!/usr/bin/python3
"""
Module 2-export_to_JSON
Using "https://jsonplaceholder.typicode.com/"
Returns information about his/her TODO list progress
"""
import json
import requests
from sys import argv


def gather_data_to_json():
    """Fetches data of employees and their todo tasks"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    for i in users.json():
        if i.get("id") == int(argv[1]):
            USERNAME = i.get("username")
            break
    TASK_STATUS_TITLE = []
    todos = requests.get("http://jsonplaceholder.typicode.com/todos")
    for t in todos.json():
        if t.get('userId') == int(argv[1]):
            TASK_STATUS_TITLE.append((t.get('completed'), t.get('title')))

    """export to json"""
    t = []
    for task in TASK_STATUS_TITLE:
        t.append({"task": task[1], "completed": task[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    gather_data_to_json()
