import collections
import heapq

'''
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串。

思路:最大堆 , 不断存取
'''


class Solusion:

    def reorganizeString(self, S: str) -> str:
        dict = collections.Counter(S)
        if max(dict.values()) > (len(S) + 1) // 2:
            return ''
        head = []
        for k,v in dict.items():
            heapq.heappush(head,(-v,k))
        res = ''
        last = (0,None)
        while(head):
            cur = heapq.heappop(head)
            res += cur[1]
            cur = (cur[0]+1,cur[1])
            if last[0] < 0:
                heapq.heappush(head,last)
            last = cur
        return res


if __name__ == '__main__':
    print(Solusion().reorganizeString('aaab'))
