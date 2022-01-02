import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

scale = [262, 294, 330, 349, 392, 440, 494, 523]

try:
    while 1:
        p = GPIO.PWM(12, 100)       # 100hz로 설정
        p.start(50)                 # Duty cycle를 50으로 설정
        for i in scale:
            p.ChangeFrequency(i)    # Frequency를 scale[] 의 값으로 변경
            time.sleep(1)
        p.stop()                    # PWM Output 정지
        time.sleep(5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()