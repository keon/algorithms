'''
Given a list of tuples(w,v) lst, and maximum weight - bag,
	w - weight
	v - value
of items, knapsack(lst) returns a solution to the Knapsack problem,
i.e it returns a list of items which maximize the value within the maximum weight constraint.
'''

def knapsack(lst,bag):
	def get_knapsack(lst,bag,table):
		if bag<=0:
			return 0
		if str(bag) in table:
			v,itm = table[str(bag)]
			return int(v)
		max_v = 0
		max_itm = (-1,-1)
		for itm in lst:
			if itm[0] <= bag:
				temp_v = get_knapsack(lst,bag-itm[0],table)
				if temp_v + itm[1] > max_v:
					max_v = temp_v + itm[1]
					max_itm = itm
		table[str(bag)] = (max_v,max_itm)
		return max_v
	table = {}
	val = get_knapsack(lst,bag,table)
	sol = []
	while(str(bag) in table and table[str(bag)][0]>0):
		sol.append(table[str(bag)][1])
		bag -= table[str(bag)][1][0]
	return (val,sol)

print(knapsack([(3,5),(2,1)],8))

