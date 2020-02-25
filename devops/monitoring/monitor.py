import psutil as p
"""cpu"""
print(p.cpu_percent(interval=1))
"""memory"""
memusage = p.virtual_memory()
print(memusage)