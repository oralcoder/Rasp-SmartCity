import time
import picamera                 # 카메라 라이브러리 사용

picam = picamera.PiCamera()     # piCam 객체 생성
picam.start_preview()           # 카메라 미리보기 모드 실행
time.sleep(10)
picam.stop_preview()            # 카메라 미리보기 모드 종료
picam.capture('./photo.jpg')    # 장면 캡쳐 및 저장
picam.close()                   # 카메라 종료

# gpicview photo.jpg