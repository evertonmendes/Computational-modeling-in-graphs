import os

help_path=os.path.dirname(__file__)
file_name=input()

print(help_path+"/"+file_name)
archive= open(help_path+"/"+file_name, 'r')

for i in archive:
    print(i)