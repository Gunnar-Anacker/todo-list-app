# todo.py

# Step 1: Start with an empty list to hold tasks
tasks = []
complete_tasks = []
# Step 2: Add a task
def add_task(task):
    tasks.append(task)

# Step 3: View tasks
def view_tasks():
    for task in tasks:
        print(task)
    for task in complete_tasks:
        print (task)
# Step 4: Delete a task
def del_task(taskNum):
    tasks.pop(taskNum)
            

# Step 5: Mark task complete
def mark_complete(task):
    completeTask = (tasks[task] + "✅")
    complete_tasks[task] == (completeTask)
    
# Demo flow (you can run this file directly: python todo.py)
if __name__ == "__main__":
    add_task("Finish Cyber 201 assignment")
    add_task("Push code to GitHub")
    view_tasks()
    del_task(1)
    mark_complete(0)
    view_tasks()