int numCacheTrees(int n, int* cache) {
    
    if (n < 0)
        return 0;
    
    // reuse the value in the cache
    if (cache[n] > -1)
        return cache[n];
        
    int cnt = 0;
    // fot each case where i is root
    for (int i = 1 ; i <= n ; i++) {
        cnt += (numCacheTrees(i-1, cache)*numCacheTrees(n-i, cache));
    }
    
    // update the cache
    cache[n] = cnt;
    return cnt; 
}

int numTrees(int n) {
    
    int* cache = (int*) malloc(sizeof(int)*(n+1));
    cache[0] = 1;
    
    // init cache
    for (int i = 1 ; i <= n ; i++) {
        cache[i] = -1;
    }
    
    // start count
    int cnt = numCacheTrees(n, cache);
    free(cache);
    
    return cnt;
}