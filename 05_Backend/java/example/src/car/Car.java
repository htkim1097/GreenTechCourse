package car;

public class Car  {
		Glass glass;
		Seat seat;
		Handle handle;
		Engine engine;
		Pedal pedal;
		InfoSystem infosystem;
		Tire tire;
		Wifer wifer;
		Dashboard dashboard;
		
		String model;
		String color;
	  	 
		IThree board = new Three();
	 	
		int temp=16;
		int speed = 0;
		int volume = 0;
		
		boolean au_on = false;
		boolean tp_on = false;
		
		
		TempSystem ts = new TempSystem() {};
		AccBreakSystem ab = new AccBreakSystem() {};
		AudioSystem as = new AudioSystem() {};


		public Car(String m, String c) {
			this.glass = new Glass();
			this.seat = new Seat();
			this.handle = new Handle();
			this.engine = new Engine();
			this.pedal = new Pedal();
			this.infosystem = new InfoSystem();
			this.tire = new Tire();
			this.wifer = new Wifer();
			this.dashboard = new Dashboard();
			this.model = m;
			this.color =c;
//			board ;
		}


		public void engineOn() {
			this.engine.engineOn();

		}
		public void engineOff() {
			this.engine.engineOff();
		}
		

		public void AudioOn() {
			if(this.engine.isOn==true) {
				as.AudioOn();
				this.au_on = true;

			}
		}
		public void AudioOff() {
			if(this.engine.isOn==true) {
				as.AudioOff();
				this.au_on = false;

			}
		}
		
		public void setGear(String gear) {
			if (gear.equals("P")) {
				this.board.Gear_P();
				System.out.println("기어를 P로 바꿨습니다");
				this.speed =0;
				board.setCarSpeed(this.speed);


			}
			else if (gear.equals("R")) {
				this.board.Gear_R();
				System.out.println("기어를 R로 바꿨습니다");

			}
			else if (gear.equals("N")) {
				this.board.Gear_N();
				System.out.println("기어를 N로 바꿨습니다");
				this.speed =0;
				board.setCarSpeed(this.speed);

			}
			else if (gear.equals("D")) {
				this.board.Gear_D();
				System.out.println("기어를 D로 바꿨습니다");
			}
 
		}
		
		public void setSpeed(boolean up, int time) {
			if(this.engine.isOn) {
			String gear = board.getGear();
			if (gear.equals("P")) {
				System.out.println("기어가 p입니다");
				this.speed=0;
			}
			else if (gear.equals("R")) {
				System.out.println("후진합니다");
				this.speed = ab.setSpeed(up, time, this.speed);
			}
			else if (gear.equals("D")){
				this.speed = ab.setSpeed(up, time, this.speed);
			}
			else if(gear.equals("N")) {
				System.out.println("기어가 N입니다");
				this.speed=0;
			}
		
			board.setCarSpeed(this.speed);
			}
			else {
				System.out.println("시동이 꺼져있습니다");
			}
		}
		
		public void turn(String RL) {
			if(this.engine.isOn) {

			if(RL.equals("R")) {
				if(this.speed>0 && (board.getGear().equals("D") || board.getGear().equals("R"))) {
					this.handle.turnRight();
				}
			}
			else if(RL.equals("L")) {
				if(this.speed>0 && (board.getGear().equals("D")|| board.getGear().equals("R"))) {
					this.handle.turnLeft();
				}
			}	
			}
		}
		
		public void showDashboard() {
			if(this.engine.isOn) {

			this.board.ShowDashboard();
			}
		}
		

		public void setVolume(boolean up) {
			if(this.engine.isOn && this.au_on) {

				int v=as.setVolume(up, this.volume);
				this.volume = v;
			}

		}
		
		public void tempOn() {
			if(this.engine.isOn) {
				ts.TempOn();
				this.tp_on = true;
			}
		}
		public void tempOff() {
			if(this.engine.isOn) {
				ts.TempOff();
				this.tp_on = false;

			}
		}
		public void setTemp(boolean up) {
			if(this.engine.isOn && this.tp_on) {
				int temp =ts.setTemp(up, this.temp);
				this.temp = temp;
			}
		}
		
	
	}

