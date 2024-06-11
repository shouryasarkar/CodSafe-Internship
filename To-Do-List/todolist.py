# Importing the required module and tasks
from task import Task


# Defining a class which represents a to-do-list
class ToDoList:

    # This is the constructor method. It initializes the ToDoList object.
    def __init__(self):
        # Initialize an empty list to store tasks.
        self.tasks = []

    # This method adds a new task to a list
    def add_task(self, description):
        # Create a new Task object with the given description and append it to the tasks list.
        self.tasks.append(Task(description))

    # Going to show all the tasks 
    def view_task(self):
        # Interate over each task index in the list
        for idx, task in enumerate(self.tasks):
            # Print the task number (index + 1) and its description.
            print(f"{idx + 1}.{task}")

    # This method updates an exhisting task in the list 
    def update_task(self, index, description=None, completed= None):
        if description:
            self.tasks[index].description = description
        if completed is not None:
            if completed:
                self.tasks[index].mark_complete()
            else:
                self.tasks[index].completed = False
    
    # This method deletes a task from the list 
    def delete_task(self, index):
        del self.tasks[index]

    # This method saevs the tasks to a file
    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.desctiption}\t{task.completed}\n")

    # Loads task from a file 
    def load_tasks(self, filename):
        self.tasks = []
        with open(filename, 'r') as file:
            for line in file:
                description, completed = line.strip().split('\t')
                task = Task(description)
                if completed == 'True':
                    task.mark_complete()
                self.tasks.append(task)