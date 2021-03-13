from todo import *


answer = str(input("You want hide message(h) or find message(f)?\n"))

if answer == "h":
    message = input("Enter message what you want to hide:\n")
    # if len(message) == 0:
    #     raise ValueError("You didn't enter any data")

    # text to ascii
    ascii_text = textToAscii(message)
    print(ascii_text)

    # ascii to bin
    bin_text = asciiToBin(ascii_text)
    print(bin_text)

    image = input("Enter you image name with extension:\n")
    i = imageInfo(image)
    print(i)

    # hide text in image
    filename = input("Enter name of new encoded image with extension:\n")
    encoded_image = hideText(i, bin_text)
    cv2.imwrite(filename, encoded_image)
    print(encoded_image)

elif answer == "f":
    print("im ready to find")
else:
    print("choose right mode:c")
