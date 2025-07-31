package car;

public interface AudioSystem {
	// 상수 필드 

	int MIN_VOLUME = 0;
	int MAX_VOLUME = 100;
	
	

	default void AudioOn() {
		System.out.println("오디오를 켭니다.");
	}
	
	
	default void AudioOff() {
		System.out.println("오디오를 끕니다.");

	}
	
//	public void setVolume(int volume);
	
	default int setVolume(boolean up_down, int volume) {
//		if(up_down.equals("up")) {
		if(up_down) {
			if(volume >= 100) {
				volume = AudioSystem.MAX_VOLUME;
				System.out.println("최대볼륨입니다.");
			} else {
				volume += 10;
			}
			
			System.out.println("현재 볼륨 :" + volume);
		} else if(up_down == false){
			if(volume < 0) {
				volume = AudioSystem.MIN_VOLUME;
				System.out.println("최소볼륨입니다.");
			} else {
				volume -= 10;
			}
			
			System.out.println("현재 볼륨 :" + volume);
			
		}else {
			System.out.println("제대로 된 값을 입력해 주세요.");
		}
		return volume;
	
	}
	
	
	// 탬프(온,오프)
	// 에어컨 최저 16도 최고 28도
	// 오디오 최저 0 최고 100
	// 정수형 현재 온도값
	// 정수형 현재 볼륨값
	
	// 상태값을 boolean으로 받아서-> 온일때 에어컨 조작이 가능하게하게고 온도조절을 16~28도까지 가능하게하고 현재 온도 저장 가능한상태로 만들기.
	// 오디오도 같은 맥락으로 0~100까지 볼륨조절,저장 가능하게 같은 방식으로 설계
	
	// 엑셀,브레이크는 각각 boolean으로 true false를 받아서
	// 시간초도 같이 변수로 받을 수 있게 해서 true일때
	// 지속시간에 따라서 고정 속도가 증가하거나 감소할 수 있게 설계
	
	// 추상메소드없이 디폴트 or 스태틱메소드만 사용해서 드라이버쪽에서 함수호출만으로 사용할 수 있게 설계.
	
}
