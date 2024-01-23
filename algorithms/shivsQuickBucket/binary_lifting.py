import math
class BL:
    def __init__(self, n, parent):
        # up stores 2^ith parent
        self.height = 1 + int(math.log2(n))
        self.up = [[-1] * (self.height) for _ in range(n)]
        # update parents first and then go for higher order parents preprocessing
        for j in range(self.height):
            for i in range(n):
                if j == 0: 
                    self.up[i][0] = parent[i]
                    continue
                elif self.up[i][j - 1] != -1:
                    self.up[i][j] = self.up[self.up[i][j - 1]][j - 1]

    # Function to return the Kth ancestor of V
    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1: 
            i = int(math.log2(k))
            node = self.up[node][i]
            k -= (1 << i)
        return node 