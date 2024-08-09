# ** Open and Read a file
    # 1) Traditional way
    # 2) Better way


# 1) Traditional way
# file = open("file.txt")
# content = file.read()
# print(content)
# file.close()


# 2) Better way: No need to use file.close()
# with open("file.txt") as file:
#     content = file.read()
#     print(content)




# ** Write to a file: All the things depend on mode a for append, w for write and delete the previous text, and so many more...
# with open("file.txt", mode="a") as file:
#     file.write("\nGoodbye.")
    
# Let's write to a file which doesn't exist
# with open("new.txt", mode="w") as file:
#     file.write("This is Python running in vscode!")
    
    
    


# *************************** PATH **************************
# file_path = "C:/Users/Alidad Azimi/Desktop/file.txt"
abs_file_path = "/Users/Alidad Azimi/Desktop/file.txt"   # absolute path
rel_file_path = "../../Desktop/file.txt"   # relative path
with open(rel_file_path) as file:
    content = file.read()
    print(content)