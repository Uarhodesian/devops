import psutil as p
"""cpu"""
print('cpu use:',p.cpu_percent(interval=1))
"""memory"""
memusage = p.virtual_memory()
print('memory use:', memusage)
"""disk partitions"""
disk_part = p.disk_partitions()
print('disk part:',disk_part)
"""disk usage"""
disk_usage = p.disk_usage("/")
print('disk use:',disk_usage)
#"""network connection"""
#net = p.net_io_counters()
#print(net)
"""boot time"""
import datetime as dt
boot = p.boot_time()
#print(boot)
x = dt.datetime.fromtimestamp(boot).strftime("%Y-%m-%d %H:%M:%S")
print(x)
