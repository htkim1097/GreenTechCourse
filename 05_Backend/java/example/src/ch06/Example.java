package ch06;

import java.util.*;

class Member {
	// 13
	public String name;
	public String id;
	public String password;
	public int age;
	
	// 14
	public Member(String name, String id) {
		this.name = name;
		this.id = id;
	}
}

// 15
class MemberService {
	public String name;
	public String id = "hong";
	public String password = "12345";
	
	public boolean login(String id, String password) {
		return this.id != id ? false : this.password != password ? false : true;
	}
	
	public void logout(String id) {
		System.out.println(String.format("%s 님이 로그아웃 되었습니다.", id));
	}
}

class Printer {
	// 16
	public void println(String value) {
		System.out.println(value);
	}
	
	public void println(int value) {
		System.out.println(value);
	}
	
	public void println(double value) {
		System.out.println(value);
	}
	
	public void println(boolean value) {
		System.out.println(value);
	}
	
	// 17
	public static void println2(String value) {
		System.out.println(value);
	}
	
	public static void println2(int value) {
		System.out.println(value);
	}
	
	public static void println2(double value) {
		System.out.println(value);
	}
	
	public static void println2(boolean value) {
		System.out.println(value);
	}
}

// 18
class ShopService {
	private static ShopService Instance;
	
	private ShopService() {
		
	}
	
	public static ShopService getInstance() {
		if (Instance == null) {
			Instance = new ShopService();
		}
		
		return Instance;
	}
}

// 19
class Account {
	private int balance;
	private static final int MIN_BALANCE = 0;
	private static final int MAX_BALANCE = 1000000;
	
	public Account() {
		
	}
	
	public int getBalance() {
		return balance;
	}
	
	public void setBalance(int value) {
		if (MIN_BALANCE <= value && value <= MAX_BALANCE) {
			balance = value;
		}
	}
}

// 20
class Account2 {
	private int balance;
	private String name;
	private String num;
	
	public Account2() {
		
	}
	
	public int getBalance() {
		return balance;
	}
	
	public void setBalance(int value) {
		balance = value;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String value) {
		name = value;
	}
	
	public String getNum() {
		return num;
	}
	
	public void setNum(String value) {
		num = value;
	}
}

class BankApplication {
	private Account2[] accounts = new Account2[100];
	private int selected = 0;
	private boolean isEnd = false;
	
	public void start() {
		while (!isEnd) {
			System.out.println("----------------------------------------------");
			System.out.println("1. 계좌생성 | 2. 계좌목록 | 3. 예금 | 4. 출금 | 5. 종료");
			System.out.println("----------------------------------------------");
			
			Scanner sc = new Scanner(System.in);
			System.out.print("선택> ");
			selected = sc.nextInt();
			
			switch (selected) {
			case 1:
				createAccount();
				break;
			case 2:
				getAccountList();
				break;
			case 3:
				deposit();
				break;
			case 4:
				withdrawal();
				break;
			case 5:
				isEnd = true;
				break;
			}
		}
	}
	
	private void createAccount() {
		int idx = -1;
		
		for (int i = 0; i < accounts.length; i++) {
			if (accounts[i] == null) {
				idx = i;
				break;
			}
		}
		
		accounts[idx] = new Account2();
		
		System.out.println("------");
		System.out.println("계좌생성");
		System.out.println("------");
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("계좌번호: ");
		String num = sc.next();
		accounts[idx].setNum(num);
		
		System.out.print("계좌주: ");
		String name = sc.next();
		accounts[idx].setName(name);
		
		System.out.print("초기입금액: ");
		int val = sc.nextInt();
		accounts[idx].setBalance(val);
		
		System.out.println("결과: 계좌가 생성되었습니다.");
	}
	
	private void getAccountList() {
		System.out.println("------");
		System.out.println("계좌목록");
		System.out.println("------");
		
		for (int i = 0; i < accounts.length; i++) {
			if (accounts[i] != null) {
				System.out.println(String.format("%s    %s    %d", accounts[i].getNum(), accounts[i].getName(), accounts[i].getBalance()));				
			}
		}
	}
	
	private void deposit() {
		System.out.println("------");
		System.out.println("예금");
		System.out.println("------");
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("계좌번호: ");
		String num = sc.next();
		
		int idx = -1;
		for (int i = 0; i < accounts.length; i++) {
			if (accounts[i] != null && accounts[i].getNum().equals(num)) {
				idx = i;
			}
		}
		
		if (idx == - 1) {
			System.out.println("잘못된 계좌입니다.");
			return;
		}
		
		System.out.print("예금액: ");
		int val = sc.nextInt();
		accounts[idx].setBalance(accounts[idx].getBalance() + val);
		
		System.out.println("결과: 입금되었습니다.");
	}
	
	private void withdrawal() {
		System.out.println("------");
		System.out.println("출금");
		System.out.println("------");
		
		Scanner sc = new Scanner(System.in);
		
		System.out.print("계좌번호: ");
		String num = sc.next();
		
		int idx = -1;
		for (int i = 0; i < accounts.length; i++) {
			if (accounts[i] != null && accounts[i].getNum().equals(num)) {
				idx = i;
			}
		}
		
		if (idx == - 1) {
			System.out.println("잘못된 계좌입니다.");
			return;
		}
		
		System.out.print("출금액: ");
		int val = sc.nextInt();
		if (accounts[idx].getBalance() - val >= 0) {
			accounts[idx].setBalance(accounts[idx].getBalance() - val);
			System.out.println("결과: 출금되었습니다.");
		}
		else {
			System.out.println("결과: 잔액이 부족합니다.");
		}
	}
}

public class Example {
	public static void main(String[] args) {
		Member user1 = new Member("홍길동", "hong");
		
		// 15
		MemberService memberService = new MemberService();
		boolean result = memberService.login("hong", "12345");
		
		if (result) {
			System.out.println("로그인 되었습니다.");
			memberService.logout("hong");
		}
		else {
			System.out.println("id 또는 password가 올바르지 않습니다.");
		}
		
		// 16
		Printer printer = new Printer();
		printer.println(10);
		printer.println(true);
		printer.println(5.7);
		printer.println("홍길동");
		
		// 17
		Printer.println2(10);
		Printer.println2(true);
		Printer.println2(5.7);
		Printer.println2("홍길동");
		
		// 18
		ShopService obj1 = ShopService.getInstance();
		ShopService obj2 = ShopService.getInstance();
		
		if (obj1 == obj2) {
			System.out.println("같은 ShopService 객체입니다.");
		}
		else {
			System.out.println("다른 ShopService 객체입니다.");
		}
		
		
		// 19
		Account account = new Account();
		
		account.setBalance(10000);
		System.out.println("현재 잔고: " + account.getBalance());
		
		account.setBalance(-100);
		System.out.println("현재 잔고: " + account.getBalance());
		
		account.setBalance(2000000);
		System.out.println("현재 잔고: " + account.getBalance());
		
		account.setBalance(300000);
		System.out.println("현재 잔고: " + account.getBalance());
		
		// 20
		BankApplication bank = new BankApplication();
		bank.start();
	}
}