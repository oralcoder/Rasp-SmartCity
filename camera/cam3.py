import RPi.GPIO as GPIO
import time
import picamera

pir = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir, GPIO.IN)
picam = picamera.PiCamera()
count = 1

try:
    while 1:
        input = GPIO.input(12)
        print (input)
        if input == 1:
            picam.start_preview()
            picam.start_recording('video%s.h264' % count)  # 촬영될 때 마다 파일 이름 변경
            picam.wait_recording(15)
            picam.stop_recording()
            picam.stop_preview()
            count = count + 1
            time.sleep(0.5)

except KeyboardInterrupt:
    picam.stop_preview()
    picam.close()

GPIO.cleanup()