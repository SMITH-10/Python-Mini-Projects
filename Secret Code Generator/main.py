
print("WELCOME TO SECRET PASSWORD GENERATOR \n")

# Define the alphabet, numbers, and symbols to be used in the Secret password generater.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '(', ')', '_', '*', '+']

# Define the Secret password generater function
def secret(start_text, shift_amount, password_direction):
    end_text = ""
    
    # Check if the secret password direction is 'decode', and adjust the shift amount accordingly.
    if password_direction == "decode":
        shift_amount *= -1
        
    # Iterate through each character in the input text
    for char in start_text:
        # Check if the character is in the alphabet
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        # Check if the character is a number
        elif char in numbers:
            position = numbers.index(char)
            new_position = position + shift_amount
            end_text += numbers[new_position]
        # Check if the character is a symbol
        elif char in symbols:
            position = symbols.index(char)
            new_position = position + shift_amount
            end_text += symbols[new_position]
            
    # Print the result based on the cipher direction
    print(f"Here's the {password_direction} result: {end_text}")

# Initialize a variable to control the loop
should_end = False
# Start a loop to allow multiple encryption/decryption operations

while not should_end:
    # Ask the user for the cipher direction (encode or decode)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
    # Ask the user for the message to be encrypted/decrypted
    text = input("Type your message:\n").lower()
    
    # Ask the user for the shift amount
    shift = int(input("Type the shift number:\n"))
    
    # Ensure the shift amount is within the range of the alphabet (0-25)
    shift = shift % 26
    
    # Call the secret function with the user inputs
    secret(start_text=text,shift_amount=shift,password_direction=direction)
    
    # Ask the user if they want to continue with another operation
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    
    # If the user doesn't want to continue, end the loop
    if restart == "no":
        should_end = True
        print("Goodbye")

