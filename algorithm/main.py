import collections
import heapq

'''

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。
为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。
//求和0的数量

'''

class Solusion:

    def leastInterval(self, tasks: [str], n: int) -> int:
        map = collections.Counter(tasks)
        maxLen = max(map.values())
        time = len([ v for v in  map.values() if v == maxLen])
        return max(len(tasks),(maxLen-1)*(n+1)+time)



if __name__ == '__main__':
    a = [[1,2],[3,4],[5,6]]
    print(a)