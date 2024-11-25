import tkinter as tk

def button_click(number):
    """Append the clicked number or operator to the entry widget."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    """Clear the entry widget."""
    entry.delete(0, tk.END)

def erase():
    """Delete the last character from the entry widget."""
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    """Evaluate the expression in the entry widget."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the expression
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

# Button layout
buttons = [
    ("C", 1, 0, "lightcoral", clear), ("⌫", 1, 1, "lightblue", erase), ("/", 1, 2, "lightgray", lambda: button_click("/")), ("*", 1, 3, "lightgray", lambda: button_click("*")),
    ("7", 2, 0, "white", lambda: button_click("7")), ("8", 2, 1, "white", lambda: button_click("8")), ("9", 2, 2, "white", lambda: button_click("9")), ("-", 2, 3, "lightgray", lambda: button_click("-")),
    ("4", 3, 0, "white", lambda: button_click("4")), ("5", 3, 1, "white", lambda: button_click("5")), ("6", 3, 2, "white", lambda: button_click("6")), ("+", 3, 3, "lightgray", lambda: button_click("+")),
    ("1", 4, 0, "white", lambda: button_click("1")), ("2", 4, 1, "white", lambda: button_click("2")), ("3", 4, 2, "white", lambda: button_click("3")), ("=", 4, 3, "lightgreen", calculate),
    ("0", 5, 0, "white", lambda: button_click("0")), (".", 5, 1, "white", lambda: button_click(".")),
]

# Create and place buttons
for (text, row, col, color, command) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), bg=color, command=command)
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Adjust grid weights for even scaling
for i in range(6):  # 6 rows (including the entry row)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
