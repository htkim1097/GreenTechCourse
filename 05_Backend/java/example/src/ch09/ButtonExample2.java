package ch09;

public class ButtonExample2 {

	public static void main(String[] args) {
		Button btn = new Button();
		
		btn.setClickListener(new Button.ClickListener() {
			
			@Override
			public void onClick() {
				System.out.println("Ok 버튼을 클릭했습니다.");
				
			}
		});
		
		btn.click();
		
		Button btn2 = new Button();
		
		btn2.setClickListener(new Button.ClickListener() {
			
			@Override
			public void onClick() {
				System.out.println("Cancel 버튼을 클릭했습니다.");
				
			}
		});
		
		btn2.click();

	}

}
