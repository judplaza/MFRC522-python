#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
class Rfid_rc522:
        def scan_uid(self):
                reader = SimpleMFRC522()
                uid=reader.read_uid()
                uid_hex=hex(uid).upper()
                return uid_hex
if __name__ == "__main__":
        __init__()
        try:
                rf=Rfid_rc522()
                uid = rf.scan_uid()
                print(uid.strip("0X"))
        finally:
                GPIO.cleanup()
                

