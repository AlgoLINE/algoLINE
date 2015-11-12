class Solution(object):
    def initialize(self):
        self.curr = 0
        self.temp = 1
        self.op = '*'
        
    def update_temp(self):
        if self.op == '/':
            self.temp /= self.curr
        elif self.op == '*':
            self.temp *= self.curr
    
    def calculate(self, s):
        stack = []
        self.initialize()
        
        for each in s:
            if each == ' ':
                continue
            elif each == '+':
                self.update_temp()
                stack[-1] = stack[-1]*self.temp
                stack.append(1)
                self.initialize()
            elif each == '-':
                self.update_temp()
                stack[-1] = stack[-1]*self.temp
                stack.append(-1)
                self.initialize()
            elif each == '*':
                self.update_temp()
                self.curr = 0
                self.op = '*'
            elif each == '/':
                self.update_temp()
                self.curr = 0
                self.op = '/'
            else:
                if len(stack) == 0: stack.append(1)
                self.curr = self.curr*10 + int(each)
        
        self.update_temp()
        stack[-1] = stack[-1]*self.temp
        
        ret = 0
        for each in stack:
            ret += each
    
        return ret