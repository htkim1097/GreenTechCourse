package Car;

public class Three implements IThree {
	private final int WIPER_MAX = 5;
	private final int WIPER_MIN = 0;
	private int wiperSpeed = 0;
	private boolean wiperCheck;
	private boolean lightCheck;
	private int carSpeed;      // 자동차 속도
    private String gear;       // 기어 상태: P, R, N, D
    private String wiper;      // 와이퍼 상태: Y/N
	
	public Three() {
        this.carSpeed = 0;
        this.gear = "P";
        this.wiper = "0";
	}
    
    // Getter/Setter
	@Override
    public int getCarSpeed() {
        return carSpeed;
    }

    @Override
    public void setCarSpeed(int carSpeed) {
        this.carSpeed = carSpeed;
    }

    @Override
    public String getGear() {
        return gear;
    }

    @Override
    public String getWiper() {
        return wiper;
    }

    @Override
    public void setWiper(String wiper) {
        this.wiper = wiper;
    }

	@Override
	public void Gear_P() {
		gear = "P";
	}

	@Override
	public void Gear_N() {
		gear = "N";
	}

	@Override
	public void Gear_R() {
		gear = "R";
	}

	@Override
	public void Gear_D() {
		gear = "D";
	}

	@Override
	public void lightOn() {
		lightCheck = true;
//		System.out.println("안내 : 라이트를 켰습니다.");
	}

	@Override
	public void lightOff() {
		lightCheck = false;
//		System.out.println("안내 : 라이트를 껐습니다.");
	}

	@Override
	public void wiperOn() {
		wiperCheck = true;
//		System.out.println("안내 : 와이퍼를 켰습니다.");
	}

	@Override
	public void wiperOff() {
		wiperCheck = false;
//		System.out.println("안내 : 와이퍼를 껐습니다.");
	}

	@Override
	public void wiperUp() {
		
		if (WIPER_MIN <= wiperSpeed && wiperSpeed < WIPER_MAX) {
			++wiperSpeed;
//			System.out.println("안내 : 와이퍼 속도를 올립니다. 현재속도 : " + wiperSpeed);
		} else if (wiperSpeed >= WIPER_MAX) {			
			//this.wiperSpeed = wiperSpeed;
			wiperSpeed = 5;
//			System.out.println("안내 : 와이퍼 속도는 최대 5까지 가능합니다. 현재속도 : " + wiperSpeed);
		}
	}

	@Override
	public void wiperDown() {
		
		if(WIPER_MIN < wiperSpeed && wiperSpeed <= WIPER_MAX) {
			--wiperSpeed;
//			System.out.println("안내 : 와이퍼 속도를 내립니다. 현재속도 : " + wiperSpeed);			
		} else if (wiperSpeed == WIPER_MIN) {
//			System.err.println("안내 : 현재 와이퍼 속도가 0 입니다.");
		}
	}
	
	@Override
	public void ShowDashboard() {
		System.out.println("============계 기 판============");
		if (wiperCheck) {
			System.out.println("와이퍼 : ON ");
			System.out.println("와이퍼 속도 : " + wiperSpeed);
		}
		else {
			System.out.println("와이퍼 : OFF");
		}
		
		if (lightCheck) {
			System.out.println("라이트 : ON");
		}
		else {
			System.out.println("라이트 : OFF");
		}
		
		System.out.println("현재 속도 : " + carSpeed + "Km/h");
		System.out.println("현재 기어 : " + gear + "단");
		System.out.println("==============================");
	}
}
