def kmp(text, pattern):
        m, n = len(text), len(pattern)
        pi = [0 for i in range(m)]

        j = 0
        # making pi table -> finding the longest prefix that is also a suffix
        # Examples - P = ABCDABD π = (0, 0, 0, 0, 1, 2, 0)
        for i in range(1, n):
            while j and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
                pi[i] = j

        # finding pattern in text
        j = 0
        ret = []
        for i in range(m):
            while j and text[i] != pattern[j]:
                j = pi[j - 1]
            if text[i] == pattern[j]:
                j += 1
                if j == n:
                    ret.append(i - n + 1)
                    j = pi[j - 1]
                    
        return ret