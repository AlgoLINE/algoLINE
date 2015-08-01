class Vertex:
    def __init__(self, idx):
        self.idx = idx
        self.visited = False
        self.hasCycle = None
        self.pre = []

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # construct graph using adjacency list
        self.adjList = [None] * numCourses
        for edge in prerequisites:
            idx = edge[0]
            if self.adjList[idx] == None:
                self.adjList[idx] = Vertex(idx)
            self.adjList[idx].pre.append(edge[1])     # add target idx
        
        # find cycle recursively
        for v in self.adjList:
            if self.hasCycle(v):
                return False
        return True
                
    def hasCycle(self, v):
        if v == None:
            return False
            
        if v.visited == True:
            if v.hasCycle == False:
                return False
            else:
                return True
                
        v.visited = True
        
        for n in v.pre:
            if self.hasCycle(self.adjList[n]):
                return True

        v.hasCycle = False
        return False