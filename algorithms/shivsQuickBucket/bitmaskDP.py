# 473. Matchsticks to Square

class Solution:
    def makesquare(self, matches) -> bool:
        n, side = len(matches), sum(matches) // 4                         # Precomputing the required side for a square
        
        if sum(matches) % 4 or max(matches) > side: return False          # matches array is invalid
        
        
        self.cache = {}                                                   # will be used for memoization
        
        # this helper function has the remaining side ('s') to be formed, already made number of sides ('k') and
        # the mask stores the number of values from matches already taken (sort of like visited)
        
        def helper(k, s, mask):
            if (k, s, mask) in self.cache: return self.cache[(k, s, mask)] # if we have seen these values lets not compute them again
            if k == 4: return True                                         # if we reach here we have made a square so return true
            
            if not s:                                                      # if we exhaust a side there needs to be a search initiated for the next side
                self.cache[(k, s, mask)] = helper(k + 1, side, mask)       # store the new result in cache
                return self.cache[(k, s, mask)]
            
            for i in range(n):
                if mask & (1 << i) or matches[i] > s: continue             # if we have already taken a number or that number is not suitable skip it
                self.cache[(k, s, mask)] = helper(k, s - matches[i], mask ^ (1 << i))
                if self.cache[(k, s, mask)]: return True                   # if in future we find this to make a square then return true from here
            
            return False
        return helper(0, side, 0)