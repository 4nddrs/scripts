import sys
import json
from colorama import Fore, Style

TASKS_FILE = 'tasks.json'

def load_tasks():
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def list_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✅" if task['completed'] else "❌"
        print("")
        print(f"{i+1}. {status} {task['description']}")
    print("")
def add_task(tasks, description):
    tasks.append({'description': description, 'completed': False})
    save_tasks(tasks)
    list_tasks(tasks)

def complete_task(tasks, index):
    tasks[index]['completed'] = True
    save_tasks(tasks)
    list_tasks(tasks)

def main():
    tasks = load_tasks()
    
    if len(sys.argv) < 2:
        print("Usage: tdo [list|add|complete] [task_description|task_number]")
        return
    
    command = sys.argv[1]
    
    if command == 'list':
        list_tasks(tasks)
    elif command == 'add':
        description = ' '.join(sys.argv[2:])
        add_task(tasks, description)
    elif command == 'complete':
        index = int(sys.argv[2]) - 1
        complete_task(tasks, index)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()