import RPi.GPIO as GPIO
import threading
import time
from time import sleep
from threading import *

#sensor = 21
sample = 15 
count = 0
start = 0
end = 0
        
def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21,GPIO.IN)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)

class motordriver(Thread):
    def run(self):
        P = GPIO.PWM(4,100)
        P.start(0)
        duty_cycle=10
        while(1):
            GPIO.output(17, True)
            GPIO.output(22, False)
            P.ChangeDutyCycle(duty_cycle)
            GPIO.output(4, True)
            duty_cycle=duty_cycle+10;
            if(duty_cycle>100):
                duty_cycle=10
            sleep(5)
            GPIO.output(4,False)
 
class tachometer(Thread):
    def run(self):
        def set_start():
            global start
            start = time.time()

        def set_end():
            global end
            end = time.time()

        def get_rpm(c):
            global count 
            if not count:
                set_start() # create start time
                count = count + 1 # increase counter by 1
            else:
                count = count + 1

            if count == sample:

                set_end() # create end time
                delta = end - start
                # time taken to do a half rotation in seconds
                delta = delta / 60 # converted to minutes
                rpm = (sample / delta) / 2 # converted to time for a full single rotation
                angular_velocity=(rpm*44)/420 #speed of that vehicle in m/minute
                speed = (angular_velocity * 0.05)
                print (speed)
                count = 0 # reset the count to 0

        GPIO.add_event_detect(21, GPIO.RISING, callback=get_rpm)
        # execute the get_rpm function when a HIGH signal is detected
        
def destroy():
            GPIO.cleanup()


if __name__ == "__main__":
            setup()
            t1 = motordriver()
            t2 = tachometer()
            #t3 = your logic()
            try:
                t1.start()
                t2.start()
                #t3.start()
                #loop()
            except KeyboardInterrupt:
                destroy()
else:
    print("not executing")

