public class Solution {
    HashMap<Float, HashMap<Float, HashSet<Point>>> hash = new  HashMap<Float, HashMap<Float, HashSet<Point>>>();
    HashMap<String,HashSet<Point>> same = new HashMap<String,HashSet<Point>>();
    
    public int maxPoints(Point[] points) {
        
        if(points.length == 1)
            return 1;
        
        int max = 0;
        
        for(int i = 0 ; i < points.length; i++)
        {
            for(int j = i ; j < points.length; j++)
            {
                int x1 = points[i].x, y1 = points[i].y;
                int x2 = points[j].x, y2 = points[j].y;
                
                if(i == j)
                    continue;
                   
                HashSet<Point> set;   
                
                if(x1==x2 && y1==y2)   
                {
                    if(null == (set = same.get(points[i].x+":"+points[i].y)))
                    {
                        set = new HashSet<Point>();
                    }
                    
                    set.add(points[i]);
                    set.add(points[j]);
                
                    same.put(points[i].x+":"+points[i].y, set);
                
                    int num = set.size();
                    if( num > max)
                    {
                        max = num;
                    }
                    continue;
                }
                
                Float slope = (float)(y2-y1)/(x2-x1);
                Float yIntercept = (float)y2 - x2*slope;
                
                if(x2 == x1)
                {
                    yIntercept = (float)x2;
                }
            
                HashMap<Float, HashSet<Point>> h;
                
                if(null == (h = hash.get(slope)))
                {
                    h = new HashMap<Float, HashSet<Point>>();
                    hash.put(slope, h);
                }
                
                if(null == (set = h.get(yIntercept)))
                {
                    set = new HashSet<Point>();
                }
                
                set.add(points[i]);
                set.add(points[j]);
                
                h.put(yIntercept, set);
                
                int num = set.size();
                if( num > max)
                {
                    max = num;
                }
            }
        }
        return max;
    }
}
