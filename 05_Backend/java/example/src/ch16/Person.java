package ch16;

public class Person {
	public void action(Workable workable) {
		workable.work();
	}
	
	public void action(Calcuable calculable) {
		double res = calculable.calc(10, 4);
		System.out.println("결과: " + res);
	}
}
