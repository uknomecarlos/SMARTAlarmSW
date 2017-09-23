import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
previous = True
state = True

tempTime = 0
debounce = 0.2

while True:
    inputValue = GPIO.input(18)
    if((inputValue == False) and (previous == True) and ((time.time() - tempTime) > debounce)):
        if(state == True):
            state = False
        else:
            state = True

        tempTime = time.time()

    GPIO.output(17, not state)
    previous = inputValue
