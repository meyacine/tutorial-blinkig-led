# Blinking LED on Raspberry PI
Tutorial in progress 
الدرس قيد التحرير 
```
import RPi.GPIO as GPIO
```
 GPIO معنى عذا السطر هو اننا نريد إستعمال المكتبة الخاصة بالتحكم في

```
import time
```
معنى عذا السطر هو اننا نريد إستعمال المكتبة الخاصة بالتحكم في الوقت

 BOARD معني السطرين التالين هو اننا نريد إستعمال الدبوس 40 في نظام التعداد
```
LED_GPIO = 40
GPIO.setmode(GPIO.BOARD)
```
يمكننا أن نقوم بنفس

```
GPIO.setup(LED_GPIO, GPIO.OUT)
```
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
