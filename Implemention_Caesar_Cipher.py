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


def encryption(input_text,shift_value, operation_mode ='encrypt'):
    encrypted_text=""
    #check for all characters
    for char in input_text:
        #check if the character in encrypted text is a letter
        if char.isalpha(): 
            #check if the character is from upper case or lowercase
            shift_direction = shift_value if operation_mode == 'encrypt' else -shift_value
            shift_base = ord('A') if char.isupper() else ord('a')
            #perform the shift according to shift value and wrap around using modulo 
            encrypted_char= chr((ord(char)- shift_base + shift_direction) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char # Non-alphabetic characters
    return encrypted_text

# def decryption(input_text,shift_value,operation_mode ='decrypt'):
#     # Decrypting is just encrypting with the negative shift
#     return encryption(input_text,-shift_value) 

def handle_operation():
    operation_mode = cipher_mode.get()
    user_text = input_text_field.get()
    try: 
        shift_value = int(shift_value_field.get())
    except valueError:
        messagebox.showerror("Error", "Invalid shift value.Please enter a valid number.")
        return

    analysis_summary = input_text_analysis(user_text)
    encrypted_text = encryption(user_text,shift_value,operation_mode)

    result_label.config(text=f"Result: {encrypted_text}")
    analysis_label.config(text=analysis_summary)

#GUI setup 
display = gui.Tk()
display.title("Implementation of Cisear Cipher Program")
display.geometry("500x350")

gui.Label(display, text="Enter Message:").pack()
input_text_field = gui.Entry(display,width=60)
input_text_field.pack()

gui.Label(display, text="Enter Shift Value:\n For Encryption use +ve \n Decryption use -ve\n").pack()
shift_value_field = gui.Entry(display, width=15)
shift_value_field.pack()

cipher_mode = gui.StringVar(value='encrypt')
gui.Radiobutton(display, text="Encrypt", variable=cipher_mode, value='encrypt')
gui.Radiobutton(display, text="Decrypt", variable=cipher_mode, value='decrypt')

gui.Button(display, text="Process", command=handle_operation).pack()

result_label = gui.Label(display, text="Result: ")
result_label.pack()

analysis_label=gui.Label(display,text="")
analysis_label.pack()

display.mainloop()
