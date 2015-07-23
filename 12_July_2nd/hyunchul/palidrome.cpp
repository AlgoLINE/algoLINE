class Solution {
public:
	bool isPalindrome(string s)
	{

		string onlyAlphaStr;

		if (s.size() < 1)
		{
			return true;
		}

		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] > 47 && s[i] < 58)
			{
				onlyAlphaStr.push_back(s[i]);
			}
			else if (s[i] > 64 && s[i] < 91)
			{
				onlyAlphaStr.push_back(s[i]);
			}
			else if (s[i] > 96 && s[i] < 123)
			{
				onlyAlphaStr.push_back(s[i] - 32);
			}

		}

		int alphaStrSize = onlyAlphaStr.size();

		if (alphaStrSize <= 1)
		{
			return true;
		}

		int checkPalindCnt = onlyAlphaStr.size() * 0.5;

		for (int i = 0; i < checkPalindCnt; i++)
		{
			if (onlyAlphaStr[i] != onlyAlphaStr[alphaStrSize - i - 1])
			{
				return false;
			}
		}

		return true;
	}
};