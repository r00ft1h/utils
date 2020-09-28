import os
import sys


def recur(path):
    result = []
    def inner():
        for curdir, folders, files in os.walk(path):
            for file in files:
                filepath = os.path.join(curdir, file)
                result.append(filepath)

            for folder in folders:
                if folder != '_backup':
                    dirpath = os.path.join(curdir, folder)
                    recur(dirpath)
        return result
    return inner()

curdir = sys.argv[1]
filepaths = recur(curdir)
for filepath in filepaths:
    print(filepath)
