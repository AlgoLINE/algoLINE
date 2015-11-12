public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        
        final int thr = (int) Math.floor(nums.length/3) + 1;

        List<Integer> lCandis  = new ArrayList<Integer>();
        Set<Integer> lNewCandis  = new HashSet<Integer>();
        
        int cnt = 0;
        int bitSize = 8;
        int window = (int)Math.pow(2, bitSize);
        int p = window - 1;                 // point, Start from lowest bit
        int filter = 0;                     //
        int[][] counts = new int[2][window];
        
        int skip = 0;
        
        while (cnt < Integer.SIZE) {
            
            if (p > window-1 && ((skip & p) == 0)) {
                filter = filter | p;
                p = p << bitSize;
                cnt += bitSize;
                continue;
            }
            
            // count for current position
            // if p is one, do not have to apply filter, but if p is bigger than 0, it is required to apply filter to candis
            int cntCandis = 0;
            
            if (p == window - 1) {
                for (int num : nums) {
                    int bit = (num & p);
                    counts[0][bit] += 1;
                    skip |= num;
                }
            } else {
                for (int num : nums) {
                    
                    int bit = (num & p) >>> cnt;
                    int filtered = (num & filter);
                    
                    if (lCandis.size() == 2 && (filtered == lCandis.get(1))) {
                        counts[1][bit] += 1;
                    } else if ((filtered == lCandis.get(0))) {
                        counts[0][bit] += 1;
                    }
                }
            }
            
            // counts = new int[2][window];
            if (p == window - 1) {
                for (int c = 0 ; c < window ; c++) {
                    if (counts[0][c] >= thr) {
                        lNewCandis.add(c << cnt);
                    }
                    counts[0][c] = 0;
                }
            } else {
                for (int r = 0 ; r < lCandis.size() ; r++) {
                    for (int c = 0 ; c < window ; c++) {
                        if (counts[r][c] >= thr) {
                            lNewCandis.add((c << cnt) | lCandis.get(r));
                        }
                        counts[r][c] = 0;
                    }
                }    
            }
            
            if (lNewCandis.size() == 0) {
                lCandis.clear();
                return lCandis;
            }
            
            lCandis.clear();
            lCandis.addAll(lNewCandis);
            lNewCandis.clear();
            
            filter = filter | p;
            p = p << bitSize;
            cnt += bitSize;
        }
        
        return lCandis;
    }
}