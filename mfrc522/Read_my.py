#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id = reader.read_id()
        uid = reader.from_dec_to_hex8(id)
        print("UID hex8: " , uid)
finally:
        GPIO.cleanup()
                

