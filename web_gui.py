import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st. session_state["new_todo"] +"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My to do app")
st.write("This app to increase the productivity")


for index, todo in enumerate(todos):
   checkbox = st.checkbox(todo, key=todo)
   if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()

st.text_input(label='add todo', placeholder='enter a todo', key="new_todo", on_change=add_todo)


st.session_state
