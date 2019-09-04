from microbit import *
import neopixel
display.show(Image.HAPPY)
# The water lamp is connected to pin pin16, the number is 3
np = neopixel.NeoPixel(pin16, 3)
# iterate each LED in the water lights
for pixel_id in range(0, len(np)):
    # Light up the first water light to red
    np[0] = (255, 0, 0)
    # display color
    np.show()
