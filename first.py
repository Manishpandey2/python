with open("file.txt","r") as file:
    conent = file.read()
print(conent)

with open("todo.txt","w") as file:
    file.write("Learn Python Build AI Agent Practice Daily")