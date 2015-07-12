
/**
 * 
 * @author yejin-kim
 *
 */
public class EASY_isPalindrome {
	
	public boolean isPalindrome(String s) {
		char[] charArray = s.toCharArray();
		int left = getValidLeft(charArray, 0);
		int right = getValidRight(charArray, charArray.length - 1);
		while (left < right) {
			if (getPureValue(charArray[left]) != getPureValue(charArray[right])) {
				return false;
			}
			left = getValidLeft(charArray, left + 1);
			right = getValidRight(charArray, right - 1);
		}
		return true;
	}
	private int getPureValue(char value) {
		if (value > 96) {
			return value - 32;
		}
		return value;
	}
	private int getValidLeft(char[] charArray, int l) {
		for (; l < charArray.length; l++) {
			if (isValidValue(charArray[l])) {
				return l;
			}
		}
		return l;
	}
	private int getValidRight(char[] charArray, int r) {
		for (; r >= 0; r--) {
			if (isValidValue(charArray[r])) {
				return r;
			}
		}
		return r;
	}
	private boolean isValidValue(char value) {
		// Capital alphabet
		if (value > 64 && value < 91) {
			return true;
		}
		// Normal alphabet
		if (value > 96 && value < 123) {
			return true;
		}
		// Number
		if (value > 47 && value < 58) {
			return true;
		}
		// Otherwise, return false
		return false;
	}
}
