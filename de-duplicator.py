# SUPERNOOB20 © 2026
# WARNING: DO NOT RUN THIS CODE IF YOU DON'T KNOW WHAT YOU'RE DOING.

import os
from hashlib import md5

path = input("Where is your image sequence? \n")
os.chdir(path)

files = os.listdir(path)
number_of_files = len(files)

for i in range(0, number_of_files):
    for j in range(0, number_of_files):

        file_1 = files[i]
        file_2 = files[j]

        filesize_1 = os.path.getsize(file_1)
        filesize_2 = os.path.getsize(file_2)

        if (j > i) and (filesize_1 == filesize_2):

            # WIP: Add try block for the hashes here.
            try:
                hash_1 = md5(open(file_1, 'rb').read()).hexdigest()
            except:
                hash_1 = "悪い"

            try:
                hash_2 = md5(open(file_2, 'rb').read()).hexdigest()
            except:
                hash_2 = "嫌い"

            if (hash_1 == hash_2):         # Might prevent CPU overload thanks to these nested if statements. I know. Crazy.
                print("\n")
                print(f'Detected duplicate of"{file_1}"')
                delete = input(f"Do you REALLY, REALLY want to delete{file_2}???  (Y for yes, N for no)")
                if (delete == "Y"):
                    os.remove(file_2)
            

