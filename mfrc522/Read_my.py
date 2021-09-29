#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        id = reader.read_uid()
        print(id)        
finally:
        GPIO.cleanup()
                
