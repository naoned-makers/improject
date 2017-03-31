#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
#pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

# HITEC HS-5645MG
CHANNEL_LEFT_ARM = 0
SERVO_MIN_LEFT_ARM = 1000  # Min pulse length out of 4096 POSITION BASSE
SERVO_MIDDLE_LEFT_ARM = 1500  # Middle pulse length out of 4096
SERVO_MAX_LEFT_ARM = 2900  # Max pulse length out of 4096 POSITION HAUTE

# TOWER PRO MG 90
CHANNEL_LEFT_HAND = 1
SERVO_MIN_LEFT_HAND = 150  # Min pulse length out of 4096 POSITION BASSE
SERVO_MIDDLE_LEFT_HAND = 370  # Middle pulse length out of 4096
SERVO_MAX_LEFT_HAND = 590  # Max pulse length out of 4096 POSITION HAUTE


#pwm.setPWMFreq(60)                        # Set frequency to 60 Hz pour TOWER PRO MG 90
pwm.setPWMFreq(300)                        # Set frequency to 300 Hz pour le HITEC HG-5645MG

def upAndDownLeftArm(sleep = 2):
  #pwm.setPWMFreq(300) 
  pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MIN_LEFT_ARM)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MAX_LEFT_ARM)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_LEFT_ARM, 0, SERVO_MIDDLE_LEFT_ARM)
  time.sleep(sleep)

def leftAndRightLeftHand(sleep = 2):
  #pwm.setPWMFreq(60) 
  pwm.setPWM(CHANNEL_LEFT_HAND, 0, SERVO_MIN_LEFT_HAND)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_LEFT_HAND, 0, SERVO_MAX_LEFT_HAND)
  time.sleep(sleep)
  pwm.setPWM(CHANNEL_LEFT_HAND, 0, SERVO_MIDDLE_LEFT_HAND)
  time.sleep(sleep)

#leftAndRightLeftHand()
#time.sleep(sleep)
upAndDownLeftArm()

#for num in range(servoMin, servoMax):
#  pulselen = ((num * (servoMax - servoMin)) / 180) + servoMin
#  pwm.setPWM(0, 0, pulselen)

#while (True):
  # Change speed of continuous servo on channel O
  #upAndDownLeftArm()
  #time.sleep(4)
  #leftAndRightLeftHand()
  #pwm.setPWM(1, 0, servoMin)
  #time.sleep(2)
  #pwm.setPWM(1, 0, servoMax)
  #time.sleep(2)
  #pwm.setPWM(1, 0, servoMiddle)
  #time.sleep(2)



