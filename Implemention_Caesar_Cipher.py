def encryption(input_text,shift_value):
    encrypted_text=""
    #check for all characters
    for char in input_text:
        #check if the character in encrypted text is a letter
        if char.isalpha(): 
            #check if the character is from upper case or lowercase
            shift_base= ord('A') if char.isupper() else ord('a')
            #perform the shift according to shift value and wrap around using modulo 
            encrypted_char= chr((ord(char)- shift_base+shift_value)%26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char # Non-alphabetic characters
    return encrypted_text

def decryption(input_text,shift_value):
    # Decrypting is just encrypting with the negative shift
    return encryption(input_text,-shift_value) 

def main():
    print("----------------- Implementation of Cisear Cipher ----------------")
    while True:
        choice = input("Would you like to (E)ncrypt, (D)crypt. or (Q)uit?").strip().upper()
        if choice =='Q':
            print("Goodbye!")
            break
        elif choice in ['E','D']:
            message = input("Enter your message:")
            shift = int(input("Enter the shift value (0-25): "))
            if choice == 'E':
                encrypted_message = encryption(message,shift)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'D':
                decrypted_message = decryption(message,shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose E, D, or Q.")


if __name__ == "__main__":
    main()