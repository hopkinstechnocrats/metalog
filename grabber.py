import csv
import json 
folderPath = input("Enter the path of the folder: ")
filePath1 = folderPath + "\\" + input("Enter the name of the file: ")

file1 = open(filePath1, 'r').read()
object = json.loads(file1)
outer = []
fields = []
firstTime = True
for line in object:
    
    inner = []
    y = line.get("timestamp")

    for block in line:
        input(line)
        if firstTime:
            fields.append(block)
        
        inner.append(line.get(block))
        input(line.get(block))
    
    file2 = open(folderPath + "\\logs" + y + ".bag", 'r').readline()
    object2 = json.loads(file2)
    values = object2.get("values")
    
    for line in values:
        if firstTime:
            fields.append(line["name"])
        inner.append(line["value"])
    outer.append(inner)
    
    firstTime = False

writer = csv.writer(open(folderPath + "\\output", 'w'))
writer.writerow(fields)
writer.writerows(outer)
