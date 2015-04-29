uint32_t reverseBits(uint32_t n) {

    uint32_t reverse = 0;
    int i;
    
    for( i = 0 ; i < 32 ; i++)
    {
        reverse = reverse << 1;
        if(n % 2 == 1)
        {
            reverse += 1;
        }
        n = n >> 1;
    }
    
    return reverse;
}
