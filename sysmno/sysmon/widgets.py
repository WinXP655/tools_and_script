from datetime import datetime
from tkinter import *
from functools import partial
import os

import psutil as psu
from uptime import boottime


class GUI:
    def __init__(self, master):
        self.master = Frame(master, padx=10, pady=10)
        self.master.grid()

        self.whitespace_height = 12

        if os.name == "nt":
            self.time_format = "%#I:%M:%S %p"
        else:
            self.time_format = "%-I:%M:%S %p"

        self.gui_widget_metrics = [
            Label(self.master, text="CPU (%):"),
            Label(self.master, text="Memory (%):"),
            Label(self.master, text="Uptime:"),
            Label(self.master, text="System Clock:"),
            Label(self.master, text="Boot Time:"),
            Frame(self.master, height=self.whitespace_height),
            Button(self.master, text="Exit", command=master.quit)
        ]

        self.on_top_check = IntVar(value=1)
        self.gui_widget_values = [
            Label(self.master, text="{}".format(psu.cpu_percent())),
            Label(self.master, text="{}".format(psu.virtual_memory()[2])),
            Label(self.master, text=str(datetime.now() - boottime())[:-7]),
            Label(self.master, text=datetime.now().strftime("{}".format(self.time_format))),
            Label(self.master, text="{}".format(boottime().strftime("%b %d %Y, {}".format(self.time_format)))),
            Frame(self.master, height=self.whitespace_height),
            Checkbutton(master=self.master, text="Always On Top", variable=self.on_top_check, command=partial(self.update_on_top, master))
        ]

        for index, label in list(enumerate(self.gui_widget_metrics)):
            if index == 6:
                label.grid(sticky="nsew", row=index, column=0, padx=(8, 0))
            else:
                label.grid(sticky="w", row=index, column=0, padx=(8, 0), pady=(1, 0))

        for index, label in list(enumerate(self.gui_widget_values)):
            if index == 6:
                label.grid(sticky="nsew", row=index, column=1, padx=(16, 8))
            else:
                label.grid(sticky="w", row=index, column=1, padx=(16, 8), pady=(1, 0))

        master.after(1000, self.get_metrics)

    def get_metrics(self):
        cpu = psu.cpu_percent()
        memory = psu.virtual_memory()[2]
        uptime_var = (str(datetime.now() - boottime())[:-7])
        time = datetime.now().strftime("{}".format(self.time_format))

        self.gui_widget_values[0].configure(text=cpu)
        if cpu >= 90.0:
            self.gui_widget_values[0].configure(fg="red")
        else:
            self.gui_widget_values[0].configure(fg="black")

        self.gui_widget_values[1].configure(text=memory)
        if memory >= 90.0:
            self.gui_widget_values[1].configure(fg="red")
        else:
            self.gui_widget_values[1].configure(fg="black")
            
        if memory >= 60.0:
            self.gui_widget_values[1].configure(fg="yellow")
        else:
            self.gui_widget_values[1].configure(fg="black")

        self.gui_widget_values[2].configure(text=uptime_var)

        self.gui_widget_values[3].configure(text=time)

        self.master.after(1000, self.get_metrics)

    def update_on_top(self, root):
        if self.on_top_check.get() == 1:
            root.attributes("-topmost", "true")
        else:
            root.attributes("-topmost", "false")
