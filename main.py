from logo import logo

morse_dict = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/', '': ''}


def encrypt(message):
    morse_code = ""
    for char in message:
        morse_code += morse_dict[char] + " "
    print(f"Your message in Morse Code: {morse_code}")


def decode(message):
    decoded_text = ""
    cipher = message.split(" ")
    for char in cipher:
        key_list = list(morse_dict.keys())
        value_list = list(morse_dict.values())
        position = value_list.index(char)
        letter = key_list[position]
        decoded_text += letter
    print(f"Your message translated to: {decoded_text}")


print(logo)
print("Welcome to Morse Code Converter!")

while True:
    choice = input("Please type 'encode' to encrypt a message into Morse Code\n"
                   "Please type 'decode' to decode Morse Code into plain text.\n")
    if choice == 'encode':
        text = input("Type your message: ").upper()
        encrypt(text)
    elif choice == 'decode':
        text = input("Type your message: ").upper()
        decode(text)
    else:
        choice = input("Please type 'encode' to encrypt a message into Morse Code\n"
                       "Please type 'decode' to decode Morse Code into plain text. ")




