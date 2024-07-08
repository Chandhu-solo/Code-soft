import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import ttk
import time
import datetime
import threading
import os

# Ensure you have 'playsound' installed. If not, install it using: pip install playsound
class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")
        self.root.geometry("400x300")
        self.root.configure(bg="#ADD8E6")

        self.current_time_label = tk.Label(root, font=("Helvetica", 16), bg="#ADD8E6")
        self.current_time_label.pack(pady=10)
        self.update_clock()

        self.alarm_list = []

        self.add_alarm_button = tk.Button(root, text="Set New Alarm", command=self.set_new_alarm, bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 12))
        self.add_alarm_button.pack(pady=10)

        self.alarms_frame = tk.Frame(root, bg="#ADD8E6")
        self.alarms_frame.pack(pady=10)

        self.refresh_alarm_list()

    def update_clock(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_time_label.config(text=now)
        self.root.after(1000, self.update_clock)

    def set_new_alarm(self):
        alarm_time = simpledialog.askstring("Set Alarm", "Enter alarm time (HH:MM):")
        alarm_tone = simpledialog.askstring("Set Alarm Tone", "Enter path to alarm tone (or leave blank for default):")
        self.alarm_list.append({"time": alarm_time, "tone": alarm_tone, "status": True})
        self.refresh_alarm_list()

    def refresh_alarm_list(self):
        for widget in self.alarms_frame.winfo_children():
            widget.destroy()

        for alarm in self.alarm_list:
            alarm_frame = tk.Frame(self.alarms_frame, bg="#ADD8E6")
            alarm_frame.pack(fill="x", pady=2)

            alarm_label = tk.Label(alarm_frame, text=f"Alarm set for {alarm['time']}", bg="#ADD8E6", font=("Helvetica", 12))
            alarm_label.pack(side="left", padx=10)

            toggle_button = tk.Button(alarm_frame, text="On" if alarm["status"] else "Off", command=lambda a=alarm: self.toggle_alarm(a), bg="#4CAF50", fg="#FFFFFF", font=("Helvetica", 10))
            toggle_button.pack(side="right", padx=10)

    def toggle_alarm(self, alarm):
        alarm["status"] = not alarm["status"]
        self.refresh_alarm_list()

    def check_alarms(self):
        now = datetime.datetime.now().strftime("%H:%M")
        for alarm in self.alarm_list:
            if alarm["status"] and alarm["time"] == now:
                self.ring_alarm(alarm)
        self.root.after(60000, self.check_alarms)

    def ring_alarm(self, alarm):
        alarm["status"] = False
        self.refresh_alarm_list()


        snooze = messagebox.askyesno("Alarm Ringing", "Snooze the alarm?")
        if snooze:
            snooze_time = (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime("%H:%M")
            alarm["time"] = snooze_time
            alarm["status"] = True
            self.refresh_alarm_list()

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.after(1000, app.check_alarms)
    root.mainloop()
