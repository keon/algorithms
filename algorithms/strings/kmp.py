import time
class KMP:
    def part(self, pattern):
        ret = [0]
        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            if pattern[j] == pattern[i]:
                ret.append(j+1)
            else:
                ret.append(j)
        return ret
        
    def search(self, txt, find):
        part, ret, j = self.part(find), [], 0
        
        for i in range(len(txt)):
            while j > 0 and txt[i] != find[j]:
                j = part[j - 1]
            if txt[i] == find[j]:
                j += 1
            if j == len(find): 
                ret.append(i - (j - 1))
                j = 0
        if ret:
            print "String found at "
            for i in ret:
                print i,
        else:
            print "not found"
    
obj=KMP()
txt=raw_input("Enter the input string ")
find=raw_input("Enter the string to be found ")
a=time.clock()
obj.search(txt,find)
print "\n Time taken is "+str(time.clock()-a)
