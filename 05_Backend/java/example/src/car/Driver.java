package car;

public class Driver {

	public static void main(String[] args) {
		Car myCar = new Car("테슬라", "Black"); 
		System.out.println(myCar.model + myCar.color);
		
		myCar.engineOn();

		myCar.AudioOn();
		myCar.AudioOff();
		
		myCar.showDashboard();
		
		
//		myCar.board.lightOn();
//		myCar.board.lightOff();
//		
		myCar.board.wiperOn();
		myCar.board.wiperOff();
		myCar.board.wiperUp();
//		myCar.board.wiperDown();
		
		myCar.setSpeed(true, 5);
		myCar.setGear("R");
		myCar.setGear("D");
//		myCar.setGear("N");
		myCar.setSpeed(true, 5);
		myCar.setSpeed(false, 3);

		myCar.turn("L"); 

//		myCar.turn("R");
		myCar.showDashboard();

		myCar.AudioOn();
		myCar.setVolume(true);
		myCar.setVolume(true);
		myCar.setVolume(true);
		myCar.setVolume(false);
		
		myCar.tempOn();
		myCar.setTemp(true);
		myCar.tempOff();
		myCar.setTemp(true);
		myCar.setTemp(false);
		
		myCar.setGear("P");

		
		myCar.engineOff();
		myCar.setSpeed(true, 5);

		
		
		

		
				

	}

}
