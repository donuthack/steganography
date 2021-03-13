from encoding import *


question = input("What do you want: hide message('h') or find message('f')?\n")
if question == "h":
    message = input("Enter message what you want to hide:\n")

    # text to ASCII
    encoded_text = textToAscii(message)
    print(encoded_text)

    # ASCII  to binary
    bin_text = int2Binary(encoded_text)
    print(bin_text)

    # scan container if there is any text
    text = scanContainer("/Users/workplace/Desktop/stegano/lab1/container.txt")
    print(text)

    # hide message
    hide = hideMessage(bin_text, text)
    hiddenToFile(hide)

elif question == "f":
    # scan for availability of hidden message
    hidden_text = scanContainer("/Users/workplace/Desktop/stegano/lab1/hiddenMessage.txt")

    # try to find hidden message
    a = listToStr(hidden_text)

    decoded = findMessage(a)
    print("Hidden message found:")
    print(decoded)
else:
    print("Please, choose right mode for me")
