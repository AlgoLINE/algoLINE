public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        int cnt = 0;
        int revN = 0;
        
        while (cnt < 32){
            revN = revN << 1;           // position of this line is important
            
            int curBit = n & 1;
            if (curBit == 1) revN += 1;
            
            n = n >> 1;
            cnt++;
        }
        
        return revN;
    }
}