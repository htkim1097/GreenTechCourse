package car;

public class EX {


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int temp=10;
		int speed = 0;
		int volume = 0;
		
		TempSystem ts = new TempSystem() {};
		ts.TempOn();
		ts.TempOff();
		temp=ts.setTemp(true,temp);
		temp=ts.setTemp(true,temp);
		temp=ts.setTemp(true,temp);
		temp=ts.setTemp(true,temp);
		
		AccBreakSystem ab = new AccBreakSystem() {};
		
		speed = ab.setSpeed(true, 3, speed);
		speed = ab.setSpeed(true, 2, speed);
		
		AudioSystem as = new AudioSystem() {};
		
		as.AudioOn();
		as.AudioOff();
		volume = as.setVolume(true, volume);
		volume = as.setVolume(true, volume);
		volume = as.setVolume(true, volume);
		volume = as.setVolume(true, volume);
		
//		temp = ts.setTemp(true, temp);
//		AudioSystem as;
//		TempSystem ts;
//		AccBreakSystem ab;
//		
//		
//		as = new Audio();
//		as.AudioOn();
//		as.AudioOff();
//
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(true);
//		as.setVolume(false);
//	
		
//		ts = new Temp();
//		
//		ts.TempOn();
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
//		ts.setTemp(true);
		
//		ab = new AccBreak();
//		
//
//		ab.setSpeed(true, 4);
//		ab.setSpeed("down", 4);
		
//		bs = new Temp();
		
		
	}

}
