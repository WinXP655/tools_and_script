import tkinter as tk


class Calculator():
    def __main__(self, master):
        self.master = master
        master.title("Calc")

        self.result = 0
        self.current = 0
        self.new_sum = True
        self.operation = None

        self.display = tk.Entry(master, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        button_list = {
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        }
        r = 1
        c = 0
        for label in button_list:
            button = tk.Button(master, text=label, width=5, height=2, font=("Arial", 12))
            button.grid(row=r, column=c, padx=5, pady=5)
            button.bind("<Button-1>", self.button_press)
            c += 1
            if c > 3:
                c = 0
                r += 1

        clear_button = tk.Button(master, text="C", width=5, height=2, font=("Arial", 12))
        clear_button.grid(row=5, column=0, padx=5, pady=5)
        clear_button.bind("<Button-1>", self.clear)

    def button_press(self, event):
        text = event.widget.cget("text")

        if text.isdigit() or text == ".":
            if self.new_num:
                self.display.delete(0, tk.END)
                self.new_num = False
            self.display.insert(tk.END, text)
        else:
            if self.operation is not None:
                self.calculate()
            self.operation = text
            self.result = float(self.display.get())
            self.new_num = True

    def calculate(self):
        if self.operation == "+":
            self.result += float(self.display.get())
        elif self.operation == "-":
            self.result -= float(self.display.get())
        elif self.operation == "*":
            self.result *= float(self.display.get())
        elif self.operation == "/":
            self.result /= float(self.display.get())
        self.display.delete(0, tk.END)
        self.display.insert(0, self.result)
        self.new_num = True

    def clear(self, event):
        self.result = 0
        self.current = 0
        self.new_num = True
        self.operation = False
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')


root = tk.Tk()
calc = Calculator(root)
root.mainloop()
