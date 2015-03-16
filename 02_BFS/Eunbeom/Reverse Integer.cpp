class Solution {
public:
    int reverse(int x) {
        
        long long result = 0;
        int flag = 1;
        
        if(x<0){
            flag = -1;
            x = -x;
        }
    
        for( ;x>0; x/=10)
            result = result * 10 + x % 10;
        result *= flag;
        
        if(result > INT_MAX || result < INT_MIN) return 0;
        return result;
    }
};