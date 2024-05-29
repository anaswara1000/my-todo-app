import os
current_file_path = os.path.abspath(__file__)
relative_path = 'todos.txt'
full_path = os.path.join(os.path.dirname(current_file_path),relative_path)
print(full_path)

def get_todos(filepath=full_path):
    """read a textfile and return the list of todo items"""
    print(filepath)
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg,filepath=full_path):
    """write the todo items list in the textfile"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__=="__main__":
    print("hello")
    print(get_todos())



