public class GenerateParentheses {
    
    List<String> p = null;
    char output[];
    int size = 1;
    
    public List<String> generateParenthesis(int n) {
        p = new ArrayList<String>();
        output = new char[n*2];
        output[0] = '(';
        
        make(n - 1, n);
        
        return p;
    }
    
    public void make(int left, int right){
        if( left == 0 && right == 0){
            p.add(new String(output));
            return;
        }else if(right < left){
            return;
        }
    
        if(left > 0){
            output[size++] = '(';
            make(left-1, right);
            size--;
        }
        if(right > 0){
            output[size++] = ')';
            make(left, right-1);
            size--;
        }
    }
}