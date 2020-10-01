#fileObj = open("files/fruits.txt")
# print(fileObj.read())
# print(fileObj.read())

#content = fileObj.read()
# fileObj.close()
# print(content)
"""
with open("files/fruits.txt") as fileObj:
    content = fileObj.read()
print(content)

with open("files/vegetables", "a") as fileObj:
    fileObj.write("\npotato")
"""
"""
with open("files/vegetables", "a+") as fileObj:
    fileObj.write("\npotato")
    fileObj.seek(0)
    content = fileObj.read()

print(content)
"""

import time
import os
import pandas
while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")
        print(data.mean()["st1"])
        print(data["st1"][0])
    else:
        print("err:file not found")
    time.sleep(3)
