import tkinter as tk
from tkinter import filedialog, messagebox

from main import validate_input, output_to_text
from converter import to_utf8, to_utf16, to_utf32
from translator import from_utf8, from_utf16, from_utf32

root = tk.Tk()
root.title('Unicode Converter and Translator')

frame_io = tk.Frame(root)
frame_io.pack(pady=10)

# Input Field
label_input = tk.Label(frame_io, text='Input:')
label_input.pack(side=tk.LEFT, padx=(0, 10))
entry_input = tk.Entry(frame_io, width=30)
entry_input.pack(side=tk.LEFT)

# Operation Selection (Convert or Translate)
operation_var = tk.StringVar(value="convert")
radiobutton_convert = tk.Radiobutton(root, text="Convert", variable=operation_var, value="convert")
radiobutton_convert.pack()
radiobutton_translate = tk.Radiobutton(root, text="Translate", variable=operation_var, value="translate")
radiobutton_translate.pack()

# Format Selection for Conversion/Translation
format_var = tk.StringVar(value="UTF-8")
formats = [("UTF-8", "UTF-8"), ("UTF-16", "UTF-16"), ("UTF-32", "UTF-32")]
for text, mode in formats:
    button = tk.Radiobutton(root, text=text, variable=format_var, value=mode)
    button.pack(anchor=tk.W)

# Checkbox for output to text file
output_var = tk.BooleanVar()
checkbox_output = tk.Checkbutton(root, text="Output to text file", variable=output_var)
checkbox_output.pack()

# Result Label
label_result = tk.Label(root, text="Result:")
label_result.pack()

# Text Field for Result Display
text_result = tk.Text(root, height=5, width=50)
text_result.pack()
text_result.config(state=tk.DISABLED)

def execute():
    input_value = entry_input.get().upper()
    if not validate_input(input_value):
        messagebox.showerror("Error", "Invalid Input")
        return
    
    operation = operation_var.get()
    format_sel = format_var.get()
    should_output = output_var.get()
    result = "Error"

    # Determine the operation and format, then execute the appropriate function
    if operation == "convert":
        if format_sel == "UTF-8":
            result = to_utf8(input_value)
        elif format_sel == "UTF-16":
            result = to_utf16(input_value)
        elif format_sel == "UTF-32":
            result = to_utf32(input_value)
    elif operation == "translate":
        if format_sel == "UTF-8":
            result = from_utf8(input_value)
        elif format_sel == "UTF-16":
            result = from_utf16(input_value)
        elif format_sel == "UTF-32":
            result = from_utf32(input_value)


    text_result.config(state=tk.NORMAL)
    text_result.delete('1.0', tk.END)
    text_result.insert(tk.END, result)
    
    if should_output:
        filename = output_to_text(input_value, (operation, format_sel), result)
        text_result.insert(tk.END, f"\n\nFilename: {filename}")
    
    text_result.config(state=tk.DISABLED)

# Execute Button
button_execute = tk.Button(root, text="Execute", command=execute)
button_execute.pack(pady=10)

root.mainloop()