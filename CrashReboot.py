import psutil
import subprocess
import time

# Replace "your_app_name" with the actual name of the application you want to monitor
APP_NAME = "your_app_name"

def is_app_running(app_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == app_name:
            return True
    return False

def reboot_system():
    print("Rebooting the system...")
    # You can replace "shutdown /r /t 0" with the appropriate command for your operating system
    # For Windows, the above command will initiate a system restart immediately.
    subprocess.run(["shutdown", "/r", "/t", "0"])

if __name__ == "__main__":
    while True:
        if not is_app_running(APP_NAME):
            print(f"The {APP_NAME} app has crashed.")
            reboot_system()
        time.sleep(5)  # Adjust the time interval as needed (in seconds)
