from gopigo import *
import time
STOP_DIST = 50

class Pigo:

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

    def keepGoing(selfself):
        if self.status['dist'] < STOP_DIST:
            return False
        else:
            return True

    def checkDist(selfself):
         self.status['dist'] = us_dist(15)
         print "I see something" + str(self.status['dist']) + "mm away."
    #####
    ##### COMPLEX METHODS
    #####

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

