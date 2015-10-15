public class Solution 
{
    public int removeDuplicates(int[] nums) 
    {
        HashMap<Integer,Integer> map = new HashMap<>();
        int sum = 0;
        List<Integer> list = new ArrayList<>();

        if (nums.length == 0)
        {
            return 0;
        }
        
        for (int num : nums)
        {
            if (map.containsKey(num))
            {
                int count = map.get(num);
                count++;
                if (count <= 2)
                {
                    map.put(num, count);
                    list.add(num);
                }
            }
            else
            {
                map.put(num,1);
                list.add(num);
            }
        }
        
        for( Map.Entry<Integer, Integer> elem : map.entrySet())
        {
            sum += elem.getValue();
        }
        
        for (int i = 0; i < list.size(); i++)
        {
            nums[i] = list.get(i);
        }
        
        return sum;
        
    }
}