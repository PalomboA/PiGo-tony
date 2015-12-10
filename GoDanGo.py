#GOPIGO AUTONOMOUS, INSTANTIATED CLASS
#GoPiGo API: http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
import time

#Global variable on how close an object is allowed to get
STOP_DIST = 50

class Pigo:

    #######
    #######  BASIC STATUS AND METHODS
    #######

    #status array holds lots of key information. access it using self.status["KEY"]
    status = {"ismoving": False, "servo": 90, "leftspeed": 175,
              "rightspeed": 175, 'dist': 100, "wentleft": True}
    vision = [None] * 180  #will hold our sensor data
    STEPPER = 5  #keeps track of how fast we count up in our servo sweeps

    # this method means we're working with an instantiated object
    def __init__(self):
        print "I'm a little robot car. beep beep."
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "Whoaaaa there."
        for x in range(3):   #we send three so one of them will be heard by the MCU
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "Let's get going!"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["ismoving"] = True
        print "Back, back it up!"
        for x in range(3):
            bwd()

    def rightrot(self):
        self.status["ismoving"] = True
        print "Rotating right!"
        for x in range(3):
            right_rot()

    def leftrot(self):
        self.status["ismoving"] = True
        print "Rotating left!"
        for x in range(3):
            left_rot()

    #Check if conditions are safe to continue operating and returns true/false
    def keepGoing(self):
        self.checkDist()
        if self.status['dist'] < STOP_DIST:
            print "Obstacle detected. Stopping."
            return False
        elif volt() > 14 or volt() < 6:
            print "Unsafe voltage detected: " + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        servo(90)
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away."

    #######
    #######  ADVANCED METHODS
    #######


    def safeDrive(self):
        print "Let's roll."
        self.fwd()
        while self.keepGoing():
            time.sleep(.05)
        self.stop()

    def servoSweep(self):
        print "Scanning..."
        for ang in range(20, 160, self.STEPPER):
            servo(ang)
            time.sleep(.1)
            self.vision[ang] = us_dist(15)

    def dance(self):
        print "I just want to DANCE!"
        '''
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.shuffle()
            self.servoShake()
            self.blink()
        '''

    #checks to see if there is any 20 degree opening at all
    def findaPath(self):
        counter = 0
        for ang in range(20, 160, self.STEPPER):
            if self.vision[ang] > STOP_DIST:
                counter += 1
            else:
                counter = 0
            if counter >= (20/self.STEPPER):
                print "We've found a path at angle " + str(ang)
                return True   #returns when you find the first available path
        return False   #no paths were found. We're going to have to turn around

    def turnAround(self):
        print "Attempting to turn around"
        self.rightrot()
        time.sleep(.5)
        self.stop()

    #returns the smartest angle we should turn to when facing an obstacle
    #it will check our instance variable self.status['wentleft']
    def findAngle(self):
        counter = 0
        option = [0] * 12 #we're going to fill this array with the angles of open paths
        optindex = 0  #this starts at 0 and will increase every time we find an option
        for ang in range(20, 160, self.STEPPER):
            if self.vision[ang] > STOP_DIST:
                counter += 1
            else:
                counter = 0
            if counter >= (20/self.STEPPER):
                print "We've found an option at angle " + str(ang - 10)
                option[optindex] = (ang - 10)
                counter = 0
                optindex += 1
        if self.status['wentleft']:
            print "I went left last time. Seeing if I have a right turn option"
            for choice in option:
                if choice < 90:
                    self.status['wentleft'] = False #switch this for next time
                    return choice
        else:
            print "Went right last time. Seeing if there's a left turn option"
            for choice in option:
                if choice > 90:
                    self.status['wentleft'] = True
                    return choice
        print "I couldn't turn the direction I wanted. Goint to use angle " + str(option[0])
        if option[0] != 0: #let's make sure there's something in there
            return option[optindex]
        print "If I print this line I couldn't find an angle. How'd I get this far?"
        return 90


    #takes an angle as its parameter an attempts to turn that way
    def turnTo(self, angle):
        turntime = .2   #MAY NEED ADJUSTMENT
        BIGTURN = .5    #MAY NEED ADJUSTMENT
        if angle < 50 or angle > 120:
            print "We're going to need a big turn"
            turntime = BIGTURN
        if angle < 90:
            print "Turning right"
            self.rightrot()
            time.sleep(turntime)
            self.stop()
        else:
            print "Turning left"
            self.leftrot()
            time.sleep(turntime)
            self.stop()


#######
#######  MAIN APP STARTS HERE
#######
tina = Pigo()

while True:
    if tina.keepGoing():
        tina.safeDrive()
    if tina.findaPath():
        tina.turnTo(tina.findAngle())
    else:
        tina.turnAround()

tina.stop()

