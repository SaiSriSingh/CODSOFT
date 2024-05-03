class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_done(self, task_number):
        try:
            task_index = int(task_number) - 1
            self.tasks[task_index] = f"[DONE] {self.tasks[task_index]}"
            print(f"Task {task_number} marked as done.")
        except (ValueError, IndexError):
            print("Invalid task number.")

    def delete_task(self, task_number):
        try:
            task_index = int(task_number) - 1
            del self.tasks[task_index]
            print(f"Task {task_number} deleted successfully.")
        except (ValueError, IndexError):
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Delete Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = input("Enter task number to mark as done: ")
            todo_list.mark_task_done(task_number)
        elif choice == '4':
            task_number = input("Enter task number to delete: ")
            todo_list.delete_task(task_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
