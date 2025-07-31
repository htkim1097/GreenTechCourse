package Car;

public class Run extends Three{

	public static void main(String[] args) {
		
		// ----------사용예시-----------
		// 처음 사용할 때
		IThree tre = new Three();
		
		// 와이퍼 사용
		tre.wiperOn();
		
		// 와이퍼 속도 증가
		tre.wiperUp();
		tre.wiperUp();
		
		// 라이트 사용
		tre.lightOn();
		
		// 기어를 P단으로 바꾸기
		tre.Gear_P();
		
		// 속도 값을 매개변수로 넣어주세요
		tre.setCarSpeed(100);
		
		// 계기판 정보 출력
		tre.ShowDashboard();
	}
}
