import tkinter as tk
from math import *

# ----------------------------
# Window
# ----------------------------
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("450x650")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""

# ----------------------------
# Functions
# ----------------------------
def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)

def clear():
    global expression
    expression = ""
    display_var.set("")

def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except:
        display_var.set("Error")
        expression = ""

# ----------------------------
# Display
# ----------------------------
display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 24),
    bd=8,
    relief="sunken",
    bg="white",
    justify="right"
)

display.pack(fill="both", padx=10, pady=15, ipady=20)

# ----------------------------
# Buttons
# ----------------------------
buttons = [
    ['C','⌫','(',')'],
    ['7','8','9','/'],
    ['4','5','6','*'],
    ['1','2','3','-'],
    ['0','.','=','+'],
    ['sin(','cos(','tan(','sqrt('],
    ['log(','log10(','pi','e'],
    ['**','%','//','pow(']
]

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame, bg="#1e1e1e")
    row_frame.pack(expand=True, fill="both")

    for btn in row:
        if btn == "=":
            command = calculate
        elif btn == "C":
            command = clear
        elif btn == "⌫":
            command = backspace
        elif btn == "pi":
            command = lambda b=btn: press("pi")
        elif btn == "e":
            command = lambda b=btn: press("e")
        else:
            command = lambda b=btn: press(b)

        tk.Button(
            row_frame,
            text=btn,
            font=("Arial",16,"bold"),
            width=6,
            height=2,
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            command=command
        ).pack(side="left", padx=4, pady=4)

root.mainloop() 





