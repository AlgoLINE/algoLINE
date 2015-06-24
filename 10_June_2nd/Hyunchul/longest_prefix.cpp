class Solution {
public:
	string longestCommonPrefix(vector<string>& strs) {
		map<string, int> preMap;

		for (int i = 0; i < strs.size(); i++)
		{
			for (int j = 0; j < strs[i].size(); j++)
			{
				string tmpStr = strs[i].substr(0, j + 1);
				map<string, int>::iterator iter = preMap.find(tmpStr);
				if (iter != preMap.end())
				{
					iter->second += 1;
				}
				else
				{
					preMap.insert(pair<string, int>(tmpStr, 1));
				}
			}
		}

		string result;
		int max = 0;
		map<string, int>::iterator iter;
		for (iter = preMap.begin(); iter != preMap.end(); iter++)
		{
			if (iter->second > max)
			{
				max = iter->second;
				result = iter->first;
			}
			else if (iter->second == max)
			{
				if (iter->first.size() > result.size())
				{
					result = iter->first;
				}
			}
		}

		if (max < strs.size())
			result = "";

		return result;
	}
};