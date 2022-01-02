import time
import picamera                         # 카메라 라이브러리 사용

picam = picamera.PiCamera()             # piCam 객체 생성

picam.start_preview()                   # 카메라 미리보기 모드 실행

picam.start_recording('./video.h264')     # 동영상 촬영 시작
picam.wait_recording(15)                # 15초간 동영상 촬영
picam.stop_recording()                  # 동영상 촬영 종료

picam.stop_preview()                    # 카메라 미리보기 종료
picam.close()

# vlc video.h264