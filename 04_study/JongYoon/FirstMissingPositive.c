int firstMissingPositive(int A[], int n) {
    bool *posNum;
    int i, num;
    
    if(n == 0){
        return 1;
    }
    
    posNum = (bool*)malloc(sizeof(bool)*n);
    memset(posNum, 0, n);
    
    for(i = 0 ; i < n ; i++){
        num = A[i];
        if( num > 0) posNum[num] = true;
    }
    
    for(int i = 1 ; i < n ; i++){
        if(!posNum[i]){
            return i;
        }
    }
    
    return 1;
}