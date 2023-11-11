from widgets import *


# MAIN
def main():
    root = Tk()
    root.geometry("+400+200")
    root.resizable(False, False)
    root.title("System Monitor")
    root.attributes("-topmost", "true")
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
