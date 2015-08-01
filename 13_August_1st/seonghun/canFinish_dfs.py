class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # construct graph using adjacency list
        graph = [[] for _ in xrange(numCourses)]            # comparing with : graph = [[]] * numCourses
        visited = [0] * numCourses
        for fr,to in prerequisites:
            graph[fr].append(to)
            
        # recursive function using DFS
        def hasCycle(i):
            if visited[i] == -1:            # if visited previously
                return False
            if visited[i] == 1:             # if visited currently
                return True
                
            visited[i] = 1                  # set to current-visiting status
            
            for idx in graph[i]:
                if hasCycle(idx):
                    return True
                    
            visited[i] = -1                 # set to previous-visiting status
            return False
            
        # find recursively
        for idx in xrange(numCourses):
            if hasCycle(idx):
                return False
        
        return True