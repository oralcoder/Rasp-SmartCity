import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN)
try:
    while 1:
        input = GPIO.input(20)
        print(input)
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()