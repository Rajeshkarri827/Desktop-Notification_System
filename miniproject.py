import time
from win10toast import ToastNotifier
import datetime
import tkinter as tk
from tkinter import messagebox

def log(reason):
    now = datetime.datetime.now()
    start_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{reason} notification sent at: {start_time}")

def notify(reason):
    notification = ToastNotifier()
    notification.show_toast(reason, f"Time to take a {reason.lower()}!", duration=10)
    log(reason)

def start_timer(time_interval, reason):
    def timer():
        while True:
            time.sleep(time_interval)
            notify(reason)

    import threading
    threading.Thread(target=timer, daemon=True).start()

def start_app():
    try:
        hour = int(hour_var.get())
        minute = int(minute_var.get())
        second = int(second_var.get())
        reason = reason_var.get()
        if not reason:
            reason = "Break"

        time_interval = second + (minute * 60) + (hour * 3600)
        if time_interval <= 0:
            messagebox.showerror("Invalid Input", "Time interval must be greater than zero.")
        else:
            messagebox.showinfo("Timer Started", f"{reason} timer started!")
            start_timer(time_interval, reason)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for the time interval.")

root = tk.Tk()
root.title("Break Reminder")

tk.Label(root, text="Enter Hours:").grid(row=0, column=0, padx=10, pady=5)
hour_var = tk.StringVar()
tk.Entry(root, textvariable=hour_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Minutes:").grid(row=1, column=0, padx=10, pady=5)
minute_var = tk.StringVar()
tk.Entry(root, textvariable=minute_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Seconds:").grid(row=2, column=0, padx=10, pady=5)
second_var = tk.StringVar()
tk.Entry(root, textvariable=second_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Reason for Break:").grid(row=3, column=0, padx=10, pady=5)
reason_var = tk.StringVar()
tk.Entry(root, textvariable=reason_var).grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Start Timer", command=start_app).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
