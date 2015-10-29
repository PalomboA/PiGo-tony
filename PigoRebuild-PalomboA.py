from gopigo import *
import time

class Pigo:

    isMoving = False
    servoPos = 90

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
            print "I can't dp the vroom vroom"

Mater = Pigo()
Mater.fwd()
Mater.sleep(2)
Mater.stop()

