import collections
import heapq

'''
给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。

思路:  将其想象成一个矩形 , 分两种情况分析 , 1.字母种类大于停止时间 2.字母种类小于等待时间
'''

class Solusion:

    def leastInterval(self, tasks: [str], n: int) -> int:
        map = collections.Counter(tasks)
        maxLen = max(map.values())
        time = len([ v for v in  map.values() if v == maxLen])
        return max(len(tasks),(maxLen-1)*(n+1)+time)



if __name__ == '__main__':
    print(Solusion().leastInterval(["A","A","A","B","B","B"],
2
))
