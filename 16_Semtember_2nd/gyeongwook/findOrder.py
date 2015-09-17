class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        self.section = [None] * numCourses
        self.tree = [None] * numCourses
        for idx in range(numCourses):
            self.section[idx] = set()
            self.tree[idx] = set()
        
        for each_link in prerequisites:
            before = each_link[1]
            after = each_link[0]
            
            if self.reach(before, after): return []
            else: 
                self.section[after].add(before)
                self.tree[before].add(after)
            
        self.order = []
        for each_node in range(numCourses):
            self.search(each_node)
            
        self.order.reverse()
        return self.order
        
    def search(self, idx):
        if idx in self.order: return
        for each_node in self.tree[idx]:
            self.search(each_node)
        
        self.order.append(idx)
        
    def reach(self, start_point, destination):
        for each in self.section[start_point]:
            if each == destination or self.reach(each, destination): return True
            
        return False