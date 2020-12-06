import collections
import heapq

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。


思路: 本题很简单 , 但解法可以非常巧妙
'''

class Solusion:

    def leastInterval(self, tasks: [str], n: int) -> int:
        map = collections.Counter(tasks)
        maxLen = max(map.values())
        time = len([ v for v in  map.values() if v == maxLen])
        return max(len(tasks),(maxLen-1)*(n+1)+time)



if __name__ == '__main__':
    for i in range(10):
        print(200+i*400,end=',')
