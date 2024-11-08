import time
from win10toast import ToastNotifier
import datetime

def getTimeInput(): 
    hour = int(input("Enter hours of interval: ")) 
    minutes = int(input("Enter minutes of interval: ")) 
    seconds = int(input("Enter seconds of interval: ")) 
    time_interval = seconds + (minutes * 60) + (hour * 3600) 
    return time_interval

def getBreakReason():
    reason = input("Enter the reason for this break (e.g., 'Water Break', 'Stretch Break'): ")
    return reason if reason else "Break"  # Default to "Break" if no input

def log(reason):
    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{reason} notification sent at: {start_time}")

def notify(reason):
    notification = ToastNotifier()
    notification.show_toast(reason, f"Time to take a {reason.lower()}!", duration=10)
    log(reason)

def start_timer(time_interval, reason):
    while True:
        time.sleep(time_interval)
        notify(reason)

if __name__ == "__main__":
    time_interval = getTimeInput()
    reason = getBreakReason()
    start_timer(time_interval, reason)
