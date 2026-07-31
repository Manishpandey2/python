# with open("file.txt","r") as file:
#     conent = file.read()
# print(conent)

# with open("todo.txt","w") as file:
#     file.write("Learn Python Build AI Agent Practice Daily")

with open("students.txt","r") as file:
    for line in file:
        print(f"Student : {line.strip()}")