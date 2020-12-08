import re
import collections
from MPyt.fileT import *


class Model(object):

    def __init__(self):
        self.start = 0
        #包含end
        self.end = -1
        self.body = ''
        self.sons = []


def __spilt(content: str, start: int, end: int, notIn: str, left: str, right: str):
    uselessFlag = False
    m = Model()
    i = start
    while (i <= end):
        c = content[i]
        if c == notIn:
            uselessFlag = not uselessFlag
        if not uselessFlag:
            if c == left:
                son = __spilt(content, i + 1, end, notIn, left, right)
                son.body = left + son.body
                i = son.end
                m.sons.append(son)
            elif c == right:
                m.start = start
                m.end = i
                m.body = content[start:i + 1]
                break
        i += 1
    return m


test_str = "(ABC(BCD)CC(ccc)C)"


def spilt(content: str, left: str, right: str):
    return __spilt(content, 0, len(content) - 1, None, left, right)


if __name__ == '__main__':
    file = readFile("D:\Game\Hadis\Hades\Content\Scripts\TraitData.lua")
    res = spilt(file, '{', '}')
    print(res)
