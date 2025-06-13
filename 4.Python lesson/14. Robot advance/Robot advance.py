from microbit import *
import buildingbit

buildingbit.car_run(255, 255, 0)
buildingbit.servo(1, 0)
sleep(1000)
buildingbit.servo(1, 180)
sleep(1000)
