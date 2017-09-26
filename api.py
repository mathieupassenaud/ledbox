#!/usr/bin/python
import os
from flask import Flask, request, send_from_directory
from neopixel import *

app = Flask(__name__)

@app.route('/leds', methods=['POST'])
def leds():
    content = request.get_json()
    for led in content:
        changeLed(led["num"], led["r"], led["g"], led["b"])
    return "ok"

def changeLed(num, r, g, b):
    global strip
    print "set color"
    print r
    print g
    print b
    strip.setPixelColor( num , Color(g, r, b) )
    strip.show()

if __name__ == '__main__':
    global stip
    LED_COUNT = 10
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 5
    LED_BRIGHTNESS = 255
    LED_INVERT = False
    strip = Adafruit_NeoPixel( LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    strip.begin()
    app.run(host='0.0.0.0', port=5555, debug=True)
