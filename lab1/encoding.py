import os


def listToStr(message):
    res = ""
    return res.join(message)


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


text = []


def scanContainer(file):
    with open(file, 'r') as f:
        size = os.path.getsize(file)
        if size == 0:
            print("File is empty, i cant do anyting:c")
        else:
            lines = f.readlines()
            for a in lines:
                text.append(a)
    return text


def hideMessage(binCode, text):
    one_gap = " "  # 0 => " "
    double_gap = "  "  # 1 => "  "
    list_to_string = " ".join(str(x) for x in text)  # from list to string
    container_text = list_to_string.split()  # string split to list

    '''take string of binary code message'''
    binary_string = ""
    for i in binCode:
        binary_string += i

    '''check if our container with text can hold a hidden message'''
    if len(binary_string) > len(container_text):
        print("Container doesn't has enough place for hidding message")

    '''hide our binary-looking message in container by adding " " or "  " as a word'''
    word = ""
    for i in range(len(binary_string)):
        if str(binary_string[i]) == "0":
            word += str(container_text[i]) + one_gap
        else:
            word += str(container_text[i]) + double_gap
    return word


def hiddenToFile(text):
    file_name = 'hiddenMessage.txt'
    f = open(file_name, 'a+')  # open file in append mode
    f.write(text + '\n')
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


def findMessage(text):
    code = ""
    codes = []
    for i in range(len(text)):
        if i + 1 != len(text):
            if len(code) == 8:
                codes.append(code[0:8])
                code = ""
            if text[i] + text[i + 1] == "  ":
                code = code + "1"
            elif (i > 0) and text[i] + text[i - 1] != "  " and text[i] == " ":
                code = code + "0"
    ints = binToAscii(codes)
    res = AsciToText(ints)
    return res
