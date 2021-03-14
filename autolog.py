import json
import time
from networktables import NetworkTables
import time

json_input_path = input("Enter the JSON input file path: ")
json_path = input("Enter the JSON output file path: ")


# json_string = json_file.read().replace('\n', '')
# trial_object = json.loads(json_string)

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

ml = NetworkTables.getTable("metaLog")
ml.addEntryListener(valueChanged)

results_object = []

while True:
    input("Press Enter to Read Log Data")
    log_data = {}
    log_data["timestamp"] = ml.getString("timeStamp", "no data")
    log_data["elapsedAutoTime"] = ml.getNumber("elapsedAutoTime", 0)
    log_data["successful"] = input("successful: (y/n) ") == "y"
    log_data["markers_hit"] = input("Markers hit: ")
    log_data["markers_hit"] = input("Markers hit: ")
    log_data["markers_hit"] = input("Markers hit: ")
    print("Log Data: ", log_data)
    if input("Save: (y/n) ") == "y":
        results_object.append(log_data)
    with open(json_path,"w") as json_file:
        json.dump(results_object, json_file)

output = NetworkTables.getTable("toRobot")
output.addEntryListener(valueChanged)

print("Trying to connect...")
while not isConnected:
    print("Waiting for connection...")
    time.sleep(1)
print("Connection established!")
attributes = {}
with open(json_input_path, "r") as json_file:
    attributes = json.load(json_file)
    
while True:
    for key in attributes:
        value = input("Enter Input Value: " + key + ": ")
        if not output.putValue(key, value):
            print("The value ", value, " was not successfully converted!")
    while ml.getBoolean("enabled", False):
        time.sleep(1)
    print("Task started!")
    while ml.getBoolean("enabled", True):
        time.sleep(1)
    print("Task finished!")
    log_data = {}
    log_data["timestamp"] = ml.getString("timeStamp", "no data")
    log_data["elapsedAutoTime"] = ml.getNumber("elapsedAutoTime", 0)
    log_data["successful"] = input("successful: (y/n) ") == "y"
    log_data["markers_hit"] = input("Markers hit: ")
    print("Log Data: ", log_data)
    if input("Save: (y/n) ") == "y":
        results_object.append(log_data)
    with open(json_path,"w") as json_file:
        json.dump(results_object, json_file)
    
    
