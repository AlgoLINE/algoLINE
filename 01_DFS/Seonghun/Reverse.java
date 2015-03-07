public class Solution {
    public int reverse(int x) {
        int copy = x;
        Queue<Integer> q = new LinkedList<Integer>();
        while(copy != 0){
            q.add(copy % 10);
            copy = copy/10;
        }
        
        int reverse = 0;
        while(!q.isEmpty()){
            int size = q.size();
            reverse += (int)(q.poll() * Math.pow(10, size-1));
        }
        
        if(x >= 0 && reverse < 0)       return 0;
        else if(x < 0 && reverse >= 0)  return 0;
        return reverse;
    }
}