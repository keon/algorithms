#Minimum Waiting Time
#Time O(nLogn) for sorting array nlogn time takes and for keep tracking
#it takes n time so total nlogn + n so simply negates nlogn since n is less than nlogn
#So time O(N) and Space O(1) since we don't use extra space here

def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
	totalWaitingTime=0
	for idx,duration in enumerate(queries):
		queriesLeft=len(queries)-(idx+1)
		totalWaitingTime+=duration*queriesLeft
	return totalWaitingTime	
