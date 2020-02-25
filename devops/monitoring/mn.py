import os
import platform
import psutil as p
import sys
import datetime as dt

argumentList = sys.argv
print (argumentList)
"""boot time"""
boot = p.boot_time()
#print(boot)
x = dt.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S")
print(x)
"""os"""
print(platform.system())
print(platform.release())
#print("use arguments '"'mem'"' or '"'cpu'"' to to specify which metrics you want to print")
if argumentList[1] == "mem":
    print("mem rules")
elif argumentList[1] == "cpu":
    print("cpu rules")
else:
    print("Wrong arguments! Use arguments '"'mem'"' or '"'cpu'"' to to specify which metrics you want to print")