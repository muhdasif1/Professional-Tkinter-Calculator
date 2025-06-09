import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.expression = ""

        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.root, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
        self.entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)

        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '√', '='],
            ['x^y', '!', '(', ')']
        ]

        for row in buttons:
            frame = tk.Frame(self.root)
            frame.pack(expand=True, fill='both')
            for btn in row:
                tk.Button(
                    frame, text=btn, font=("Arial", 18),
                    command=lambda b=btn: self.on_click(b)
                ).pack(side="left", expand=True, fill='both')

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
            self.update_entry()
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.update_entry()
        elif char == '=':
            self.calculate()
        elif char == '√':
            try:
                result = math.sqrt(eval(self.expression))
                self.expression = str(result)
            except:
                self.expression = "Error"
            self.update_entry()
        elif char == '!':
            try:
                result = math.factorial(int(eval(self.expression)))
                self.expression = str(result)
            except:
                self.expression = "Error"
            self.update_entry()
        elif char == 'x^y':
            self.expression += '**'
            self.update_entry()
        else:
            self.expression += str(char)
            self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except Exception as e:
            self.expression = "Error"
        self.update_entry()

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
