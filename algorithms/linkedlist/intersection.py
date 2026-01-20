"""
   This function takes two lists and returns the node they have in common, if any.
   In this example:
   1 -> 3 -> 5
               \
                7 -> 9 -> 11
               /
   2 -> 4 -> 6
   ...we would return 7.
   Note that the node itself is the unique identifier, not the value of the node.
   """
import unittest




class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None


def intersection(h1, h2):
    flags = [False for i in range(9)]

    count = 0
    flag = None
    h1_orig = h1
    h2_orig = h2

    while h1 or h2: ## 1
        flags[0] = True
        count += 1

        if not flag and (h1.next is None or h2.next is None): ## 3
            flags[1] = True
            # We hit the end of one of the lists, set a flag for this
            flag = (count, h1.next, h2.next)

        if h1: #5
            flags[2] = True
            h1 = h1.next
        if h2: #6
            flags[3] = True
            h2 = h2.next

    long_len = count    # Mark the length of the longer of the two lists
    short_len = flag[0]

    if flag[1] is None: #7
        flags[4] = True
        shorter = h1_orig
        longer = h2_orig
    elif flag[2] is None: #8
        flags[5] = True
        shorter = h2_orig
        longer = h1_orig

    while longer and shorter: #9
        flags[6] = True

        while long_len > short_len: #10
            flags[7] = True
            # force the longer of the two lists to "catch up"
            longer = longer.next
            long_len -= 1

        if longer == shorter: #11
            flags[7] = True
            
           
            print(len(list(filter(lambda x:(x == True) ,  flags))) / len(flags))
           
     
          
            return longer ##12
        else: ## 13
            flags[8] = True
            longer = longer.next
            shorter = shorter.next
    print(flags)
    # branch_coverage = len(flags) / len(filter(lambda x:(x == True) ,  flags))
    # print(branch_coverage)
    return None




    

def test_intersection():

    # create linked list as:
    # 1 -> 3 -> 5
    #            \
    #             7 -> 9 -> 11
    #            /
    # 2 -> 4 -> 6
    a1 = Node(1)
    b1 = Node(3)
    c1 = Node(5)
    d = Node(7)
    a2 = Node(2)
    b2 = Node(4)
    c2 = Node(6)
    e = Node(9)
    f = Node(11)

    a1.next = d
    b1.next = d
    c1.next = d
    a2.next = d
    b2.next = d
    c2.next = d
    d.next = d
    e.next = d
    intersection(a1, a2)

    


if __name__ == '__main__':

   

    test_intersection()


    # unittest.main()
