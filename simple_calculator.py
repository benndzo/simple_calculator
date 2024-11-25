import tkinter as tk

class SimpleCalculator:
    def __init__(self):
        self.screen = tk.Tk()
        self.screen.geometry("400x500")
        self.screen.title("Simple Calculator")
        self.create_widgets()

    def create_widgets(self):
        self.result = tk.StringVar()

        # Entry to display the result
        self.result_display = tk.Entry(self.screen, textvariable=self.result, font=("Arial", 20), bd=10, relief="sunken", justify="right")
        self.result_display.grid(row=0, column=0, columnspan=4, pady=10)  # Add some padding at the top

        # Button layout
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        # Create number and operation buttons with colors
        for (text, row, col) in button_texts:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        if text == "C":
            button = tk.Button(self.screen, text=text, font=("Arial", 15), command=lambda: self.on_button_click(text), width=4, bg="red", fg="white")
        elif text == "=":
            button = tk.Button(self.screen, text=text, font=("Arial", 15), command=lambda: self.on_button_click(text), width=4, bg="blue", fg="white")
        elif text in ['+', '-', '*', '/']:
            button = tk.Button(self.screen, text=text, font=("Arial", 15), command=lambda: self.on_button_click(text), width=4, bg="gray", fg="white")
        else:
            button = tk.Button(self.screen, text=text, font=("Arial", 15), command=lambda: self.on_button_click(text), width=4)

        button.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, button_text):
        current_text = self.result.get()

        if button_text == "=":
            try:
                result = str(eval(current_text))
                self.result.set(result)
            except Exception as e:
                self.result.set("Error")
        elif button_text == "C":
            self.clear()
        else:
            self.result.set(current_text + button_text)

    def clear(self):
        self.result.set("")

    def run(self):
        self.screen.mainloop()

# Run the calculator app
app = SimpleCalculator()
app.run()
