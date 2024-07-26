import streamlit as st
from mega_course import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    write_todos(todos)

st.title("My Todo App: ")
st.subheader('The Todo app:')
st.write('This app will increase your productivity')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo , key = todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a Todo', placeholder='Add a new Todo...', on_change=add_todo, key='new_todo')
