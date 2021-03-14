import json
import time
from networktables import NetworkTables

json_path = input("Enter the JSON file path: ")

# json_string = json_file.read().replace('\n', '')
# trial_object = json.loads(json_string)

ip = input("Robot IP Address: ")

NetworkTables.initialize(server=ip)


def valueChanged(table, key, value, isNew):
    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))


def connectionListener(connected, info):
    print(info, "; Connected=%s" % connected)


NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

sd = NetworkTables.getTable("metaLog")
sd.addEntryListener(valueChanged)

results_object = []

while True:
    input("Press Enter to Read Log Data")
    log_data = {}
    log_data["timestamp"] = sd.getString("timeStamp", "no data")
    log_data["elapsedAutoTime"] = sd.getNumber("elapsedAutoTime", 0)
    log_data["successful"] = input("successful: (y/n) ") == "y"
    log_data["markers_hit"] = input("Markers hit: ")
    log_data["markers_hit"] = input("Markers hit: ")
    log_data["markers_hit"] = input("Markers hit: ")
    print("Log Data: ", log_data)
    if input("Save: (y/n) ") == "y":
        results_object.append(log_data)
    with open(json_path,"w") as json_file:
        json.dump(results_object, json_file)
