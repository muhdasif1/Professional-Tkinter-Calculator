erase mistake 

# 🧮 Professional GUI Calculator using Python & Tkinter

A professional-grade, feature-rich calculator built with Python's Tkinter library. This desktop GUI application supports basic arithmetic and advanced mathematical functions, designed with a clean interface and intuitive user interaction.

---

## 📖 Description

This Python application is a GUI-based calculator that replicates the look and feel of a real calculator while offering functionality like:

- Basic arithmetic: addition, subtraction, multiplication, and division
- Advanced operations: factorials, square roots, exponents, parentheses, and modulus
- Clear and backspace functionality
- Error handling for invalid mathematical expressions

The calculator was created using only Python’s standard libraries (`tkinter`, `math`), ensuring easy portability and no external dependencies.

---

## 🎯 Features

- 🧮 **Basic Math**: `+`, `-`, `*`, `/`, `%`, `.`
- 📈 **Advanced Math**: 
  - Square root `√`
  - Factorial `!`
  - Power `x^y`
  - Parentheses `()`
- 🧹 **Utility Functions**:
  - `C` Clear all
  - `⌫` Backspace
  - `=` Evaluate expression
- 📉 **Error Handling**:
  - Handles invalid input (like `1/0`)
  - Invalid operations (like factorial of a float or negative number)

---

## 🧠 Code Overview
The calculator is structured using OOP principles with a class-based design:

🔹 Calculator Class
__init__: Initializes the GUI, sets window title and size, calls widget creation

create_widgets(): Dynamically generates buttons and input field

on_click(): Handles logic for all button presses

Handles math symbols (+, -, **, etc.)

Special buttons (C, ⌫, =, √, !)

calculate(): Evaluates the final expression using eval() and shows result

update_entry(): Updates the display text in the entry widget

---
## 🔹 GUI Layout
Built using tk.Frame and tk.Button

Button grid designed for intuitive calculator-like layout

Entry box at top for displaying and typing expressions

---
## 📸 Screenshot

<img width="395" alt="Screen Shot 2025-06-09 at 4 50 47 AM" src="https://github.com/user-attachments/assets/a854ccad-1fdd-4976-9661-3681dcf343ec" />

---

## 👨‍💻 Author
MUHAMMAD ASIF

📧 asifnasaaz2005@gmail.com

🔗 GitHub https://github.com/muhdasif1

