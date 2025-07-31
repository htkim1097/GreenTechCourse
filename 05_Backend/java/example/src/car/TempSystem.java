package car;

public interface TempSystem {
	
	int MIN_TEMP = 16;
	int MAX_TEMP = 28;
	
	
	
	// 메소드
	default void TempOn() {
		System.out.println("에어컨을 킵니다.");
	}
	
	default void TempOff() {
		System.out.println("에어컨을 끕니다.");
	}

	default int setTemp(boolean up_down,int temp) {
		if(up_down) {
			if(temp >= MAX_TEMP) {
				temp = TempSystem.MAX_TEMP;
				System.out.println("최대온도입니다.");
			} else {
				temp += 1;
			}
			
			System.out.println("현재 온도 :" + temp);
		} else if(up_down == false) {
			if(temp < MIN_TEMP) {
				temp = TempSystem.MIN_TEMP;
				System.out.println("최소 온도 입니다.");
			} else {
				temp -= 1;
			}
			
			System.out.println("현재 온도 :" + temp);
			
		}else {
			System.out.println("제대로 된 값을 입력해 주세요.");
		}
		return temp;
	}
	
}
