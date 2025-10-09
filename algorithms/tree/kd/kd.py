from __future__ import annotations
import json
import math
import sys
from typing import List

# Datum class.
class Datum():
    def __init__(self,
                 coords : tuple[int],
                 code   : str):
        self.coords = coords
        self.code   = code
    def to_json(self) -> str:
        dict_repr = {'code':self.code,'coords':self.coords}
        return(dict_repr)

# Internal node class.
class NodeInternal():
    def  __init__(self,
                  splitindex : int,
                  splitvalue : float,
                  leftchild,
                  rightchild):
        self.splitindex = splitindex
        self.splitvalue = splitvalue
        self.leftchild  = leftchild
        self.rightchild = rightchild

# Leaf node class.
class NodeLeaf():
    def  __init__(self,
                  data : List[Datum]):
        self.data = data

# KD tree class.
class KDtree():
    def  __init__(self,
                  k    : int,
                  m    : int,
                  root = None):
        self.k    = k
        self.m    = m
        self.root = root

    # For the tree rooted at root, dump the tree to stringified JSON object and return.
    def dump(self) -> str:
        def _to_dict(node) -> dict:
            if isinstance(node,NodeLeaf):
                return {
                    "p": str([{'coords': datum.coords,'code': datum.code} for datum in node.data])
                }
            else:
                return {
                    "splitindex": node.splitindex,
                    "splitvalue": node.splitvalue,
                    "l": (_to_dict(node.leftchild)  if node.leftchild  is not None else None),
                    "r": (_to_dict(node.rightchild) if node.rightchild is not None else None)
                }
        if self.root is None:
            dict_repr = {}
        else:
            dict_repr = _to_dict(self.root)
        return json.dumps(dict_repr,indent=2)

    # Insert the Datum with the given code and coords into the tree.
    # The Datum with the given coords is guaranteed to not be in the tree.
    def insert(self,point:tuple[int],code:str):
      self.insertAux(point,code,self.root)

    def insertAux(self,point:tuple[int],code:str,curr):
        if (curr is None): 
            datum = Datum(coords=point, code=code)
            curr = NodeLeaf(data=[datum])
        if (self.root is None): #empty tree
            self.root = curr
        elif isinstance(curr,NodeLeaf):
            if len(curr.data) < self.m:
                datum = Datum(coords=point, code=code)
                curr.data.append(datum)
            else: #split
                datum = Datum(coords=point, code=code)
                curr.data.append(datum)
                maxS_idx = self.calcMaxSpread(curr.data)
                coordSorted = sorted(curr.data, key=lambda datum: self.get_kth_coord(datum, maxS_idx))
                # for d in coordSorted:
                #     print(d.coords)
                median = -1
                n = len(coordSorted)
                if n % 2 == 1:
                    median = float(coordSorted[n // 2].coords[maxS_idx])
                else:
                    left = coordSorted[n // 2 - 1].coords[maxS_idx]
                    right = coordSorted[n // 2].coords[maxS_idx]
                    median = float((left + right)/2)
                leftchild = NodeLeaf(data=coordSorted[0:n//2])
                rightchild = NodeLeaf(data=coordSorted[n//2:])
                splitNode = NodeInternal(splitindex=maxS_idx, splitvalue=median, leftchild=leftchild, rightchild=rightchild)
                if (self.root == curr):
                    self.root = splitNode
                else:
                    return splitNode    
        else: #traverse to leaf node
            if (point[curr.splitindex] < curr.splitvalue):
                if (isinstance(curr.leftchild, NodeLeaf)) and (len(curr.leftchild.data) == self.m):
                    curr.leftchild = self.insertAux(point,code,curr.leftchild)
                else:
                    self.insertAux(point,code,curr.leftchild)
            else:
                if (isinstance(curr.rightchild, NodeLeaf)) and (len(curr.rightchild.data) == self.m):
                    curr.rightchild = self.insertAux(point,code,curr.rightchild)
                else:
                    self.insertAux(point,code,curr.rightchild)

    def get_kth_coord(self,datum, k):
        return datum.coords[k]

    def calcMaxSpread(self,datums:List):
        maxSpread = 0
        maxIdx = -1
        #find the max of each dimension
        max = 0
        min = sys.maxsize*2+1
        for k in range(0,self.k):
            for m in range (0,self.m+1):
                if (max < datums[m].coords[k]):
                    max = datums[m].coords[k]
                if (min > datums[m].coords[k]):
                    min = datums[m].coords[k]
            spread = max - min
            max = 0
            min = sys.maxsize*2+1
            if maxSpread < spread:
                maxSpread = spread
                maxIdx = k
        return maxIdx
    def findParent(self,curr,target,point:tuple[int]):
        if isinstance(curr, NodeInternal):
            if (curr.leftchild == target):
                return [curr, 'l']
            if (curr.rightchild == target):
                return [curr, 'r']
            else:
                if (point[curr.splitindex] < curr.splitvalue):
                    return self.findParent(curr.leftchild,target,point)
                else:
                    return self.findParent(curr.rightchild,target,point)

    # Delete the Datum with the given point from the tree.
    # The Datum with the given point is guaranteed to be in the tree.
    def delete(self,point:tuple[int]):
        parent_target = self.findSplitNode(point, self.root)
        r = 'r'

        if (parent_target[1] == r):
            if len(parent_target[0].rightchild.data) == 1:
                parent = self.findParent(self.root, parent_target[0],point)
                if parent == None:
                    self.root = parent_target[0].leftchild
                    return self.root
                if isinstance(parent_target[0].leftchild, NodeLeaf):
                    newLeaf = NodeLeaf(data=parent_target[0].leftchild.data)
                    if parent[1] == 'l':
                        parent[0].leftchild = newLeaf 
                    else:
                        parent[0].rightchild = newLeaf
                else:
                    splitidx = parent_target[0].leftchild.splitindex
                    splitval = parent_target[0].leftchild.splitvalue
                    right = parent_target[0].leftchild.rightchild
                    left = parent_target[0].leftchild.leftchild
                    newSplit = NodeInternal(splitindex=splitidx, splitvalue=splitval, rightchild=right, leftchild=left)
                    if parent[1] == 'l':
                        parent[0].leftchild = newSplit 
                    else:
                        parent[0].rightchild = newSplit
            else:
                for d in (parent_target[0].rightchild.data):
                    if (d.coords == point):
                        return parent_target[0].rightchild.data.remove(d)        
        elif parent_target[1] == 'l':
            if len(parent_target[0].leftchild.data) == 1:
                parent = self.findParent(self.root, parent_target[0],point)
                if parent == None:
                    self.root = parent_target[0].rightchild
                    return self.root
                if isinstance(parent_target[0].rightchild, NodeLeaf):
                    newLeaf = NodeLeaf(data=parent_target[0].rightchild.data)
                    if parent[1] == 'l':
                        parent[0].leftchild = newLeaf 
                    else:
                        parent[0].rightchild = newLeaf
                else:
                    splitidx = parent_target[0].rightchild.splitindex
                    splitval = parent_target[0].rightchild.splitvalue
                    right = parent_target[0].rightchild.rightchild
                    left = parent_target[0].rightchild.leftchild
                    newSplit = NodeInternal(splitindex=splitidx, splitvalue=splitval, rightchild=right, leftchild=left)
                    if parent[1] == 'l':
                        parent[0].leftchild = newSplit 
                    else:
                        parent[0].rightchild = newSplit
            else:
                for d in (parent_target[0].leftchild.data):
                    if (d.coords == point):
                        return parent_target[0].leftchild.data.remove(d)
        else:
             for d in (self.root.data):
                    if (d.coords == point):
                        return self.root.data.remove(d)            

    def findSplitNode(self,point:tuple[int],curr):
        if isinstance(curr, NodeLeaf):
            return [self.root, 'n']
        if (point[curr.splitindex] < curr.splitvalue):
            if isinstance(curr.leftchild, NodeLeaf):
                return [curr, 'l']
            else:
                return self.findSplitNode(point, curr.leftchild)
        else:
            if isinstance(curr.rightchild, NodeLeaf):
                return [curr, 'r']
            else:
                return self.findSplitNode(point, curr.rightchild)
            
    def knn(self,k:int,point:tuple[int]) -> str:
        leaveschecked = 0
        knnlist = []
        lc = []
        self.knnAux(k, point, lc, knnlist, self.root)
        leaveschecked = len(lc)
        return(json.dumps({"leaveschecked":leaveschecked,"points":[datum.to_json() for datum in knnlist]},indent=2))
    
    def knnAux(self,k,point,lc,knn,curr):
        if isinstance(curr, NodeLeaf):
            # self.printKnn(knn)
            lc.append(curr)
            unworked = curr.data.copy()
            while len(unworked) > 0:
                currKnnD = 0
                closestD = sys.maxsize*2+1
                code = ""
                datum = None
                dsquared = 0
                for d in unworked: #find closest coord in curr datum
                    idx = 0
                    dsquared = 0
                    dsquared = self.distance(d, point)
                    if closestD > dsquared:
                        closestD = dsquared
                        code = d.code
                        datum = d
                    elif closestD == dsquared:
                        if d.code < code:
                            closestD = dsquared
                            datum = d
                if len(knn) == k: #if points in leaf are better
                    currKnnD = 0
                    for i in range(0, len(knn)):
                        currKnnD = self.distance(knn[i], point)
                        if closestD < currKnnD:
                            knn.insert(i,datum)
                            if len(knn) > k:
                                knn.pop(-1)
                            break
                        elif closestD == currKnnD:
                            if code < knn[i].code:
                                knn.insert(i,datum)
                                if len(knn) > k:
                                    knn.pop(-1)
                                break
                if len(knn) == 0:
                    knn.append(datum)
                    unworked.remove(datum)
                    continue
                oldlen = len(knn)
                if len(knn) < k and len(knn) > 0: #if list is not full
                    currKnnD = 0
                    for d in knn:
                        currKnnD = self.distance(d, point) #compute currknnd
                        if closestD < currKnnD:
                            knn.insert(knn.index(d),datum)
                            break
                        elif closestD == currKnnD:
                            if code < d.code:
                                knn.insert(knn.index(d),datum)
                                break
                    if oldlen == len(knn):
                        knn.append(datum)
                #self.printKnn(knn)
                unworked.remove(datum)
        else:
            if len(knn) > 0:
                furthestD = self.distance(knn[-1], point)
            leftBB = self.calcBB(curr.leftchild, point)
            if len(leftBB) == self.k * 2:
                leftBB = self.compress(leftBB)
            rightBB = self.calcBB(curr.rightchild, point)
            if len(rightBB) == self.k * 2:
                rightBB = self.compress(rightBB)
            leftBBDist = self.distanceBB(leftBB, point)
            rightBBDist = self.distanceBB(rightBB, point)
            closest = -1
            closestSubTree = None
            other = None
            if leftBBDist <= rightBBDist:
                closest = leftBBDist
                closestSubTree = curr.leftchild
                other = curr.rightchild
                otherBBD = rightBBDist
            else:
                closest = rightBBDist
                closestSubTree = curr.rightchild
                other = curr.leftchild
                otherBBD = leftBBDist
            if len(knn) > 0:
                furthestD = self.distance(knn[-1], point)
            if len(knn) < k or closest <= furthestD:
                self.knnAux(k,point,lc,knn,closestSubTree)
            if len(knn) > 0:
                furthestD = self.distance(knn[-1], point)
            if len(knn) < k or otherBBD <= furthestD:
                self.knnAux(k,point,lc,knn,other)
    
    def distance(self,knnD,point):
        dsquared = 0
        idx = 0
        for c in knnD.coords:
            dsquared += (c - point[idx])**2
            idx+=1
        return dsquared
    
    def calcBB(self,curr,point):
        minMax = []
        for k in range(0,self.k):
            kmin = sys.maxsize*2+1
            kmax = 0
            self.findkthminMax(k,curr,kmin,kmax,minMax)
        return minMax
        
        
    def findkthminMax(self,k,curr,kmin,kmax,minMax):
        if isinstance(curr, NodeLeaf):
            for d in curr.data:
                if kmin > d.coords[k]:
                    kmin = d.coords[k]
                if kmax < d.coords[k]:
                    kmax = d.coords[k]
            if k < len(minMax):
                if kmin < minMax[k][0]:
                    minMax[k][0] = kmin
                if kmax > minMax[k][1]:
                    minMax[k][1] = kmax
                return minMax
            return minMax.append([kmin,kmax])
        self.findkthminMax(k, curr.leftchild, kmin, kmax, minMax)
        self.findkthminMax(k, curr.rightchild, kmin, kmax, minMax)

    def distanceBB(self,BB,point):
        k = 0
        dsquared = 0
        for c in point:
            if c < BB[k][0]:
                dsquared += (BB[k][0] - c)**2
            if c > BB[k][1]:
                dsquared += (c - BB[k][1])**2
            k+=1
        return dsquared
        
    def compress(self,BB):
        newBB = []
        for i in range(0,len(BB)//2):
            rPair = BB[i*2+1]
            lPair = BB[i*2]
            min = None
            max = None
            if rPair[0] < lPair[0]:
                min = rPair[0]
            else:
                min = lPair[0]
            if rPair[1] > lPair[1]:
                max = rPair[1]
            else:
                max = lPair[1]
            newBB.append([min, max])
        return newBB

    # def printLeaf(self, leaf:NodeLeaf):
    #     for d in leaf.data:
    #         print(f"Coords: {d.coords}, Code: {d.code}")
    
    # def printKnn(self, knn:list[Datum]):
    #     print("Curr Knn list: \n")
    #     for d in knn:
    #         print(f"Coords: {d.coords}, Code: {d.code}")
    #     print("\n")
