#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
class Rfid_rc522:
        def __init__(self):
                self.reader = SimpleMFRC522()
        def read_uid(self):
                id = self.reader.read_id()
                return (hex(id).upper()[2:10])
if __name__ == "__main__":
        __init__()
        try:
                rf=Rfid_rc522()
                uid = rf.scan_uid()
                print(uid)
        finally:
                GPIO.cleanup()
                

