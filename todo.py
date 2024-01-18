user_prompt="Enter Task To Executed:"
todo=[]
while True:
    todo=input(user_prompt)
    print(todo.capitalize())
    todo.append(todo)

