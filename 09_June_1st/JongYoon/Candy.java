public class Solution {
    public int candy(int[] ratings) {
        int sum = 1, plus = 1, updateNum = 1, lastMax = 1;

        for (int i = 1 ; i < ratings.length  ; i++)
        {
            if (ratings[i-1] > ratings[i]) {
                sum += plus;
                if( lastMax > plus)
                    sum -= 1;
                plus += 1;
                updateNum = 1;
            }
            else if (ratings[i-1] < ratings[i]) {
                updateNum++;
                lastMax = updateNum;
                plus = 1;
            } 
            else {
                plus = 1;
                updateNum = 1;
                lastMax = 1;
            }
            
            sum += updateNum; 
        }
        
        return sum;
    }
}