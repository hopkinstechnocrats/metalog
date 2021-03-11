import json
from networktables import NetworkTables
import time

json_path = input("Enter the JSON file path: ")
json_file = open(json_path,"r")
json_string = json_file.read().replace('\n', '')
trial_object = json.loads(json_string)

ip = input("Robot IP Address: ")

NetworkTables.initialize(server=ip)

# This function be rewritten. It doesn't use the table value at all.  
def valueChanged(table, key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))

isConnected = False
def connectionListener(connected:bool, info):
    print(info, "; Connected=%s" % connected)
    global isConnected
    if connected: isConnected = True

NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

output = NetworkTables.getTable("toRobot")
output.addEntryListener(valueChanged)
input = NetworkTables.getTable("fromRobot")

print("Trying to connect...")
while not isConnected:
    print("Waiting for connection...")
    time.sleep(1)
    isConnected = True  # for debug purposes
print("Connection established!")
for line in trial_object:
    # Puts all output in json object
    for key in line:
        if not output.putValue(key, line.get(key)):
            print("The value", line.get(key), "was not successfully converted!")
    while not input.getBoolean("inTask", False):
        time.sleep(1)
        input.putBoolean("inTask", True)  # for debug purposes
    print("Task started!")
    while input.getBoolean("inTask", True):
        time.sleep(1)
        input.putBoolean("inTask", False)  # for debug purposes
    print("Task finished!")
    
