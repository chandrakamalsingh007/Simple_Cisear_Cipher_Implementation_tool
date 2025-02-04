import tkinter as gui
from tkinter import messagebox

def input_text_analysis(input_text):
    letter_count = sum(char.isalpha() for char in input_text)
    digit_count = sum(char.isdigit() for char in input_text)
    special_char_count = len(input_text) - letter_count - digit_count

    analysis_summary = (f"Message Analysis:\n"
                        f"First and last characters: {input_text[:1]}***{input_text[-1]}\n"
                        f"Total characters: {len(input_text)}\n"
                        f"Letters: {letter_count}\n"
                        f"Digits: {digit_count}\n"
                        f"Special characters: {special_char_count if special_char_count > 0 else 'None'}")

    return analysis_summary

# transformation = either transformation or decryption
def transformation(input_text, shift_value, operation_mode='encrypt'):
    transformed_text = ""
    for char in input_text:
        if char.isalpha(): 
            shift_direction = shift_value if operation_mode == 'encrypt' else -shift_value
            shift_base = ord('A') if char.isupper() else ord('a')
            transformed_char = chr((ord(char) - shift_base + shift_direction) % 26 + shift_base)
            transformed_text += transformed_char
        else:
            transformed_text += char
    return transformed_text


def handle_operation():
    operation_mode = cipher_mode.get()
    user_text = input_text_field.get()
    # Check if the input text is empty
    if not user_text:
        messagebox.showerror("Error", "Input message cannot be empty. Please enter a message.")
        return

    # Check if shift value is valid
    try:
        
        shift_value = int(shift_value_field.get())

    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter a valid number.")
        return

    # Analyze the input message
    analysis_summary = input_text_analysis(user_text)

    # Encrypt or decrypt based on operation mode
    transformed_text = transformation(user_text, shift_value, operation_mode)

    # Show the encrypted/decrypted result
    result_text.delete(1.0, gui.END)
    result_text.insert(gui.END, f"Result: {transformed_text}")

    # Show analysis result
    analysis_label.delete(1.0, gui.END)  # Clear any previous analysis
    analysis_label.insert(gui.END, analysis_summary)  # Insert new analysis


def clear_all():
    input_text_field.delete(0, gui.END)
    shift_value_field.delete(0, gui.END)
    result_text.delete(1.0, gui.END)
    analysis_label.delete(1.0, gui.END)


# GUI setup
display = gui.Tk()
display.title("Implementation of Caesar Cipher Program")
display.geometry("500x500")

# Input text field
gui.Label(display, text="Enter Message:").pack()
input_text_field = gui.Entry(display, width=50)
input_text_field.pack()

# Shift value input
gui.Label(display, text="Enter Shift Value: ").pack()
shift_value_field = gui.Entry(display, width=15)
shift_value_field.pack()

# Cipher mode selection
cipher_mode = gui.StringVar(value='encrypt')
encryption = gui.Radiobutton(display, text="Encrypt", variable=cipher_mode, value='encrypt', fg='white', selectcolor='#555555')
decryption = gui.Radiobutton(display, text="Decrypt", variable=cipher_mode, value='decrypt', fg='white', selectcolor='#555555')

# pack the radio buttons
encryption.pack()
decryption.pack()
# Buttons
gui.Button(display, text="Process", command=handle_operation).pack()
gui.Button(display, text="Clear All", command=clear_all).pack()

# Result label
result_label = gui.Label(display, text="Result: ")
result_label.pack()

# Analysis text widget
analysis_label = gui.Text(display, height=6, width=50)
analysis_label.pack()

# Text widget for result
result_text = gui.Text(display, height=2, width=50)
result_text.pack()

# Start the GUI loop
display.mainloop()
