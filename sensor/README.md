# GPIO 모듈 설치

```
sudo apt-get install python3-dev
sudo apt-get install python3-rpi.gpio
```

# 작업 디렉토리 생성

```
mkdir /home/pi/works/sensor
cd /home/pi/works/sensor
```

# DHT11 라이브러리 설치

```
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
```
