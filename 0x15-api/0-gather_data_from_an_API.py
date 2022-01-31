#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
Using "https://jsonplaceholder.typicode.com/"
Returns information about his/her TODO list progress
"""
import requests
from sys import argv


def gather_data():
    """Fetches data of employees and their todo tasks"""
    users_url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url)
    EMPLOYEE_NAME = ""
    for i in users.json():
        if i.get("id") == argv[1]:
            EMPLOYEE_NAME = i.get("name")
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos = requests.get(todos_url)
    for tasks in todos.json():
        if tasks.get("userId") == argv[1]:
            TOTAL_NUMBER_OF_TASKS += 1
            if tasks.get("completed") is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(tasks.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t {}".format(task))


if __name__ == "__main__":
    gather_data()
