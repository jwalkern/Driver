import sys
from time import sleep

battery_status_file = "/sys/class/power_supply/BAT0/state"

print("Monitoring battery status. Press <Ctrl>+C to exit.")

try:
    with open(battery_status_file) as state:
        while True:
            state.seek(0)
            for line in state:
                data = line.split(":")[1].strip().split(" ")[0]
                if "present rate" in line:
                    rate = int(data)
                elif "remaining" in line:
                    remaining = int(data)
            time_left = float(remaining) / rate
            hours = int(time_left)
            minutes = int((time_left - hours) * 60)
            print("\rRemaining time left: %d hours %d minutes," % (hours, minutes))

            sys.stdout.flush()
            sleep(1)
except KeyboardInterrupt:
    print("\nCtrl+C pressed. Exiting")
