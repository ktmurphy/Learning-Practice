#! python3

import time, subprocess

timeLeft = int(input("Set countdown timer. Enter integer:"))
while timeLeft > 0:
    print(timeLeft, end="")
    time.sleep(1)
    timeLeft -= 1
try:
    # doesn't work, but that's ok - got the gist of it
    subprocess.Popen("C:\\Program Files (x86)\\Windows Media Player", "alarm.wav")
except:
    print("\nWake up")
