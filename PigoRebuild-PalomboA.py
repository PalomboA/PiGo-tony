from gopigo import *
import time

class Pigo:

    #####
    ##### BASIC STATUS AND METHODS
    #####
    status = {'ismoving' : false, 'servo' : 90, 'leftspeed' : 175,
              'rightspeed' : 175}

    def __init__(self):
        print "I'm a little robot car. Beep beep."

    def stop(self):
        self.isMoving = False
        while stop() != 1:
            time.sleep(.1)
            print "Oh no i can't control myself on these icy roads! HELP!"

    def fwd(self):
        se;f.isMoving = True
        while fwd() != 1
            time.sleep(.1)
            print "I can't do the vroom vroom"

    #####
    ##### COMPLEX METHODS
    #####

    #####
    ##### MAIN APP STARTS HERE
    #####

Mater = Pigo()
Mater.fwd()
Mater.sleep(2)
Mater.stop()

