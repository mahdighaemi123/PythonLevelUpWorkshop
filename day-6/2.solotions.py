# solution 1
import json

intro = """
------------------------
     To-Do list CLI
------------------------"""

options = """
------------------------
         Options
------------------------
1. Add new task
2. Mark task as completed
3. Remove task
4. Exit
"""

file_path = "tasks.json"


def app_exit():
    exit()


def load_tasks():
    with open(file_path) as file:
        tasks = file.read()
        tasks = json.loads(tasks)
        return tasks


def display_tasks(tasks):
    if len(tasks) == 0:
        print("       empty list       ")
        return

    for (index, key) in enumerate(tasks.keys(), start=1):
        task = key
        status = tasks[key]
        status_message = "[✓]" if status else "[ ]"
        print(str(index)+". "+status_message+" "+task)


def display_intro(tasks):
    print(intro)
    display_tasks(tasks)
    print(options)


def add_task(tasks, task_title):
    tasks[task_title] = False


def mark_task(tasks, task_title):
    tasks[task_title] = True


def remove_task(tasks, task_title):
    del tasks[task_title]


def save_tasks(tasks):
    open(file_path, "w").write(json.dumps(tasks))


def main():
    while 1:
        try:
            tasks = load_tasks()
            display_intro(tasks)

            option = input("> enter option number: ")

            if option == "1":
                title_title = input("> enter task title: ")
                add_task(tasks, title_title)

            elif option == "2":
                title_title = input("> enter task title: ")
                mark_task(tasks, title_title)

            elif option == "3":
                title_title = input("> enter task title: ")
                remove_task(tasks, title_title)

            elif option == "4":
                app_exit()

            else:
                print("option not found")

            save_tasks(tasks)

        except:
            print("error")


main()
