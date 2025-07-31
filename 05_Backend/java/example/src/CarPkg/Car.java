package CarPkg;

public class Car implements ICar {
	private final String model = "";
	private String color;
	private Object glass;
	private Object seat;
	private Engine engine;
	private DashBoard board;
	private boolean isEngineStarted;
	private boolean isWiperOn;
	private boolean isLightOn;
	
	public Car() {
		engine = new Engine();
		isEngineStarted = false;
	}
	
	@Override
	public void turnOnEngine() {
		isEngineStarted = true;
		System.out.println("");
	}

	@Override
	public void turnOffEngine() {
		isEngineStarted = false;
		System.out.println("");
	}

	@Override
	public void turnLeft() {
		System.out.println("좌회전");
	}

	@Override
	public void turnRight() {
		System.out.println("우회전");
	}

	@Override
	public void wiperOn() {
		System.out.println("");
	}

	@Override
	public void wiperOff() {
		System.out.println("");
		
	}

	@Override
	public void wiperUp() {
		System.out.println("");
		
	}

	@Override
	public void wiperDown() {
		System.out.println("");
		
	}

	@Override
	public void lightOn() {
		System.out.println("");
		
	}

	@Override
	public void lightOff() {
		System.out.println("");
		
	}

	@Override
	public void Gear_P() {
		System.out.println("");
		
	}

	@Override
	public void Gear_N() {
		System.out.println("");
		
	}

	@Override
	public void Gear_R() {
		System.out.println("");
		
	}

	@Override
	public void Gear_D() {
		System.out.println("");
		
	}

	@Override
	public void setCarSpeed(int carSpeed) {
		System.out.println("");
		
	}

	@Override
	public void setGear() {
		System.out.println("");
		
	}

	@Override
	public void setWiper(String wiper) {
		System.out.println("");
		
	}

	@Override
	public void showDashboard() {
		System.out.println("============계 기 판============");
		if (isWiperOn) {
			System.out.println("와이퍼 : ON ");
			System.out.println("와이퍼 속도 : " );
		}
		else {
			System.out.println("와이퍼 : OFF");
		}
		
		if (isLightOn) {
			System.out.println("라이트 : ON");
		}
		else {
			System.out.println("라이트 : OFF");
		}
		
		System.out.println("현재 속도 : " + "Km/h");
		System.out.println("현재 기어 : " + "단");
		System.out.println("==============================");
		
	}

	@Override
	public void pushAccPedal() {
		System.out.println("");
		
	}

	@Override
	public void pushBrakePedal() {
		System.out.println("");
	}
}
