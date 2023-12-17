import tkinter as tk

def on_click(button_value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(current) + str(button_value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display and input numbers
entry = tk.Entry(root, width=16, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, width=4, height=2, command=lambda btn=button: on_click(btn)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', width=4, height=2, command=clear_entry).grid(row=row_val, column=col_val)

# Equal button
tk.Button(root, text='=', width=4, height=2, command=calculate).grid(row=row_val, column=col_val + 1)

# Run the GUI
root.mainloop()