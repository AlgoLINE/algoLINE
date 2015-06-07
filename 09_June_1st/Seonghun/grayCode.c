int* grayCode(int n, int* returnSize) {
    
    if (n < 0)
        return NULL;
        
    int size = (int)pow(2,n);
    *returnSize = size;
    int cnt = 0;
    
    int* grayCode = (int*)malloc(sizeof(int)*size);
    grayCode[cnt++] = 0;

    for (int i = 1 ; i <= n ; i++) {
        if(i == 1) {
            grayCode[cnt++] = 1;
        } else {
            int unit = (int)pow(2, i-1);
            for(int j = unit-1 ; j >= 0 ; j--) {
                grayCode[cnt++] = unit + grayCode[j];
            }
        }
    }
    
    return grayCode;
}
