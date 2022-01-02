import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

servo = 12
GPIO.setup(servo, GPIO.OUT)

try:
    p = GPIO.PWM(servo, 50)
    p.start(2.5)                    # 0도로 초기화

    while 1:
        p.ChangeDutyCycle(7.5)      # 90도로 회전
        time.sleep(1)
        p.ChangeDutyCycle(12.5)     # 180도로 회전
        time.sleep(1)
        p.ChangeDutyCycle(2.5)      # 0도로 회전
        time.sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()