import os

'''convert message into array of int'''


def textToAscii(message):
    lst = [ord(x) for x in message]
    return lst


p = []


def int2Binary(lst):
    for i in lst:
        r = '{0:08b}'.format(i)
        p.append(r)
    return p


def listToStr(message):
    res = ""
    return res.join(message)


def scanContainer(file):
    text = ""
    with open(file, 'r') as f:
        size = os.path.getsize(file)
        if size == 0:
            print("File is empty, i cant do anyting:c")
        else:
            lines = f.read()
            text += lines
    return text


def hideMessage(binCode, text):
    ukrainian_letters = "асеіорхАВСЕНІКОРТХ"
    english_letters = "aceiopxABCEHIKOPTX"

    '''take string of binary code message'''
    binary_string = ""
    for i in binCode:
        binary_string += i

    '''check if our container with text can hold a hidden message'''
    if len(binary_string) > len(text):
        print("Container doesn't has enough place for hidding message")

    i = 0
    encoded_message = ""
    letter = ""
    for char in text:
        if char in ukrainian_letters:
            if i < len(binary_string):
                if str(binary_string[i]) == "1":
                    index = ukrainian_letters.index(char)
                    print(4, index, char)
                    letter = str(english_letters[index])
                    print(7, letter)
                elif str(binary_string[i]) == "0":
                    letter = char
                i += 1
            else:
                letter = char
        else:
            letter = char

        encoded_message += letter

    return encoded_message


def hiddenToFile(text_to_write):
    file_name = 'hiddenMessage.txt'
    f = open(file_name, 'w')
    f.write(text_to_write + '\n')
    f.close()


def listToStr(text):
    res = ""
    return res.join(text)


def binToAscii(codes):
    ints = [int(item, 2) for item in codes]
    return ints


def AsciToText(ints):
    res = "".join(chr(x) for x in ints)
    return res


def findMessage(hidden_text):
    ukrainian_letters = "асеіорхАВСЕНІКОРТХ"
    english_letters = "aceiopxABCEHIKOPTX"

    code = ""
    codes = []  # array of binaries of our text
    for i in hidden_text:  # go through all text
        print(5, i)
        if len(code) == 8:
            if code == "00000000":
                break
            codes.append(code)
            code = ""
        if i in english_letters:
            print(str(i))
            code += "1"
        elif i in ukrainian_letters:
            print(6, str(i))
            code += "0"
    print(8, codes)

    arr_of_ascii = binToAscii(codes)
    res = AsciToText(arr_of_ascii)
    return res
