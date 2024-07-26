# import FreeSimpleGUI as sg 

# text = sg.Text("Welcome")
# button = sg.Button("Delete", key="delete")
# window = sg.Window('My App', layout=[[text], [button]])
# print(window["delete"])

# window.read()
# print(window["delete"])
# window.close()
# from mega_course import get_todos,write_todos
# label = sg.Text("Enter a Todo: ")
# input_box = sg.InputText(tooltip = "Enter Todo", key='Todo')

# add_button = sg.Button("Add")


# window = sg.Window("My To-Do App: ", layout = [[label],
# [input_box,add_button],],
# font=('Helvetica',20))

# while True:
#     event , value = window.read()
#     print(event)
#     print(value)
#     match event:
#         case 'Add':
#             todos = mega_course.get_todos()
#             new_todo = value['Todo'] + "\n"
#             print(new_todo)
#             todos.append(new_todo)
#             mega_course.write_todos(todos)
#         case sg.WIN_CLOSED:
#             break

# window.close()


# NOTE: This script runs only on your local IDE
import FreeSimpleGUI as sg
from converters import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text("", key="output")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button, output_label]])

while True:
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="white")


window.close()