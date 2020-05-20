import os
from pathlib import Path

filename = input()


try:
    os.mkdir(filename)
except OSError:
    print("Creation of the file has failed")
else:
    print("File %s successfully created" % filename)
