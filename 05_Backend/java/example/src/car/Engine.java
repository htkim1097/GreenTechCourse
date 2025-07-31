package car;

public class Engine {

	 public boolean isOn = false;

	 
	 public void engineOn() {
		 this.isOn =true;
		 System.out.println("시동이 걸렸습니다");
		 
	 }
	 
	 public void engineOff() {
		 this.isOn =false;
		 System.out.println("시동이 꺼졌습니다");
		 
	 }

}
	 


