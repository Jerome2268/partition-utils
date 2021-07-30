import random


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


#
# def GBK2312():
#     head = random.randint(0xb0, 0xf7)
#     body = random.randint(0xa1, 0xfe)
#     val = f'{head:x} {body:x}'
#     str = bytes.fromhex(val).decode('gb2312')
#     return str

def get_num():
    return random.randint(5, 9)


def get_id():
    s = []
    for i in range(get_num()):
        s.append(Unicode())

    return "".join(s)


if __name__ == '__main__':

    for i in range(10000):
        print(get_id())
