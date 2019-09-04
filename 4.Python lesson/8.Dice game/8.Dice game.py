from microbit import *
import random
while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        display.show(str(random.randint(1, 6)))
        