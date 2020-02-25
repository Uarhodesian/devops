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
platform.system()
platform.release()