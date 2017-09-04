import RPi.GPIO as GPIO
import time

# constante pin GPIO
LED_GPIO = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_GPIO, GPIO.OUT)
try: 
    while True:
        GPIO.output(LED_GPIO, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_GPIO, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    print "Exit"

finally:
    GPIO.cleanup()
