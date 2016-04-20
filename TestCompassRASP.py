import sys

sys.path.append('/home/pi/Navigation/Compass/quick2wire-python-api')
from i2clibraries import i2c_hmc5883l
from time import sleep

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)
hmc5883l.setContinuousMode()
hmc5883l.setDeclination(7,52)

while True:
    (degress, minutes) = hmc5883l.getHeading()
    heading = hmc5883l.getHeadingString()
    degrees = heading.split("°")
    print(degrees[0])
    sleep(0.1)
