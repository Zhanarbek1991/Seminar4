from mytree import BSTMap

folder = open('words_48.txt','r')
lines=folder.readlines()

treeInst = BSTMap()
treeInst._bstInsert(lines, 1, 2)
treeInst._bstDelete()
treeInst._bstMinimum( )

print(treeInst.printer())
    
#for l in lines:
 #   print(l)
#for l in range(0, 561):
    
    
