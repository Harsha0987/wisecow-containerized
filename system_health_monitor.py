import psutil
import time
import logging


logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s %(message)s')


CPU_THRESHOLD = 80.0  
MEMORY_THRESHOLD = 80.0  
DISK_THRESHOLD = 80.0 
PROCESS_THRESHOLD = 300  

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
        print(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory.percent}%')
        print(f'High Memory usage detected: {memory.percent}%')
    return memory.percent

def check_disk_usage():
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > DISK_THRESHOLD:
        logging.warning(f'High Disk usage detected: {disk_usage.percent}%')
        print(f'High Disk usage detected: {disk_usage.percent}%')
    return disk_usage.percent

def check_running_processes():
    processes = len(psutil.pids())
    if processes > PROCESS_THRESHOLD:
        logging.warning(f'High number of running processes detected: {processes}')
        print(f'High number of running processes detected: {processes}')
    return processes

def monitor_system():
    while True:
        cpu_usage = check_cpu_usage()
        memory_usage = check_memory_usage()
        disk_usage = check_disk_usage()
        running_processes = check_running_processes()

        logging.info(f'CPU Usage: {cpu_usage}%, Memory Usage: {memory_usage}%, Disk Usage: {disk_usage}%, Running Processes: {running_processes}')

        
        time.sleep(60)

if __name__ == "__main__":
    monitor_system()

