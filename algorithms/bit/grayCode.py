class Solution:
    def recursive(self,n):
        if n==1:
            return ['0','1']
        res=self.recursive(n-1)
        myres=[]
# each time we are getting solution off n-1
# then we are adding 0 in front of each solution

        for i in range(len(res)):
            s='0'+res[i]
            myres.append(s)
# then we are traversing it reverse and adding 1 to each bit
        for i in range(len(res)-1,-1,-1):
            s=res[i]
            myres.append('1'+s)
        return myres


    def grayCode(self, n: int):
        # print(self.recursive(n))
        lst=self.recursive(n)
        for i in range(len(lst)):
            lst[i]=int(lst[i],2)
        return lst