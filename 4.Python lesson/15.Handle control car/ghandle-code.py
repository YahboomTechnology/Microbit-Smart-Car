# -*- coding: utf-8-*-# Encoding cookie added by Mu Editor
from microbit import display, Image
import ghandle
import radio

display.show(0)
radio.on()
radio.config(group=1)

while True:

    if ghandle.rocker(ghandle.up):
        radio.send('A')
        display.show(Image.ARROW_N)
    elif ghandle.rocker(ghandle.down):
        radio.send('B')
        display.show(Image.ARROW_S)
    elif ghandle.rocker(ghandle.left):
        radio.send('D')
        display.show(Image.ARROW_W)
    elif ghandle.rocker(ghandle.right):
        radio.send('C')
        display.show(Image.ARROW_E)
    elif ghandle.rocker(ghandle.pressed):
        radio.send('0')
        display.show(Image.NO)
    else:
        radio.send('0')
        display.clear()

    if ghandle.B1_is_pressed():
        radio.send('E')
        display.show("R")
    if ghandle.B2_is_pressed():
        radio.send('F')
        display.show("G")
    if ghandle.B3_is_pressed():
        radio.send('G')
        display.show("B")
    if ghandle.B4_is_pressed():
        radio.send('I')
        display.show("Y")