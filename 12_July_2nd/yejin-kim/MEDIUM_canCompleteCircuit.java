/**
 * 
 * @author yejin-kim
 *
 */
public class MEDIUM_canCompleteCircuit {
	public int canCompleteCircuit(int[] gas, int[] cost) {
		int total = 0;
		int current = 0;
		int start = -1;
		for (int runner = 0; runner < gas.length; runner++) {
			total += gas[runner] - cost[runner];
			current += gas[runner] - cost[runner];
			if (current < 0) {
				start = runner;
				current = 0;
			}
		}
		if (total < 0) {
			return -1;
		} else {
			return start + 1;
		}
	}
}
