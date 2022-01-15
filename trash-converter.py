#!/bin/python3
import time

startTime = time.time()

f = open("caroza.txt", "r")
text = f.read() # this will take some memory but idc since i have like 12gb ram loll
f.close() # closing it since why not
jsonver = "{" #json version in memory (yes it will take even more memory)
subtitle = ""
scompleted = False
content = ""

def addSubtitle(title, text):
    global jsonver
    jsonver += f'\n\t"{title}": "{text}",'

nr = 0

for char in text:
    nr+=1
    print(f"{round(nr/len(text)*100)}% ({nr}/{len(text)})")
    if not scompleted:
        if char != " ":
            subtitle+=char
        else:
            scompleted = True
        continue
    if char != "\n":
        if char == "\"":
            content+="\\\""
            continue
        content+=char
    else:
        addSubtitle(subtitle, content)
        scompleted = False
        subtitle = ""
        content = ""

jsonver += "\n}"

coolio = open("beautified.json", "w")
coolio.write(jsonver)
coolio.close()
print(f"Finished! {time.time()-startTime}s")