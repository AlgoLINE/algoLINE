/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    public int maxPoints(Point[] points) {
        
        int i = 0, j = 0;
        int size = points.length;
        int max = Integer.MIN_VALUE;
        
        if (size < 2)
            return size;
        
        Map<String, Integer> samePoint = new HashMap<String, Integer>();
        List<Point> distictPointList = new ArrayList<Point>(size);
        for (Point p : points) {
            String key = keySamePoint(p);
            if (samePoint.containsKey(key)) {
                samePoint.put(key, samePoint.get(key)+1);
            } else {
                samePoint.put(key, 1);
                distictPointList.add(p);
            }
        }
        
        if (distictPointList.size() == 1)
            return size;
            
        size = distictPointList.size();
        Point[] distictPoints = distictPointList.toArray(new Point[size]);
        
        Map<String, Integer> sameLineCnt = new HashMap<String, Integer>();
        Map<String, Set<Point>> sameLineP = new HashMap<String, Set<Point>>();
        
        // calculate gradient and y-intercept between all distict coupble of two points
        double gradient = 0.0;
        double y_intercept = 0.0;
        for (i = 0 ; i < size-1 ; i++){
            Point a = distictPoints[i];
            
            for (j = i+1 ; j < size ; j++){
                Point b = distictPoints[j];
                
                if (a.x == b.x) {
                    gradient = a.x;
                    y_intercept = Double.NEGATIVE_INFINITY;
                } else if (a.y == b.y) {
                    gradient = 0.0;
                    y_intercept = a.y;
                } else {
                    gradient = (double)(a.x - b.x)/(double)(a.y - b.y);
                    y_intercept = a.y - gradient*a.x;
                }
                
                // find max
                String lineKey = keySameLine(gradient, y_intercept);
                int cnt = 0;
                Set<Point> setP = null;
                if (sameLineP.containsKey(lineKey)) {
                    cnt = sameLineCnt.get(lineKey);
                    setP = sameLineP.get(lineKey);
                } else {
                    setP = new HashSet<Point>();
                    sameLineP.put(lineKey, setP);
                }
                if (setP.add(a)) cnt += samePoint.get(keySamePoint(a));
                if (setP.add(b)) cnt += samePoint.get(keySamePoint(b));
                sameLineCnt.put(lineKey, cnt);
                
                if (cnt > max)
                    max = cnt;
                
            }
        }
        
        return max;
        
    }
    
    private String keySamePoint(Point p){
        return "" + p.x + ":" + p.y;
    }
    
    private String keySameLine(double gradient, double y_intercept){
        return "" + gradient + ":" + y_intercept;
    }
}