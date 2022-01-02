import RPi.GPIO as GPIO
import time
import Adafruit_DHT as dht

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.IN)

# try 블럭 안에 있는 구문 수행. 만약 예외(오류)가 발생한다면 except 블럭으로 이동
try:
    while 1:
        h, t = dht.read_retry(dht.DHT11, 14)
        print (f'Temp={t:.1f}   Humidity={h:.1f}')

        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()