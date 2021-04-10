from todo import *


def Steganography():
    a = input("Image Steganography \n 1. Encode the data \n 2. Decode the data \n Your input is: ")
    userinput = int(a)
    if userinput == 1:
        print("\nEncoding....")
        encode_text()

    elif userinput == 2:
        print("\nDecoding....")
        print("Decoded message is " + decode_text())
    else:
        raise Exception("Enter correct input")


Steganography()  # encode image
