import os
import platform
import psutil as p
import sys
import datetime as dt

argumentList = sys.argv
argumentList += argumentList
print (argumentList)
"""boot time"""
boot = p.boot_time()
x = dt.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S")
print(x)
"""os"""
print(platform.system())
print(platform.release())
if argumentList[1] == "mem":
    print("======")
    print("mem")
    print("======")
    print('mem:', p.virtual_memory())
elif argumentList[1] == "cpu":
    print("======")
    print("cpu")
    print("======")
    print('per-cpu:', p.cpu_percent(interval=1))
    print('per-cpu:', p.cpu_stats())
    print('per-cpu:', p.cpu_freq())
else:
    print("Wrong arguments!\nUse arguments '"'mem'"' or '"'cpu'"' to to specify which metrics do you want to print!")