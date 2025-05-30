import spidev
import time
import RPi.GPIO as GPIO
 
LATCH_PIN = 11
SRCLR_PIN = 13
RESTART_PIN = 29

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LATCH_PIN, GPIO.OUT)
GPIO.setup(SRCLR_PIN, GPIO.OUT)
GPIO.setup(RESTART_PIN, GPIO.OUT)


GPIO.output(LATCH_PIN, GPIO.HIGH)
GPIO.output(SRCLR_PIN, GPIO.HIGH)
GPIO.output(RESTART_PIN, GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0, 0)

spi.max_speed_hz = 100000
spi.mode = 0b00

try:
    print("Testing")

    spi.writebytes([0b00000000, 0b00000100])
    print("All outputs ON")
    time.sleep(2)
    print(0b10000000)
    
    spi.writebytes([0b00000000, 0b00000000])
    print("All outputs OFF")
    time.sleep(2)

finally:
    spi.close()
    GPIO.cleanup()
