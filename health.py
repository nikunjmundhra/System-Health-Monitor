from datetime import datetime
import psutil
import os

os.makedirs("logs" ,exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

line = f"{timestamp} CPU = {cpu}% RAM={ram}% DISK={disk}%"
print(line)

try:
    with open("logs/health.log","a") as f:
        f.write(line + "\n")
except OSError as e:
    print("could not write log: ", e)
