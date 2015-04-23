class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
    	uint32_t mask, m, shiftCount;

    	shiftCount = 1;
    	mask = 0x55555555;
        m = (n ^ (n >> shiftCount) ) & mask;
        n = ((n & mask) ^ m) | ((n & (mask << shiftCount)) ^ (m << shiftCount));

        shiftCount = shiftCount << 1;
        mask = 0x33333333;
        m = (n ^ (n >> shiftCount) ) & mask;
        n = ((n & mask) ^ m) | ((n & (mask << shiftCount)) ^ (m << shiftCount));

        shiftCount = shiftCount << 1;
        mask = 0x0F0F0F0F;
        m = (n ^ (n >> shiftCount) ) & mask;
        n = ((n & mask) ^ m) | ((n & (mask << shiftCount)) ^ (m << shiftCount));

        shiftCount = shiftCount << 1;
        mask = 0x00FF00FF;
        m = (n ^ (n >> shiftCount) ) & mask;
        n = ((n & mask) ^ m) | ((n & (mask << shiftCount)) ^ (m << shiftCount));

        shiftCount = shiftCount << 1;
        mask = 0x0000FFFF;
        m = (n ^ (n >> shiftCount) ) & mask;
        n = ((n & mask) ^ m) | ((n & (mask << shiftCount)) ^ (m << shiftCount));
    }
};