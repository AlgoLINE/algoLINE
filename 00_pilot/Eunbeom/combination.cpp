class Solution {
public:
    
    vector<vector<int>> vv;
    vector<int> v;
    
    vector<vector<int> > combine(int n, int k) {
        f(n, k, 0);
        return vv;
    }
    
    void f(int n, int k, int i){
        
        if(k==0){
            vv.push_back(v);
            return;
        }

        for(int j=i+1;j<=n;j++){
            v.push_back(j);
            f(n, k-1, j);
            v.pop_back();
        }
    }
};