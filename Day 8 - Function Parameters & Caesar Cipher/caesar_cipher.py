from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encode(msg, shift):
    encoded_msg = ""
    for char in msg:
        if(char.islower()):
            encoded_msg += alphabet[((alphabet.index(char) + shift) % 26)]
        else:
            encoded_msg += char
    return encoded_msg


def decode(msg, shift):
    decoded_msg = ""
    for char in msg:
        if(char.islower()):
            decoded_msg += alphabet[alphabet.index(char) - (shift % 25)]
        else:
            decoded_msg += char
    return decoded_msg


print(logo)

while True:
    choice = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()

    if choice != "encode" and choice != "decode":
        print("Invalid choice")
        continue

    msg = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))

    if choice == 'encode':
        encoded_msg = encode(msg, shift)
        print(f"Here's the encoded result: {encoded_msg}")
    else:
        decoded_msg = decode(msg, shift)
        print(f"Here's the decoded result: {decoded_msg}")

    flag = input(
        "Type 'yes' if ypu want to go again. Otherwise type 'no'. \n").lower()

    if flag != 'yes':
        print("Goodbye")
        break
