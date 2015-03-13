//
//  SingleOne.cpp
//  
//
//  Created by LinePlus on 2015. 3. 10..
//
//

class Solution {
public:
    int singleNumber(int A[], int n) {
        int singleOneIndex = 0;
        int tmp = 0;
        for (int i = 0; i < n; i++) {
            if (tmp == A[i] / 2) {
                singleOneIndex = i - 1;
            } else {
                tmp = A[i];
            }
        }
        return A[singleOneIndex];
    }
};
