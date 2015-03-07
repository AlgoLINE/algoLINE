public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
        if(n < k)
            return null;
            
        int[] arr = new int[k];
        for(int i = 0 ; i < k ; i++){
            arr[i] = i+1;
        }

        List<List<Integer>> ll = new ArrayList<List<Integer>>();
        do{
            ll.add(makeList(arr));
        }while(update(arr, n));
        
        return ll;
    }
    
    private boolean update(int[] arr, int maxNum){
        
        int k = arr.length;
        
        for(int i = k-1 ; i >= 0 ; i--){
            if(maxNum - arr[i] > k - (i+1)){
                arr[i]++;
                for(int j = i+1 ; j < k ; j++){
                    arr[j] = arr[j-1] + 1;
                }
                return true;
            }
            arr[i] = 0;
        }
        return false;
    }
    
    private List<Integer> makeList(int[] arr){
        int k = arr.length;
        
        List<Integer> l = new ArrayList<Integer>(k);
        for(int i = 0 ; i < k ; i++){
            l.add(arr[i]);
        }
        
        return l;
    }
    
}
