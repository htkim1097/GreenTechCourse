package car;

public class VolumeClass implements Volume {

	// 필드
	private int volume;

	// turnOn() 추상 메소드의 실체 메소드
	@Override
	public void volumeOn() {
		System.out.println("Audio를 켭니다.");
	}

	@Override
	// turnOff() 추상 메소드의 실체 메소드
	public void volumeOff() {
		System.out.println("Audio를 끕니다.");
	}

	// setVolume() 추상 메소드의 실체 메소드
	@Override
	public void setVolume(String up_down) {
		if (up_down.equals("up")) {
			if (volume > Volume.MAX_VOLUME) {
				this.volume = Volume.MAX_VOLUME;
				System.out.print("최대값을 초과하였습니다.");
			} else {
				this.volume += 20;
			}
			System.out.println("현재 볼륨: " + volume); // ✅ 이게 반드시 필요!

		} else if (up_down.equals("down")) {
			if (volume < Volume.MIN_VOLUME) {
				this.volume = Volume.MIN_VOLUME;
				System.out.println("최소값을 초과하였습니다.");
			} else {
				this.volume -= 20;
			}
			System.out.println("현재 볼륨: " + volume);

		}
		else {
			System.out.println("잘못된 명령입니다. 'up' 또는 'down'을 입력하세요.");
		}

//		if (volume > Volume.MAX_VOLUME) {
//			this.volume = Volume.MAX_VOLUME;
//		} else if (volume < Volume.MIN_VOLUME) {
//			this.volume = Volume.MIN_VOLUME;
//		} else {
//			this.volume = volume;
//		}
//		System.out.println("현재 Audio 볼륨: " + this.volume);
	}



}
