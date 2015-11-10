### GOPIGO AUTONOMOUS SCRIPT
### http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time
STOP_DIST = 50

class Pigo:

    def spin(selfself):
        right_rot(360)

    #####
    ##### BASIC STATUS AND METHODS
    #####

    status = {'ismoving' : false, 'servo' : 90, 'leftspeed' : 175,
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

    def checkDist(selfself):
         self.status['dist'] = us_dist(15)
         print "I see something" + str(self.status['dist']) + "mm away."
    #####
    ##### COMPLEX METHODS
    #####s

        def dance(selfself):
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
Mater = Pigo()

while Mater.keepGoing():
    Mater.checkDist()
    Mater.fwd()
    if Mater.keepGoing() == False:
        break
    Mater.sleep(2)
    Mater.stop()

Mater.stop()

