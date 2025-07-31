package ch16;


public class Example {
	// 6
	@FunctionalInterface
	private static interface Function {
		double apply(double x, double y);
	}
	
	@FunctionalInterface
	public interface Operator {
		public int apply(int x, int y);
	}
	
	private static int[] scores = {10, 50, 3};
	
	public static int maxOrMin(Operator operator) {
		int res = scores[0];
		for (int score : scores) {
			res = operator.apply(res, score);
		}
		return res;
	}
	
	public static double calc(Function fun) {
		double x = 10;
		double y = 4;
		
		return fun.apply(x, y);
	}
	
	public static void main(String[] args) {
		// 5
		Button btnOk = new Button();
		btnOk.setClickListener(() -> {
			System.out.println("Ok 버튼을 클릭했습니다.");
		});
		btnOk.click();
		
		// 6
		double res = calc((x, y) -> (x / y));
		System.out.println("result: " + res);
		
		// 7
		int max = maxOrMin((x, y) -> {
			if (x >= y) {
				return x;
			}
			else {
				return y;
			}
		});
		
		System.out.println("최대값: " + max);
	}
}
