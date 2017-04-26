'''
lps returns the length of longest palindromic subsequence in a string by maintaining a table that stores solution for substrings
'''

def lps(str):

	def get_lps(i,j,str,table):
		if i>j:
			return 0
		elif i==j:
			return 1
		elif table[i][j]!=-1:
			return table[i][j]
		for k in range(i,j):
			if str[k]==str[j]:
				table[i][j] = max(get_lps(i,j-1,str,table),2+get_lps(k+1,j-1,str,table))
				return table[i][j]
		table[i][j] = get_lps(i,j-1,str,table)
		return table[i][j]

	table = [[-1 for x in range(len(str))]]*(len(str))
	return get_lps(0,len(str)-1,str,table)
