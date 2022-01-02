import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

i=0
while i<10:
    GPIO.output(16, True)
    time.sleep(0.5)
    GPIO.output(16, False)
    GPIO.output(20, True)
    time.sleep(0.5)
    GPIO.output(20, False)
    GPIO.output(21, True)
    time.sleep(0.5)
    GPIO.output(21, False)
    i += 1

GPIO.cleanup()