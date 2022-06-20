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


def encode(message):
    message = message.upper()
    encoded = ""
    for char in message:
        if char in morse_dict:
            encoded += morse_dict[char] + " "
    return encoded


def decode(message):
    decoded = ""
    cipher = message.split(" ")
    for char in cipher:
        key_list = list(morse_dict.keys())
        value_list = list(morse_dict.values())
        try:
            position = value_list.index(char)
        except ValueError:
            return ""
        letter = key_list[position]
        decoded += letter
    return decoded


print(logo)
print("Welcome to Morse Code Converter!")

if __name__ == "__main__":
    while True:
        choice = input("Please type 'encode' to encrypt a message into Morse Code\n"
                       "Please type 'decode' to decode Morse Code into plain text.\n")
        if choice == 'encode':
            text = input("Type your message: ")
            morse_code = encode(text)
            print(f"Your message in Morse Code: {morse_code}")
        elif choice == 'decode':
            text = input("Type your message: ")
            decoded_text = decode(text)
            print(f"Your message translated to: {decoded_text}")
        else:
            choice = input("Please type 'encode' to encrypt a message into Morse Code\n"
                           "Please type 'decode' to decode Morse Code into plain text. ")
