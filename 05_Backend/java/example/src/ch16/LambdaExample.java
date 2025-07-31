package ch16;

public class LambdaExample {
	public static void main(String[] args) {
		Person person = new Person();
		
		person.action(() -> {
			System.out.println("fdsf");
		});
		
		person.action((x, y) -> {
			double res = x + y;
			return res;
		});
		
		person.action((x, y) -> (x + y));
		
		person.action(Computer::staticMethod);
		
		Computer com = new Computer();
		person.action(com::instanceMethod);
		
		String a = new String();
	
		
	}
}
