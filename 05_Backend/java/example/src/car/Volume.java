package car;

public interface Volume {
	int MAX_VOLUME = 100;
	int MIN_VOLUME = 0;


	public void volumeOn();

	public void volumeOff();

	public void setVolume(String up_down);
}
