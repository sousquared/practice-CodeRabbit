import os
from datetime import datetime

def get_files(dir):
    files_list = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(".txt"):
                files_list.append(os.path.join(root, file))
    return files_list

def read_file(file):
    with open(file, 'r') as f:
        data = f.read()
    return data

def get_current_date():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    return date

def write_to_file(dir, data):
    with open(dir + "/output.txt", 'w') as f:
        f.write(data)

dir = "/home/user/documents"
files = get_files(dir)
for file in files:
    data = read_file(file)
    print(data)
write_to_file(dir, get_current_date())