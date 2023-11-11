import os
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import psutil  # Import the psutil library for process information

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kill_process():
    process_name = process_entry.get()
    clear_screen()
    subprocess.call(["taskkill", "/f", "/im", process_name])
    messagebox.showinfo("Task Manager", f"Process '{process_name}' has been terminated.")
    process_entry.delete(0, tk.END)

def run_program_in_terminal(program_path):
    subprocess.run(program_path, shell=True)

def shutdown_options(option):
    if option == "shutdown":
        os.system("shutdown /s /t 0")
    elif option == "restart":
        os.system("shutdown /r /t 0")
    elif option == "logoff":
        os.system("shutdown /l")

def show_shutdown_options():
    shutdown_window = tk.Toplevel(root)
    shutdown_window.resizable(False, False)
    shutdown_window.title("Shutdown Options")
    shutdown_label = tk.Label(shutdown_window, text="Select shutdown option:", bg="#0078D7", fg="#FFFFFF")
    shutdown_label.pack()
    shutdown_buttons = [
        ("Shutdown", "shutdown"),
        ("Restart", "restart"),
        ("Log Off", "logoff")
    ]
    for label, option in shutdown_buttons:
        tk.Button(shutdown_window, text=label, bg="#F0F0F0", command=lambda o=option: shutdown_options(o)).pack(fill=tk.X)
    close_button = tk.Button(shutdown_window, text="Close", bg="#F0F0F0", command=shutdown_window.destroy)
    close_button.pack(fill=tk.X)

# Function to update the process list
def update_process_list():
    process_listbox.delete(0, tk.END)
    for proc in psutil.process_iter(['pid', 'name']):
        process_listbox.insert(tk.END, f"PID: {proc.info['pid']} - {proc.info['name']}")

root = tk.Tk()
root.resizable(False, False)
root.title("Task Manager")
root.configure(bg="#0078D7")

menu_label = tk.Label(root, text="Task Manager", bg="#0078D7", fg="#FFFFFF", font=("Tahoma", 12))
menu_label.pack()

process_label = tk.Label(root, text="Enter process name:", bg="#0078D7", fg="#FFFFFF")
process_label.pack()

process_entry = tk.Entry(root)
process_entry.pack(fill=tk.X)

kill_button = tk.Button(root, text="Kill Process", command=kill_process, bg="#F0F0F0")
kill_button.pack(fill=tk.X)

program_label = tk.Label(root, text="Enter program path:", bg="#0078D7", fg="#FFFFFF")
program_label.pack()

program_entry = tk.Entry(root)
program_entry.pack(fill=tk.X)

run_button = tk.Button(root, text="Run Program", command=lambda: run_program_in_terminal(program_entry.get()), bg="#F0F0F0")
run_button.pack(fill=tk.X)

shutdown_button = tk.Button(root, text="Shutdown Options", command=show_shutdown_options, bg="#F0F0F0")
shutdown_button.pack(fill=tk.X)

exit_button = tk.Button(root, text="Exit", command=root.quit, bg="#F0F0F0")
exit_button.pack(fill=tk.X)

process_list_window = tk.Toplevel(root)
process_list_window.title("Process List")

process_listbox = tk.Listbox(process_list_window)
process_listbox.pack(fill=tk.BOTH, expand=True)

refresh_button = tk.Button(process_list_window, text="Refresh List", command=update_process_list, bg="#F0F0F0")
refresh_button.pack(fill=tk.X)

update_process_list()  # Initial update of process list

root.mainloop()