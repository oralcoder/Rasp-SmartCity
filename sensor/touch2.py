import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

try:
    while 1:
        input = GPIO.input(20)
        print(input)
        if input == 1:
            GPIO.output(16, True)
        else:
            GPIO.output(16, False)

        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()