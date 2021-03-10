import json
from networkTables import NetworkTables
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

sd = NetworkTables.getTable("SmartDashboard")
sd.addEntryListener(valueChanged)

print("Trying to connect...")
while not isConnected:
    print("Waiting for connection...")
    time.sleep(1)
print("Connection established!")

# Stuff for after the connection is established should go here. 
maxAcceleration = 4

"autolog" "maxAcceleration"
