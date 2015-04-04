class Solution {
public:
	string convertToTitle(int n) {
		const int alphabetNum = 26;
		int alphabetIndex = 0;
		int cycleCount = 0;
		char alphabetAry[alphabetNum];
		int askiiIndex = 65;
		string result = "";

		if (n < 1) {
			return NULL;
		}

		alphabetAry[0] = 90;

		for (int i = 1; i < alphabetNum; i++) {
			alphabetAry[i] = askiiIndex;
			askiiIndex++;
		}

		while (n >= 1) {
			int index = n % alphabetNum;
			result += alphabetAry[n % alphabetNum];
			n /= 26;
			if (index == 0) {
				n -= 1;
			}
		}

		reverse(result.begin(), result.end());


		return result;
	}
};