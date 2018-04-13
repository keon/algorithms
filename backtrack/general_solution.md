
# Backtracking
A backtracking algorithm tries to build a solution to a computational problem incrementally.Whenever the algorithm needs to decide between multiple alternatives to the next component of the solution, it simply tries all possible options recursively.

# General Pattern
[Reference](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/03-backtracking.pdf)
1. Find a small choice whose correct answer would reduce the problem size.
2. For each possible answer, temporarily adopt that choice and recurse. (Don’t try to be clever about which choices to try; just try them all.)
3. The recursive subproblem is often more general than the original target problem; in each recursive subproblem, we must consider only solutions that are consistent with the choices we have already made

# Sample Code Pattern
```python
def solve(configuration conf):
    if (no more choices):
        // BASE CASE
        return (conf is goal state);
    
    for (all available choices):
        # Mark
        try one choice c;

        # Recurse
        ok = Solve(conf with choice c made);
        
        # Unmark
        unmake choice c;
        if (ok):
            return True;
    return False; // tried all choices, no soln found
```

# References
* [Notes from Prof Jeff Erickson, UIUC](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/03-backtracking.pdf)
* [Notes from Prof Julie Zelenski, Stanford](https://see.stanford.edu/materials/icspacs106b/h19-recbacktrackexamples.pdf)


# Sample Problems
This general code pattern/structure might apply to many other backtracking questions. In the following section, the structure is demonstrated for
  * Subsets
    * [Subsets I](#subsets-i)
    * [Subsets II](#subsets-ii)
  * Permutations
    * [Permutations I](#permutations-i)
    * [PermutationsII](#permutations-ii)
  * Combination Sum
    * [Combination Sum I](#combination-sum-i)
    * [Combination Sum II](#combination-sum-ii)
  * Palindrome partitions
    * [Palindrome Partitioning](#palindrome-partitioning)

## Subsets I
https://leetcode.com/problems/subsets/
```python
def subsets(nums):
    res = [] 
    temp = []
    nums.sort()
    backtrack(res, temp, nums, 0);
    return res

def backtrack(res, temp, nums, start):
    res.append(temp[:]) # creating a copy of temp and appending
    for i in range(start, len(nums)):

        # Mark
        temp.append(nums[i]);

        # Recurse
        backtrack(res, temp, nums, i + 1);

        # Unmark
        temp.pop()
```

## Subsets II 
(contains duplicates)
https://leetcode.com/problems/subsets-ii/
```python
def subsets_with_duplicates(nums):
    res = [] 
    temp = []
    nums.sort()
    backtrack(res, temp, nums, 0);
    return res

def backtrack(res, temp, nums, start):
    res.append(temp[:]) # creating a copy of temp and appending
    for i in range(start, len(nums)):
        if (i > start and nums[i] == nums[i-1]):
            continue
        # Mark
        temp.append(nums[i]);

        # Recurse
        backtrack(res, temp, nums, i + 1);

        # Unmark
        temp.pop()
```

## Permutations I
https://leetcode.com/problems/permutations/
```python
def permute(nums):
    res = [] 
    temp = []
    visited = [False for _ in range(len(nums))]
    nums.sort()
    backtrack(res, temp, nums, visited);
    return res

def backtrack(res, temp, nums, visited):
    if len(temp) == len(nums):
        res.append(temp[:]) # creating a copy of temp and appending
        return
    for i in range(len(nums)):
        if visited[idx]:
            continue

        # Mark
        visited[idx] = True
        temp.append(nums[i]);

        # Recurse
        backtrack(res, temp, nums, visited);

        # Unmark
        temp.pop()
        visited[idx] = False
```

## Permutations II
(contains duplicates)
https://leetcode.com/problems/permutations-ii/
```python

def permute_with_duplicates(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        visited = [False for _ in range(len(nums))]
        nums.sort()
        backtrack(nums, len(nums), visited, temp, res)
        return res

def backtrack(nums, lnums, visited, temp, res):
    if len(temp) == lnums:
        res.append(temp[:]) # creating a copy of temp and appending
        return
    for idx in range(lnums):
        if visited[idx]:
            continue
        if idx and nums[idx-1] == nums[idx] and not visited[idx-1]:
            continue

        # Mark
        visited[idx] = True
        temp.append(nums[idx])

        # Recurse
        backtrack(nums, lnums, visited, temp, res)

        # Unmark
        temp.pop()
        visited[idx] = False
```

## Combination Sum I
https://leetcode.com/problems/combination-sum/
```python
def combination_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        helper(nums, target, 0, temp, res)
        return res
        
def helper(nums, target, pos, temp, res):
    csum = sum(temp)
    if target < csum:
        return
    if target == csum:
        res.append(temp[:]) # creating a copy of temp and appending
        return
    for idx in range(pos, len(nums)):
        # Mark
        temp.append(nums[idx])

        # Recurse
        helper(nums, target, idx, temp, res)

        # Unmark
        temp.pop()
```

## Combination Sum II
(can't reuse same element)
https://leetcode.com/problems/combination-sum-ii/
```python
def combinationSum2(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        nums.sort()
        backtrack(nums, target, 0, temp, 0, res)
        return res

def backtrack(nums, target, pos, temp, csum, res):
    csum = sum(temp)
    if target < csum:
        return
    if target == csum:
        res.append(temp[:]) # creating a copy of temp and appending
        return
    for idx in range(pos, len(nums)):
        if idx > pos and nums[idx] == nums[idx-1]:
            continue

        # Mark
        temp.append(nums[idx])

        # Recurse
        helper(nums, target, idx+1, temp, csum+nums[idx], res)

        # Unmark
        temp.pop()
```

## Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
```python
def palindrome_partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    is_palin = get_palindrome_matrix(s)
    res = []
    temp = []
    s = [c for c in s]
    backtrack(s, len(s), 0, is_palin, temp, 0, res)
    return res

def get_palindrome_matrix(s):
    s = [ c for c in s]
    slen = len(s)
    n = slen
    res = [[False for _ in range(slen)] for _ in range(slen)]
    for i in range(n-1, -1, -1):
        for j in range(i, n):
          if i == j:
            res[i][j] = True
            continue
          if j == i + 1:
            res[i][j] = s[i] == s[j]
            continue
          if s[i] == s[j] and res[i+1][j-1]:
            res[i][j] = True
    return res
        
def backtrack(s, slen, idx, is_palin, temp, temp_len, res):
    if idx > slen:
        return
    if temp_len == slen:
        res.append(temp[:]) # creating a copy of temp and appending
        return
    for i in range(idx, slen):
        if not is_palin[idx][i]:
            continue
        part = ''.join(map(str, s[idx:i+1]))
        
        # Mark
        temp.append(part)
        temp_len += len(part)
        
        # Recurse
        backtrack(s, slen, i+1, is_palin, temp, temp_len, res)
        
        # Unmark
        temp_len -= len(part)
        temp.pop()
```
