import collections

'''

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

//求和0的数量

'''

class Solusion:

    def fourSumCount(self, A: [int], B: [int], C: [int], D: [int]) -> int:
        dict = collections.Counter(u+v for u in A for v in B)
        return sum([ dict[-u-v] for u in C for v in D if  dict[-u-v]])


if __name__ == '__main__':
    print(Solusion().fourSumCount([-1,1,1,1,-1],[0,-1,-1,0,1],[-1,-1,1,-1,-1],[0,1,0,-1,-1]))