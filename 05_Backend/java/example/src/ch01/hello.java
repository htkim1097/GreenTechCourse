package ch01;

@FunctionalInterface
interface Calculable {
	// 추상 메서드
	void calculate(int x, int y);
}

public class hello {

	public static void main(String[] args) {
	
		action((x, y) -> {
			System.out.println(x + y);
		});
	}
	
	public static void action(Calculable calc) {
		int x = 10;
		int y = 4;
		calc.calculate(x, y);
	}
}