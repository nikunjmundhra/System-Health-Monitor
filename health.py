from datetime import datetime
import psutil
import os

os.makedirs("logs" ,exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("C:\\").percent

line = f"{timestamp} CPU = {cpu}% RAM={ram}% DISK={disk}%"
lines_to_write = [line]

if cpu > 80:
    lines_to_write.append(f"{timestamp} WARNING : CPU AT {cpu}%")
if disk>90:
    lines_to_write.append(f"{timestamp} WARNING : Disk at {disk}%")

try:
    with open("logs/health.log","a") as f:
        for item in lines_to_write:
            f.write(item + "\n")
except OSError as e:
    print("could not write log: ", e)
