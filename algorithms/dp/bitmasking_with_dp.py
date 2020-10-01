#Python program to find number of ways to wear hats 
from collections import defaultdict 

class AssignCap: 

	# Initialize variables 
	def __init__(self): 

			self.allmask = 0

			self.total_caps = 100

			self.caps = defaultdict(list) 


	# Mask is the set of persons, i is the current cap number. 
	def countWaysUtil(self,dp, mask, cap_no): 
		
		# If all persons are wearing a cap so we 
		# are done and this is one way so return 1 
		if mask == self.allmask: 
			return 1

		# If not everyone is wearing a cap and also there are no more 
		# caps left to process, so there is no way, thus return 0; 
		if cap_no > self.total_caps: 
			return 0

		# If we have already solved this subproblem, return the answer. 
		if dp[mask][cap_no]!= -1 : 
			return dp[mask][cap_no] 

		# Ways, when we don't include this cap in our arrangement 
		# or solution set 
		ways = self.countWaysUtil(dp, mask, cap_no + 1) 
		
		# assign ith cap one by one to all the possible persons 
		# and recur for remaining caps. 
		if cap_no in self.caps: 

			for ppl in self.caps[cap_no]: 
				
				# if person 'ppl' is already wearing a cap then continue 
				if mask & (1 << ppl) : continue
				
				# Else assign him this cap and recur for remaining caps with 
				# new updated mask vector 
				ways += self.countWaysUtil(dp, mask | (1 << ppl), cap_no + 1) 

				ways = ways % (10**9 + 7) 

		# Save the result and return it 
		dp[mask][cap_no] = ways 

		return dp[mask][cap_no] 



	def countWays(self,N): 

		# Reads n lines from standard input for current test case 
		# create dictionary for cap. cap[i] = list of person having 
		# cap no i 
		for ppl in range(N): 

			cap_possessed_by_person = map(int, raw_input().strip().split()) 

			for i in cap_possessed_by_person: 

				self.caps[i].append(ppl) 

		# allmask is used to check if all persons 
		# are included or not, set all n bits as 1 
		self.allmask = (1 << N) -1

		# Initialize all entries in dp as -1 
		dp = [[-1 for j in range(self.total_caps + 1)] for i in range(2 ** N)] 

		# Call recursive function countWaysUtil 
		# result will be in dp[0][1] 
		print self.countWaysUtil(dp, 0, 1,) 

#Driver Program 
def main(): 
	No_of_people = input() # number of persons in every test case 

	AssignCap().countWays(No_of_people) 


if __name__ == '__main__': 
	main() 

# This code is contributed by Neelam Yadav 
