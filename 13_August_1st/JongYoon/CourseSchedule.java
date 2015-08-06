public class Solution {
    boolean[][] root;
    boolean[][] child;
    
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        root = new boolean[numCourses][numCourses];
        child = new boolean[numCourses][numCourses];

        for (int i = 0 ; i < prerequisites.length ; i++) {
            int from = prerequisites[i][0];
            int to = prerequisites[i][1];
            
            child[to][from] = true;
            if(!setMyRoot(to, -1, from, numCourses))
            {
                return false;
            }
        }
        return true;
    }
    
    boolean setMyRoot(int rootNum, int origin, int myNum, int numCourses)
    {
        boolean t = false;
        for ( int i = 0 ; i < numCourses ; i++)
        {
            if (root[rootNum][i] && root[myNum][i])
            {
                return false;
            }
        }
        root[myNum][rootNum] = true;
        if ( origin != -1) {
            root[myNum][origin] = false;
        }
        
        for (int k = 0 ; k < numCourses ; k++)
        {
            if (child[myNum][k])
            {
                return setMyRoot(rootNum, myNum, k, numCourses);
            }
        }
        return true;
    }
}