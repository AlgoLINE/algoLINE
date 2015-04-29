int minimumTotal(int **triangle, int numRows) {
    int i = 0, j = 0;
    int index = 0;
    int a, b;
    int min = INT_MAX;

    for(i = 1 ; i < numRows-1 ; i++)
    {
        for(j = 0 ; j < i ; j++)
        {
            index++;
        
            if (j == 0)
            {
                *(&triangle[0][0] + index) += *(&triangle[0][0] + index -i);
            }
            else if( j == i-1)
            {
                *(&triangle[0][0] + index) += *(&triangle[0][0] + index -i - 1);
            }
            else
            {
                a = *(&triangle[0][0] + index -i);
                b = *(&triangle[0][0] + index -i - 1);
                (a > b) ? (*(&triangle[0][0] + index) += b) : (*(&triangle[0][0] + index) += a);
            }
            
            if( *(&triangle[0][0] + index) < min)
                min = *(&triangle[0][0] + index);
            
        }
    }
    
    return min;
    
}
