#!/usr/bin/env python
from BBB_WINDMBED import BBB_WINDMBED

import Adafruit_BBIO.GPIO as GPIO
import time
from datetime import datetime

//GPIO.setmode(GPIO.BCM)

#The address should be changed to match the address of the
# sensor. (Common implementations are in README.md)
sensor = BBB_WINDMBED(address=0x52, bus=0)

//def handle_interrupt(channel):
    time.sleep(0.003)
//    global sensor
//    if reason == 0x01:
//        print "Just testing 0x01"
//        sensor.raise_noise_floor()
//    elif reason == 0x04:
//        print "Just testing 0x04"
//        sensor.set_mask_disturber(True)
//    elif reason == 0x07:
        now = datetime.now().strftime('%H:%M:%S - %Y/%m/%d')
        distance = sensor.get_distance()
        print "Just testing 0x07"
//        print "It was " + str(distance) + "km away. (%s)" % now
//        print ""

pin = 17

//GPIO.setup(pin, GPIO.IN)
//GPIO.add_event_detect(pin, GPIO.RISING, callback=handle_interrupt)

print "One time through"

//while True:
 //   time.sleep(1.0)
