import tkinter as tk
from tkinter import ttk, messagebox
import os
import shutil
import psutil
import subprocess
from tkinter.font import Font

# Function to clear temporary files
def clear_temp_files():
    temp_dirs = [
        os.getenv("TEMP"),
        os.path.join(os.getenv("USERPROFILE"), "AppData", "Local", "Temp"),
    ]
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            for filename in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, filename)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    messagebox.showinfo("Success", "Temporary files cleared!")

# Function to disable startup programs
def disable_startup_programs():
    try:
        subprocess.run(["msconfig"], shell=True)
        messagebox.showinfo("Info", "Disable unnecessary programs in the Startup tab.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open msconfig: {e}")

# Function to optimize power settings (Medium Performance)
def optimize_power_settings():
    try:
        subprocess.run(["powercfg", "/setactive", "8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c"], shell=True)  # High-performance plan
        messagebox.showinfo("Success", "Power settings optimized for performance!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to optimize power settings: {e}")

# Function to activate Ultimate Performance
def activate_ultimate_performance():
    try:
        # Enable Ultimate Performance plan
        subprocess.run(["powercfg", "-duplicatescheme", "e9a42b02-d5df-448d-aa00-03f14749eb61"], shell=True)
        # Set Ultimate Performance as active
        subprocess.run(["powercfg", "/setactive", "e9a42b02-d5df-448d-aa00-03f14749eb61"], shell=True)
        messagebox.showinfo("Success", "Ultimate Performance plan activated!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to activate Ultimate Performance: {e}")

# Function to kill unnecessary processes
def kill_processes():
    for proc in psutil.process_iter():
        try:
            if proc.name() in ["unnecessary_process.exe"]:  # Add processes to kill
                proc.kill()
        except Exception as e:
            print(f"Failed to kill process {proc.name()}: {e}")
    messagebox.showinfo("Success", "Unnecessary processes killed!")

# GUI Setup
root = tk.Tk()
root.title("PC Booster")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# Custom Font
custom_font = Font(family="Helvetica", size=12)

# Header Label
header_label = ttk.Label(root, text="PC Booster", font=("Helvetica", 20, "bold"), background="#f0f0f0")
header_label.pack(pady=20)

# Buttons with Icons (Placeholder for icons)
button_style = ttk.Style()
button_style.configure("TButton", font=custom_font, padding=10)

clear_temp_button = ttk.Button(root, text="Clear Temporary Files", command=clear_temp_files, style="TButton")
clear_temp_button.pack(pady=10)

disable_startup_button = ttk.Button(root, text="Disable Startup Programs", command=disable_startup_programs, style="TButton")
disable_startup_button.pack(pady=10)

optimize_power_button = ttk.Button(root, text="Optimize Power Settings (Medium)", command=optimize_power_settings, style="TButton")
optimize_power_button.pack(pady=10)

ultimate_performance_button = ttk.Button(root, text="Activate Ultimate Performance", command=activate_ultimate_performance, style="TButton")
ultimate_performance_button.pack(pady=10)

kill_processes_button = ttk.Button(root, text="Kill Unnecessary Processes", command=kill_processes, style="TButton")
kill_processes_button.pack(pady=10)

# Footer Label
footer_label = ttk.Label(root, text="© 2025 PC Booster. All rights reserved.", font=("Helvetica", 8), background="#f0f0f0")
footer_label.pack(side="bottom", pady=10)

# Run the app
root.mainloop()