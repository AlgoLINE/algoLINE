uint32_t reverseBits(uint32_t n) {

	const int BIT_COUNT = 32;
	int remainder = 0;
	int result = 0;

	for (int i = 0; i < BIT_COUNT; i++)
	{
		remainder = n % 2;
		if (remainder != 0)
		{
			result += 1 << (31 - i);
			n -= 1;
		}
		n /= 2;

	}

	return result;

}