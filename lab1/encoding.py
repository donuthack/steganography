import os

'''convert message into array of int'''


def textToAscii(message):
    lst = [ord(ch) for ch in message]
    return lst


p = []


def int2Binary(lst):
    for i in lst:
        r = '{0:08b}'.format(i)
        p.append(r)
    # print(4, type(p))
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
    container_words = ''
    zero_gap = " "  # 0 => " "
    one_gap = "  "  # 1 => "  "
    a = " ".join(str(x) for x in text)  # from list to string
    x = a.split()  # string split to list
    for i in x:
        container_words += str(i)
    # print(4, type(res))

    '''take string of binary code message'''
    binary_string = ' '
    for i in binCode:
        binary_string += str(i)

    '''check if our container with text can hold a hidden message'''
    if len(binary_string) > len(container_words):
        return print("Container doesn't has enough place for hidding message")

    # '''hide our binary-looking message in container by adding " " or "  " as a word'''
    # for i in binary_string:
    #     if i == "1":
    #         word = container_words[i]


