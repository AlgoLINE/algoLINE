class Solution {
public:
	int firstMissingPositive(int A[], int n) {
		int result = (n + 1);

		int positiveAry[n];
		for (int i = 0; i < n; i++) {
			positiveAry[i] = 0;
		}

		for (int i = 0; i < n; i++) {
			if (A[i] > 0 && A[i] <= n) {
				positiveAry[A[i] - 1] = A[i];
			}
		}

		if (positiveAry[0] == 0) {
			result = 1;
			return result;
		}

		for (int i = 0; i < n; i++) {

			if (positiveAry[i] != (i + 1)) {
				result = (i + 1);
				break;
			}
		}

		return result;
	}
};