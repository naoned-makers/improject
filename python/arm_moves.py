#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
#pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
pwm = PWM(0x40, debug=True)

#servoMin = 150  # Min pulse length out of 4096
#servoMax = 600  # Max pulse length out of 4096

#servoMin = 900  # Min pulse length out of 4096
#servoMax = 2200  # Max pulse length out of 4096

servoMin = 1000  # Min pulse length out of 4096 POSITION BASSE
servoMiddle = 1500  # Middle pulse length out of 4096
servoMax = 2900  # Max pulse length out of 4096 POSITION HAUTE


def setServoPulse(channel, pulse):
  print "coucouc"
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 120                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  print pulse
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(300)                        # Set frequency to 60 Hz

for letter in 'Python':
  print 'Current letter :', letter

#pulselen = ((50 * (servoMax - servoMin)) / 180) + servoMin
#pwm.setPWM(0, 0, pulselen)

#for num in range(servoMin, servoMax):
#  pulselen = ((num * (servoMax - servoMin)) / 180) + servoMin
#  pwm.setPWM(0, 0, pulselen)

pulselen = ((120 * (servoMax - servoMin)) / 120) + servoMin
print 'angle 120 divise 120', pulselen
pulselen = ((120 * (servoMax - servoMin)) / 180) + servoMin
print 'angle 120 divise 180', pulselen

pulselen = ((0 * (servoMax - servoMin)) / 120) + servoMin
print 'angle 0 divise 120', pulselen
pulselen = ((0 * (servoMax - servoMin)) / 180) + servoMin
print 'angle 0 divise 180', pulselen


pulselen = ((110 * (servoMax - servoMin)) / 120) + servoMin
pwm.setPWM(0, 0, servoMin)
time.sleep(2)
pwm.setPWM(0, 0, servoMax)
time.sleep(2)
pwm.setPWM(0, 0, 1500)
#pulselen = ((0 * (servoMax - servoMin)) / 180) + servoMin
#pwm.setPWM(0, 0, pulselen)
#pwm.setPWM(0, 2000, 0)


#time.sleep(2)

#while (True):
  # Change speed of continuous servo on channel O
  #pulselen = ((100 * (servoMax - servoMin)) / 180) + servoMin
  #pwm.setPWM(0, 0, pulselen)
  #time.sleep(2)
  #pulselen = ((10 * (servoMax - servoMin)) / 180) + servoMin
  #pwm.setPWM(0, 0, pulselen)
  #time.sleep(2)



