public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        
        final int thr = (int) Math.floor(nums.length/3) + 1;

        List<Integer> lCandis  = new ArrayList<Integer>();
        List<Integer> lNewCandis  = new ArrayList<Integer>();
        
        int cnt = 0;
        int p = 1;              // point, Start from lowest bit
        int filter = 0;         //
        int[][] counts = new int[2][2];
        
        boolean setSkip = false;
        int skip = 0;
        
        while (cnt < Integer.SIZE) {
            
            if (p > 1 && ((skip & p) == 0)) {
                filter = filter | p;
                p = p << 1;
                cnt += 1;
                continue;
            }
            
            // count for current position
            // if p is one, do not have to apply filter, but if p is bigger than 0, it is required to apply filter to candis
            
            for (int num : nums) {
                int bit = (num & p) >>> cnt;
                
                if (setSkip == false) {
                    skip |= num;    
                }
                
                int filtered = (num & filter);
            
                if (p == 1) {
                    counts[0][bit] += 1;
                } else if (lCandis.size() == 2 && (filtered == lCandis.get(1))) {
                    counts[1][bit] += 1;
                } else if ((filtered == lCandis.get(0))) {
                    counts[0][bit] += 1;
                }
            }
            
            setSkip = true;
            
            int rowSize = (p == 1)? 1 : lCandis.size();
            for (int r = 0 ; r < rowSize ; r++) {
                for (int bit = 0 ; bit < 2 ; bit++) {
                    if (counts[r][bit] >= thr) {
                        if (p == 1) {
                            lNewCandis.add(bit << cnt);    
                        } else {
                            lNewCandis.add((bit << cnt) | lCandis.get(r));    
                        }
                    }
                    counts[r][bit] = 0;
                }
            }
            
            // change pointer
            List<Integer> temp = lCandis;
            lCandis = lNewCandis;
            lNewCandis = temp;
            lNewCandis.clear();
            
            if (lCandis.size() == 0) {
                return lCandis;
            }
            
            filter = filter | p;
            p = p << 1;
            cnt += 1;
        }
        
        return lCandis;
    }
}