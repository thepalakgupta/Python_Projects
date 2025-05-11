import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(f"⏳ Time Left: {time_format}", end='\r')
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's up!")

def main():
    print("🕒 Countdown Timer")
    try:
        total_seconds = int(input("Enter time in seconds: "))
        countdown_timer(total_seconds)
    except ValueError:
        print("Please enter a valid number.")

# Run the timer
main()
