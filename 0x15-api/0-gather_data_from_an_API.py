#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))

    name = user.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1

<<<<<<< HEAD
        # Display the progress
        print(f"Employee {data[0]['Ervin Howell']} is done with tasks({done_tasks}/{total_tasks}):")
        for task in done_task_names:
            print(f"\t{task}")
    else:
        print(f"Error: Unable to retrieve data for employee {employee_id}")
=======
    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))
>>>>>>> 9fe4a1ca1036641fafe0ab54f94956e84e96f182

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
