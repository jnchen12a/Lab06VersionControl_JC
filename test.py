# Encoding function
def encode(num):
    pass
# Decoding function
def decode(num):
    pass

# Start of main if dunder
if __name__ == '__main__':
    # Start of main while loop
    while True:
        print('Menu')
        print('-----------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        choice = int(input('Please enter an option: '))
        if choice == 1: # Encode a password
            password = int(input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        elif choice == 2: # Decode a password
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
        elif choice == 3: # Quitting out
            quit()
        else: # Bozo check
            print('Please enter a valid choice.')
    # End of main while loop
# End of main if dunder