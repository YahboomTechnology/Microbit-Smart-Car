from microbit import *
import neopixel
display.show(Image.HAPPY)
# The water lamp is connected to pin pin16, the number is 3
np = neopixel.NeoPixel(pin16, 3)
while True:
    for pixel_id in range(0, len(np)):
        np[0] = (255, 0, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 255)
        np.show()
        sleep(200)
        np.clear()
        np[2] = (0, 0, 255)
        np.show()
        sleep(200)
        np.clear()
        np[0] = (255, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        np[1] = (0, 255, 0)
        np.show()
        sleep(200)
        np.clear()
        np[2] = (255, 0, 255)
        np.show()

        sleep(200)
        np.clear()