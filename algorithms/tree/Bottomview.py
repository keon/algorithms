def print_bottom_of_binary_tree(root):   
      d = dict()
     
      printBottomViewUtil(root, d, 0, 0)
      for i in sorted(d.keys()):
        print(d[i][0], end = " ")
 
def bottomview(root, d, hd, level):
     if root is None:
        return
   
if hd in d:
        if level >= d[hd][1]:
            d[hd] = [root.data, level]
else:
        d[hd] = [root.data, level]
         
bottomview(root.left, d, hd - 1,level + 1)
bottomview(root.right, d, hd + 1,level + 1)