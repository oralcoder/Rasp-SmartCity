import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir = 12
GPIO.setup(pir, GPIO.IN)

try:
    while 1:
        input = GPIO.input(12)
        print(input)
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()