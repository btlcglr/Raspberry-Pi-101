import RPi.GPIO as GPIO
import time

pwmPin=18
ledPin=23
butPin=17

dc=95 #duty cycle (0-100) for PWM pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(pwmPin,GPIO.OUT)
pwm=GPIO.PWM(pwmPin,50)
GPIO.setup(butPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.output(ledPin,GPIO.LOW)
pwm.start(dc)

print('here we go! Press CTRL+C to exi')
try:
    while 1:
        if GPIO.input(butPin):
            pwm.ChangeDutyCycle(dc)
            GPIO.output(ledPin,GPIO.LOW)
        else:
            pwm.ChangeDutyCycle(100-dc)
            GPIO.output(ledPin,GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin,GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()