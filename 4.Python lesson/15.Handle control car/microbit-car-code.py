from microbit import *
import buildingbit
import radio
import neopixel

display.show(Image.HAPPY)
radio.on()
radio.config(group=1)
np = neopixel.NeoPixel(pin16, 3)
while True:
    value = radio.receive()
    if value == "A":
        buildingbit.car_run(100, 100, 0)
    elif value == "B":
        buildingbit.car_back(100, 100, 0)
    elif value == "C":
        buildingbit.car_spinright(100, 100, 0)
    elif value == "D":
        buildingbit.car_spinleft(100, 100, 0)
    elif value == "0":
        buildingbit.car_stop()
    elif value == "E":
        np.clear()
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np[2] = (255, 0, 0)
        np.show()
    elif value == "F":
        np.clear()
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np.show()
    elif value == "G":
        np.clear()
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np[2] = (0, 0, 255)
        np.show()
    elif value == "I":
        np.clear()
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np.show()
