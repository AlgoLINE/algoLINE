class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        SPACE = 0
        NUMBER = 1
        DOT = 2
        SIGN = 3
        EXPONENT = 4
        ETC = 5
        
        transitionTable = [
            [0,	0,	0,	0,	0,	0],	# 0 : 숫자 아님요
            [1,	3,	4,	2,	0,	0],	# 1 : 맨 앞 공백
            [0,	3,	4,	0,	0,	0],	# 2 : 숫자 맨 앞에 부호 등장!
            [9,	3,	10,	0,	6,	0],	# 3 : 숫자(지수가 아닌 부분) 등장!
            [0,	5,	0,	0,	0,	0],	# 4 : 소수점 등장!
            [9,	5,	0,	0,	6,	0],	# 5 : 소수점 뒤에 숫자 등장!
            [0,	8,	0,	7,	0,	0],	# 6 : 지수 표시 e / E 등장!
            [0,	8,	0,	0,	0,	0],	# 7 : 지수 부분 부호 등장!
            [9,	8,	0,	0,	0,	0],	# 8 : 지수 부분 숫자 등장!
            [9,	0,	0,	0,	0,	0],	# 9 : 맨 뒤 공백
            [9,	5,	0,	0,	6,	0]	# 10 : 숫자 나오다가 소수점 등장 (true)
        ]
        
        state = 1
        
        for each in s:
            inputType = ETC
            
            # 입력 값이 어떤 타입에 해당하는지 판별
            if each == ' ':
                inputType = SPACE
            elif '0' <= each and each <= '9':
                inputType = NUMBER
            elif each == '.':
                inputType = DOT
            elif each == '+' or each == '-':
                inputType = SIGN
            elif each == 'e' or each == 'E':
                inputType = EXPONENT
            
            # 테이블을 참조해서 입력 타입에 따른 현재 상태를 갱신 
            state = transitionTable[state][inputType]
            
            # 만약 숫자가 아니라고 이미 판정되면 바로 리턴
            if state == 0: 
                return False
        	    
        return state == 3 or state == 5 or state == 8 or state == 9 or state == 10