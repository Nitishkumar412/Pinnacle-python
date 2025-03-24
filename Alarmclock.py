import time
import pygame
import threading

# Initialize pygame mixer for playing sounds
pygame.mixer.init()

# Function to play the alarm tone
def play_alarm(tone_file):
    pygame.mixer.music.load(tone_file)
    pygame.mixer.music.play(-1)  # Loop the alarm sound

# Function to stop the alarm
def stop_alarm():
    pygame.mixer.music.stop()

# Function to set an alarm
def set_alarm(alarm_time, tone_file, snooze_duration):
    print(f"Alarm set for {alarm_time}. Tone: {tone_file}.")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("ALARM! Wake up!")
            play_alarm(tone_file)
            
            while True:
                action = input("Type 'stop' to stop the alarm or 'snooze' to snooze: ").strip().lower()
                if action == 'stop':
                    stop_alarm()
                    print("Alarm stopped.")
                    return
                elif action == 'snooze':
                    stop_alarm()
                    print(f"Snoozing for {snooze_duration} seconds...")
                    time.sleep(snooze_duration)
                    play_alarm(tone_file)
                else:
                    print("Invalid input. Please type 'stop' or 'snooze'.")
        time.sleep(1)

# Main function to configure the alarm
def main():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ").strip()
    tone_file = input("Enter the path to the alarm tone (e.g., alarm.mp3): ").strip()
    snooze_duration = int(input("Enter snooze duration in seconds: ").strip())

    # Start the alarm in a separate thread
    alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time, tone_file, snooze_duration))
    alarm_thread.start()

if __name__ == "__main__":
    main()
