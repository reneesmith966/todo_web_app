

import functions
import streamlit as sl

todos = functions.get_todos()

def add_todo():
    todo = sl.session_state["new_task"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

sl.title("My To-do App")
sl.subheader("This is my to-do app")
sl.write("This app is to increase your productivity!")
for index, todo in enumerate(todos):
    checkbox = sl.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        sl.rerun()

sl.text_input(label="", placeholder="Enter a task: ",
              on_change=add_todo, key="new_task")
print("hello")

