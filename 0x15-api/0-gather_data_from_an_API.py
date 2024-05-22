#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoint
    url = f"https://api.example.com/employees/{employee_id}/todos"

    # Make a GET request to the API endpoint
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Calculate the number of done tasks and total tasks
        done_tasks = sum(task["is_done"] for task in data)
        total_tasks = len(data)

        # Extract the names of the done tasks
        done_task_names = [task["title"] for task in data if task["is_done"]]

        # Display the progress
        print(f"Employee {data[0]['name']} is done with tasks({done_tasks}/{total_tasks}):")
        for task in done_task_names:
            print(f"\t{task}")
    else:
        print(f"Error: Unable to retrieve data for employee {employee_id}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
