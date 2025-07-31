package car;

public interface AccBreakSystem {

	int MIN_SPEED = 0;
	int MAX_SPEED = 180;
	
	
		
	default int setSpeed(boolean up_down,int time, int speed) {
		if(up_down) {
			if(speed >= 180) {
				speed = AccBreakSystem.MAX_SPEED;
				System.out.println("최대속도입니다.");
			} else {
				speed += 20 * time;
			}
			
			System.out.println("현재 속도 :" + speed + "/" + time + "초간 악셀을 밟았습니다.");
			
		} else if(up_down == false) {
			if(speed < 0) {
				speed = AccBreakSystem.MIN_SPEED;
				System.out.println("최소속도입니다.");
			} else {
				speed -= 20 * time;
			}
			
			System.out.println("현재 속도 :" + speed + "/" + time + "초간 브레이크를 밟았습니다.");
			
		}else {
			System.out.println("제대로 된 값을 입력해 주세요.");
		}
		return speed;
}
	
}
