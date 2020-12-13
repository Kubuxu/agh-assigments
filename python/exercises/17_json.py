import json

class Task:
    def __init__(self, task, due, priority, difficulty):
        self.task = task
        self.due = due
        self.priority = priority
        self.difficulty = difficulty

    def __str__(self):
        return f"{self.task}\t{self.due}\t{self.priority}\t{self.difficulty}"
    def __repr__(self):
        return str(self.__dict__)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

def encodeTask(obj):
    if isinstance(obj, Task):
        return obj.__dict__
    raise TypeError(repr(obj) + " is not JSON serializable")

def asTask(dct):
    return Task(**dct)

tasks = []


def print_tasks():
    print("Tasks:")
    print("No.\tTask\t\t\tDue\t\tPrio\tDifficulty")
    for no, task in enumerate(tasks):
        print(f"{no}.\t{task}")

with open("tasks.ndjson", "r+") as taskFile:
    for task in taskFile.read().splitlines():
        tasks.append(json.loads(task, object_hook=asTask))

    while True:
        print_tasks()

        action = input("What you want to do? [D]elete/[A]dd/[Q]uit: ")
        action = action.casefold()
        if len(action) == 0:
            break
        action = action[0]

        if action == "d":
            n = input("Which item do you want to delete: ")
            del tasks[int(n)]
        elif action == "a":
            task = input("Name of new task: ")
            due = input("Due date of new task: ")
            priority = input("Priority of new task (1-10): ")
            difficulty = input("Difficulty of new task (1-10): ")
            tasks.append(Task(task, due, priority, difficulty))
        elif action == "q":
            break

    taskFile.seek(0)
    for task in tasks:
        taskFile.write(json.dumps(task, default=encodeTask))
        taskFile.write("\n")

    taskFile.truncate()






