from RPi import GPIO
from tkinter import *
from time import sleep

clk=23
dt=24
servo=18


GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)
GPIO.setup(clk,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

counter=0
clkLastState=GPIO.input(clk)

pwm=GPIO.PWM(servo,100)
pwm.start(5)
GPIO.setwarnings(False)

master=counter
class App:
    def __init__(self,master):
        frame= Frame(master)
        frame.pack()
        scale=Scale(frame,from_=0,to=180,orient=HORIZONTAL,command=self.update)
        scale.grid(row=0)
    def update(self,angle):
        duty=float(angle)/10.0+2.5
        pwm.ChangeDutyCycle(duty)
root= Tk()
root.wm_title('Servo Control')
app= App(root)
root.geometry("200x50+0+0")
root.mainloop()

try:
    while True:
        clkState=GPIO.input(clk)
        dtState=GPIO.input(dt)
        if clkState !=clkState:
            if dtState !=dtState:
                counter +=1
            else:
                counter -=1
        print(counter)
        clkLastState=clkState
        sleep(0.01)
finally:
    GPIO.cleanup()

