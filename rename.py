import os
import sys
from pathlib import Path
import shutil


def recur(path):
    result = []
    def inner():
        for curdir_, folders, files in os.walk(path):
            for file in files:
                filepath = os.path.join(curdir_, file)
                result.append(filepath)

            for folder in folders:
                dirpath = os.path.join(curdir_, folder)
                result.append(dirpath)
                recur(dirpath)
        return result
    return inner()

source_dir = sys.argv[1]
old_word = sys.argv[2]
new_word = sys.argv[3]

# source_dir = r"C:\Users\Administrator\Desktop\1"
# old_word = 'agixx'
# new_word = 'agisk'

while True:
    items = recur(source_dir)
    for item in items:
        if old_word in item:
            if os.path.isfile(item):
                curdir = str(Path(item).parent)
            else:
                curdir = item

            # File found
            if os.path.isfile(item):
                fullname = str(Path(item).name)
                fullname_new = str(fullname).replace(old_word, new_word)
                item_new = os.path.join(curdir, fullname_new)
                shutil.move(item, item_new)
                print(f'Rename File: {fullname_new}')
                continue

            # Directory found
            if os.path.isdir(item):
                curdir_new = str(curdir).replace(old_word, new_word)
                shutil.move(curdir, curdir_new)
                print(f'Rename Directory: {curdir_new}')
                break
    else:
        print('Done.')
        break
