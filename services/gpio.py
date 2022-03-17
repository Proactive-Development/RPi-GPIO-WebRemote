import RPi.GPIO as GPIO
def configure(pin,mode):
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(int(pin), GPIO.OUT)
    print(mode)
    if mode.upper() == "HIGH":
        print("set High")
        GPIO.output(int(pin), GPIO.HIGH)
    if mode.upper() == "LOW":
        print("set Low")
        GPIO.output(int(pin), GPIO.LOW)
    