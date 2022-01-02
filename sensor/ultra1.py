import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

echo = 13
trig = 19
GPIO.setup(echo, GPIO.IN)     # ECHO
GPIO.setup(trig, GPIO.OUT)    # TRIG

try:
    while 1:
        GPIO.output(trig, False)          # Trig 핀 초기화
        time.sleep(0.05)
        GPIO.output(trig, True)           # Trig 핀으로 초음파 방사
        time.sleep(0.00001)
        GPIO.output(trig, False)          # Trig 핀 OFF
        while GPIO.input(echo) == 0:    # 초음파가 방사되면 echo는 반사된 값을 받기 위해 ON 상태가 됨
            start = time.time()             
        while GPIO.input(echo) == 1:    # 반사된 값이 수신되면 echo는 OFF 상태가 됨
            end = time.time()
        
        duration = end - start          # round trip 시간
        distance = duration * 17000     # 공식에 의해 거리 계산
        distance = round(distance, 1)   # 소수점 한 자리로 반올림
        print (f'distance={distance:.1f}')
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()