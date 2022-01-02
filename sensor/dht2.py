import RPi.GPIO as GPIO
import time
import Adafruit_DHT as dht

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

try:
    while 1:
        h, t = dht.read_retry(dht.DHT11, 14)
        print (f'Temp={t:.1f}   Humidity={h:.1f}')
        
        index = (1.8*t)-(0.55*(1-h/100.0)*(1.8*t-26))+32    # 공식에 따라 불쾌지수 계산
        print (f'불쾌지수={index:.1f}')

        if index >= 75.0:           # 불쾌지수가 75 이상이라면
            GPIO.output(20, False)  # GREEN OFF
            GPIO.output(16, True)   # RED ON
        else:                       # 그렇지 않다면, 즉 75 미만이라면
            GPIO.output(16, False)  # RED OFF
            GPIO.output(20, True)   # GREEN ON

        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()