 class SingleNumber{
 
 public int singleNumber(int[] A) {
       
        int beatNum = 0;
        for(int i = 0 ; i < A.length ; i++){
            beatNum ^= A[i];
        }
        return beatNum;
    }
 }