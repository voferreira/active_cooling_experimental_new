import spidev
import time
import RPi.GPIO as GPIO
 
LATCH_PIN = 11
SRCLR_PIN = 13
NSLEEP_PIN = 15

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LATCH_PIN, GPIO.OUT)
GPIO.setup(SRCLR_PIN, GPIO.OUT)
GPIO.setup(NSLEEP_PIN, GPIO.OUT)


GPIO.output(LATCH_PIN, GPIO.HIGH)
GPIO.output(SRCLR_PIN, GPIO.HIGH)
GPIO.output(NSLEEP_PIN, GPIO.HIGH)

spi = spidev.SpiDev()
spi.open(0, 0)

spi.max_speed_hz = 100000
spi.mode = 0b00

def latch_data():
    GPIO.output(LATCH_PIN, GPIO.LOW)
    time.sleep(0.001)
    GPIO.output(LATCH_PIN, GPIO.HIGH)
    time.sleep(0.001)

try:
    print("Testing")

    spi.writebytes([0x01])
    print(spi.readbytes(0))
    latch_data()
    print("All outputs ON")
    time.sleep(2)
    
    spi.writebytes([0x00])
    latch_data()
    print("All outputs OFF")
    time.sleep(2)

    for i in range(8):
        val = 1 << i
        spi.writebytes([val])
        print(spi.readbytes(0))
        latch_data()
        print(f"Output {i} ON")
        time.sleep(1)

finally:
    spi.close()
    GPIO.cleanup()