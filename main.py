import time
from RoomController import *

time.sleep(0.1) # Wait for USB to become ready

print("RoomController Party Light!")
s = RoomController()

s.run()