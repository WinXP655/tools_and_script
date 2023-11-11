import os
import subprocess
import psutil

def list_processes():
    clear_screen()
    print("List of Processes:")
    for process in psutil.process_iter(attrs=["pid", "name"]):
        print(f"PID: {process.info['pid']} - Name: {process.info['name']}")
    input("Press Enter to continue...")
    show_menu()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def kill_process():
    clear_screen()
    print("Select process:")
    subprocess.call(["tasklist"])
    killproc = input("Process: ")
    clear_screen()
    print("Ending process:", killproc)
    subprocess.call(["taskkill", "/F", "/IM", killproc])
    input("Press Enter to continue...")
    show_menu()

def run_program():
    clear_screen()
    runprog = input("Run program: ")
    print("Executing program:", runprog)
    subprocess.Popen(runprog, shell=True)
    input("Press Enter to continue...")
    show_menu()

def shutdown_options():
    clear_screen()
    print("Select shutdown option:")
    print("1. Shutdown")
    print("2. Restart")
    print("3. Log off")
    print("4. Cancel")
    shut = input("Option: ")

    if shut == "1":
        os.system("shutdown /s /t 0")
    elif shut == "2":
        os.system("shutdown /r /t 0")
    elif shut == "3":
        os.system("shutdown /l")

    show_menu()

def show_menu():
    clear_screen()
    print("Task Manager")
    print("Running:", os.environ["COMPUTERNAME"], os.environ["USERNAME"])
    print("Time:", subprocess.check_output("date /t", shell=True).decode().strip(),
          subprocess.check_output("time /t", shell=True).decode().strip())
    print("1. Kill process")
    print("2. Run program")
    print("3. Shutdown options")
    print("4. List processes")
    print("5. Exit")
    ch = input("1-4: ")

    if ch == "1":
        kill_process()
    elif ch == "2":
        run_program()
    elif ch == "3":
        shutdown_options()
    elif ch == "5":
        exit()
    elif ch == "4":
        list_processes()

show_menu()