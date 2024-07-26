FILE_PATH = "todos.txt"
import time 

now = time.strftime("%b %d, %Y %H:%M:%S")

print(f"It is {now}")
def get_todos():
    with open(FILE_PATH, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos):
    with open(FILE_PATH, 'w') as file:
        file.writelines(todos)

while True:
    user_action = input("Type add, show, exit, complete: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()
        
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1} - {item}")

    elif user_action.startswith("edit"):
        try: 
            number = int(user_action[5:])

            number = number - 1

            todos = get_todos()
            
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            user_action = input("Type add, show, exit, complete: ").strip()


    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            number = number - 1
            with open(FILE_PATH, 'r') as file:
                todos = file.readlines()
            
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)
            
            write_todos(todos)

            
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is no item with your typed number:  ")
            user_action = input("Type add, show, exit, complete: ").strip()

    elif user_action.startswith("exit"):
        break
    else:
        print('Command is not valid...')

print("bye")
