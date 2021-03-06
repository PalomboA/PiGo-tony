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
    vision = [None] * 180

    def __init__(self):
        print "I'm a little robot car. Beep beep."
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "Stopping."
        for x in range(3):
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "Let's get going."
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["ismoving"] = True
        print "Let's back up."
        for x in range(3):
            bwd()

    # Check if the conditions are safe for the Pigo to continue
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "I think I see something in the distance."
            self.checkDist()
            if self.status['dist'] < STOP_DIST:
                print "Yep, there is for sure something big out there"
                return False
        elif volt() > 14 or volt() < 6:
            print "Voltage outside of safe range." + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away."
        if self.status['dist'] < STOP_DIST:
            return False
        else:
            return True


    #####
    ##### COMPLEX METHODS
    #####

    def spin(self):
        right_rot()
        time.sleep(2)
        self.stop()

    def safeDrive(self):
        self.fwd()
        while self.checkDist():
            time.sleep(.05)
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)
            self.vision[ang] = us_dist(15)

    def shakeServo(self):
        for x in range(10):
            if x % 2 == 0:
                servo(120)
                time.sleep(.1)
            else:
                servo(20)
                time.sleep(.1)

    def shuffle(self):
        for x in range(3):
            self.fwd()
            time.sleep(.5)
            self.bwd()
            time.sleep(.5)
            self.stop()

    def rturn(self):
        for x in range(3):
            right_rot()
        time.sleep(1)
        self.stop()

    def lturn(self):
        for x in range(3):
            left_rot()
        time.sleep(1)
        self.stop()

    def blink(self):
        for x in range(10):
            if x % 2 == 0:
                led_on(1)
                time.sleep(.1)
                led_off(1)
            else:
                servo(20)
                time.sleep(.1)

    def dance(self):
        print "I just want to spin!"
        self.spin()
        print "I just want to shuffle!"
        self.shuffle()
        print "I just want to shake my servo!"
        self.shakeServo()
        print "I just want to turn right!"
        self.rturn()
        print "I just want to turn left!"
        self.lturn()
        print "I just want to blink!"
        self.blink()
        print "I just want to shake my servo again!"
        self.shakeServo()



    def isThereOpening(self):
        counter = 0
        for ang in range(20, 160, 5):
            if self.vision[ang] > STOP_DIST:
                counter += 1
            else:
                counter = 0
            if counter == 4:
                return True
        return False

    def turnTo(self, angle):
        turn = .25  #MAY NEED ADJUSTING
        print "Turning a small angle."
        TURN = .5   #MAY NEED ADJUSTING
        print "Turning a large angle."
        if angle > 120 or angle < 50:
            turn = TURN
        if angle < 80:
            print "We're turning right"
            self.rturn()
            time.sleep(turn)
            self.stop()
        else:
            print "we're turning left"
            self.lturn()
            time.sleep(turn)
            self.stop()


    def turnAround(self):
        self.rturn()
        time.sleep(1) #MAY NEED ADJUSTING
        print "SLEEPING!"
        self.stop()


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
            return option[0]
        print "If I print this line I couldn't find an angle. How'd I get this far?"
        return 90




    #####
    ##### MAIN APP STARTS HERE
    #####
mater = Pigo()

while True:
    if mater.checkDist():
        mater.safeDrive()
    else:
        mater.servoSweep()
        if mater.isThereOpening:
            mater.turnTo(mater.findAngle)
        else:
            mater.turnAround()