import random
import time
from hashlib import sha256

from partition.file_parser.reader import read
from partition.utils.constants import seed, group


def get_seed(bit):
    num = [chr(i) for i in range(48, 58)]

    return "".join(random.sample(num, bit))


def pseudonymize(field):
    return sha256(field.encode() + get_seed(seed).encode()).hexdigest()[:20]


def distinct(li):
    s = set(li)
    for i in s:
        if i.isspace():
            s.remove(i)
    return list(s)


def partition(path):
    li = read(path)
    p = list(map(lambda s: (s, pseudonymize(s)), distinct(li)))
    (p.__len__())
    pseu = sorted(p, key=lambda s: s[1])
    length = len(pseu)
    s = divmod(length, group)
    step = s[0]
    mod = s[1]
    sed = 0
    res = []
    arr = get_random_list(1, group, mod)
    for i in range(group):
        res.append((i + 1, list(map(lambda a: a[0], pseu[sed:(sed + step)]))))
        sed = sed + step
    # for i in range(pseu.__len__()):
    #     print("index %s , member %s " % (str(i), pseu[i][0]))
    #     print("======================================")
    #
    # for i in res:
    #     print("group %s,  member %s , count %s人 " % (i[0],
    #                                                  ",".join(i[1]),
    #                                                  str(i[1].__len__())
    #                                                  ))
    # print("======================================")

    for i in range(arr.__len__()):
        # index = len - mod +i
        index = length - mod + i
        g = arr[i]
        res[g - 1][1].append(pseu[index][0])
    for i in res:
        print("group %s,  member %s , count %s人 " % (i[0],
                                                     ",".join(i[1]),
                                                     str(i[1].__len__())
                                                     ))

    return res


def get_random_list(start, stop, n):
    '''
    生成范围在[start,stop], 长度为n的数组.
    区间包含左右endpoint
    '''
    arr = list(range(start, stop + 1))
    shuffle_n(arr, n)
    return arr[-n:]


def shuffle_n(arr, n):
    random.seed(time.time())
    for i in range((arr.__len__() - 1), (arr.__len__() - n - 1), -1):
        j = random.randint(0, i)
        arr[i], arr[j] = arr[j], arr[i]
