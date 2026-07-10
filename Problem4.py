import os

#select the directory who you want to list
directory_path= '/home/jawad-ahmed/Downloads'

#use the os model to list the directory content
content = os.listdir(directory_path)


for item in content:
    print(item)
