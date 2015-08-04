class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        self.section = [None] * numCourses
        for idx in range(numCourses):
            self.section[idx] = set()
        
        for each_link in prerequisites:
            before = each_link[1]
            after = each_link[0]
            
            if self.reach(before, after):
                return False
                
            self.section[after].add(before)
            
        return True
        
    def reach(self, start_point, destination):
        for each in self.section[start_point]:
            if each == destination or self.reach(each, destination):
                return True
            
        return False