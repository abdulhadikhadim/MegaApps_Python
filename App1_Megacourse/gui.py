import FreeSimpleGUI as sg 
from mega_course import get_todos,write_todos
import time

label = sg.Text("Enter a Todo: ")
input_box = sg.InputText(tooltip = "Enter Todo", key='todo')

sg.theme('Black')
add_button = sg.Button("Add")
add_button1 = sg.Button("Edit")
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')
clock = sg.Text('', key = 'clock')
list_box = sg.Listbox(values=get_todos(),key='todos',
enable_events=True, size=[45,10])

window = sg.Window("My To-Do App: ", layout = [[clock],[label],
[input_box,add_button],[list_box,add_button1,complete_button],[exit_button]],
font=('Helvetica',20))

while True:
    event , values = window.read(timeout = 200)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            # print(new_todo)
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values = todos)
        case 'Edit':
            try:

                todo_to_edit = values['todos'][0]
                # todo = value['todo']
                new_todo = values['todo']
                todos = get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values = todos)
            except IndexError:
                sg.popup("Select the command first")
        case 'todos':
            window['todo'].update(value = values['todos'][0])
        
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = get_todos()
                todos.remove(todo_to_complete)
                write_todos(todos)
                window['todos'].update(values = todos)
                # window['todos'].update(value = '')
            except IndexError:
                sg.popup("Select the Command first", font= ('Helvetica',20))
        

        case 'Exit':
            break
        
        case sg.WIN_CLOSED:
            break


window.close()


