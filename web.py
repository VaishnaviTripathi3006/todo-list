import streamlit as st
import functions
todos=functions.get_todos
def add_todo():
    todo=st.session_state["new"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Task Manager")
st.subheader("Prioritize your priorities")
st.write("Be Productive")
todos=functions.get_todos()
for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label="",placeholder="New task to complete...",on_change=add_todo,key='new')
