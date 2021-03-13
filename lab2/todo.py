import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt


def imageInfo(image):
    img = mpimg.imread(image)
    #  show image detail
    print("The numbers of bytes in image is:\n", img.shape)
    # resized_image = cv2.resize(img, (500, 500))
    # plt.imshow(resized_image)
    # plt.show()
    res_image = img.copy()
    return res_image


def textToAscii(message):
    text = [ord(x) for x in message]
    return text


# res = []


def asciiToBin(ascii_text):
    # for i in ascii_text:
    #     r = '{0:08b}'.format(i)
    #     res.append(r)
    # return res
    return [format(i, "08b") for i in ascii_text]


def hideText(image, bin_mess):
    #  calculate the max bytes to encode
    amount_of_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("Max bytes to encode: ", amount_of_bytes)

    #  check if the number of bytes to encode is less than the max bytes in the image
    if len(bin_mess) > amount_of_bytes:
        raise ValueError("Too much! You need bigger image or smaller amount of text!")

    text_index = 0

    text_len = len(bin_mess)

    # find the length of text that needs to be hidden
    text_len = len(bin_mess)
    for values in image:
        for pixel in values:
            # convert rgb to bin
            r, g, b = asciiToBin(pixel)
            # modify the least significant bit only if there is still text to store
            if text_index < text_len:
                # hide the text into least significant bit of red pixel
                pixel[0] = int(r[:-1] + bin_mess[text_index], 2)
                text_index += 1
            if text_index < text_len:
                # hide the text into least significant bit of green pixel
                pixel[1] = int(g[:-1] + bin_mess[text_index], 2)
                text_index += 1
            if text_index < text_len:
                # hide the text into least significant bit of blue pixel
                pixel[2] = int(b[:-1] + bin_mess[text_index], 2)
                text_index += 1
            # if text is encoded => break out loop
            if text_index >= text_len:
                break
    return image
