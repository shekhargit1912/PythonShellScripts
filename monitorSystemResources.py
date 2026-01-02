import psutil 

print("CPU Usage",psutil.cpu_percent())
print("Memory Usage",psutil.virtual_memory().percent)

print("Disk Usage",psutil.disk_usage('/').percent)
print("Network Stats",psutil.net_io_counters())
print("Battery Info",psutil.sensors_battery())
print("Processes List:")
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)
# This script uses the psutil library to monitor and print various system resources such as CPU usage, memory usage, disk usage, network statistics, battery information, and a list of running processes.
