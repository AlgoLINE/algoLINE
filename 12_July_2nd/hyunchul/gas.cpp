class Solution {
public:
	int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {

		if (gas.size() < 1)
		{
			return -1;
		}

		vector<int> margin;
		vector<int> candidate;
		int marginSum = 0;
		bool isCandidate = true;

		for (int i = 0; i < gas.size(); i++)
		{
			int tmpMargin = gas[i] - cost[i];
			marginSum += tmpMargin;
			margin.push_back(tmpMargin);
			if (tmpMargin >= 0)
			{
				if (isCandidate)
				{
					candidate.push_back(i);
					isCandidate = false;
				}

			}
			else
			{
				isCandidate = true;
			}

			if (!isCandidate && i == gas.size() - 1)
			{
				if (margin.size() > 0 && margin[0] == 0)
				{
					margin.erase(margin.begin());
				}
			}

		}

		if (marginSum < 0)
		{
			return -1;
		}

		int result = -1;
		for (int i = 0; i < candidate.size(); i++)
		{
			int start = candidate[i];
			int subMarginSum = 0;
			for (int mi = start; mi < margin.size() + start; mi++)
			{

				if (mi >= margin.size())
				{
					subMarginSum += margin[mi - margin.size()];
				}
				else
				{
					subMarginSum += margin[mi];
				}

				if (subMarginSum < 0)
				{
					break;
				}
			}

			if (subMarginSum >= 0)
			{
				result = start;
				break;
			}
		}

		return result;
	}
};