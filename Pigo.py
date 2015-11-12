### GOPIGO AUTONOMOUS SCRIPT
### http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time
STOP_DIST = 75

class Pigo:


    #####
    ##### BASIC STATUS AND METHODS
    #####

    status = {'ismoving' : False, 'servo' : 90, 'leftspeed' : 175,
              'rightspeed' : 175, 'dist': 100}

    def __init__(self):
        print "I'm a little robot car. Beep beep."
        self.status['dist'] = us_dist(15)

    def stop(self):
        self.status["ismoving"] = False
        print "STOPPP."
        for x in range(3):
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "Let's get going."
        for x in range(3):
            fwd()

    # Check if the conditions are safe for the Pigo to continue
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "Obstacle within stop distance."
            return False
        elif volt() > 14 or volt() < 6:
            print "Voltage outside of safe range." + str(volt())
            return False
        else:
            return True

    def checkDist(self):
         self.status['dist'] = us_dist(15)
         print "I see something" + str(self.status['dist']) + "mm away."
    #####
    ##### COMPLEX METHODS
    #####
    def spin(self):
        right_rot()
        time.sleep(3)
        self.stop()

    def shakeServo(self):
        for x in range(10):
            if x % 2 == 0:
                servo(120)
                time.sleep(.1)
            else:
                servo(20)
                time.sleep(.1)

    def shuffle(self):
        motor_fwd()
        time.sleep(1)
        motor_bwd()
        time.sleep(1)
        motor_fwd()
        time.sleep(1)
        motor_bwd()
        time.sleep(1)
        self.stop()

    def rturn(self):
        right()

    def lturn(self):
        left()

    def blink(self):
        for x in range(10):
            if x % 2 == 0:
                led_on()
                time.sleep(.1)
                led_off()
            else:
                servo(20)
                time.sleep(.1)

    def dance(self):
        print "I just want to DANCE!"
        self.spin()
        self.shuffle()
        self.shakeServo()
        self.rturn()
        self.lturn()
        self.blink()


    #####
    ##### MAIN APP STARTS HERE
    #####
MaterPi = Pigo()


while MaterPi.keepGoing():
    MaterPi.checkDist()
    MaterPi.fwd()
    if MaterPi.keepGoing() == False:
        break
    MaterPi.sleep(2)
    MaterPi.stop()

MaterPi.stop()

