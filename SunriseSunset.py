## this is the routine for finding sunrise and sunset
## on a given day. 
## It's program 49 on p. 95

import datetime
import math

## Get today's date and current time
## store it as a global variable for later use
now = datetime.datetime.today()

yearbeg = datetime.datetime(now.year, 1, 1, 0, 0, 0, 0)

## designate the epoch, 1990.0
epoch = datetime.datetime(1990, 1, 1, 0, 0, 0, 0)

## table 6 info from p. 87
epsg = 279.403303
omegag = 282.768422
eccen = 0.016713
rsub0 = 149598500 ## km
thetasub0 = 0.533128

epochdiff = now - epoch
yeardiff = now - yearbeg

epochdiff.days
yeardiff.days

bookN = yeardiff.days * 360 / 365.242191
bookN = bookN % 360

## calculate degree amount, and put in 0-360
Msubsun = bookN + epsg - omegag
Msubsun = Msubsun % 360

## convert to radians
Msubsun = math.radians(Msubsun)

## find solution to Kepler's equation
## E - eccen * sin E = M
## Routine R2 p. 90
E = Msubsun ## starting value
while True:
    bookdelta = E - eccen * math.sin(E) - Msubsun
    if bookdelta < 0.000001:
        break
    deltaE = bookdelta / (1 - eccen * math.cos(E))
    E = E - deltaE

## find v -- in degrees
v = math.degrees(2 * 
                math.atan( ((1 + eccen)/(1 - eccen))**(0.5) * 
                            math.tan(E/2)) )

lambdasun = (v + omegag) % 360 ## in degrees
betasun = math.radians(0) ## given
lambdasun = math.radians(lambdasun)

## convert lambdasun to RA and decl.
## routine 27, p. 40
epsilon = math.radians(23.441884) ## given for 1990.0 epoch

bookdelta = math.asin(math.sin(betasun)*math.cos(epsilon) + 
                      math.cos(betasun)*math.sin(epsilon)*math.sin(lambdasun))
y = math.sin(lambdasun) * math.cos(epsilon) - math.tan(betasun) * math.sin(epsilon)
x = math.cos(lambdasun)

alphaprime = math.atan(y / x)
alphaprime = math.degrees(alphaprime)

## remove ambiguity of inverse tangent, on -90 to 270 in radians
def trueAtan(x, y):
    if x > 0:
        return math.atan(y / x)
    else:
        return math.atan(y / x) + math.pi / 2

alphaprime = trueAtan(x, y)
alphaprime = math.degrees(alphaprime)
if alphaprime < 0:
    alphaprime = alphaprime + 360

alphahours = alphaprime / 15

## need lambdasun, bookdelta, and alphahours
## now, add 0.985647 to lambdasun to find position 24 hours later
## also update bookdelta and alphahours


lambdasun2 = math.radians(math.degrees(lambdasun) + 0.985647)

bookdelta2 = math.asin(math.sin(betasun)*math.cos(epsilon) + 
                      math.cos(betasun)*math.sin(epsilon)*math.sin(lambdasun2))

y = math.sin(lambdasun2) * math.cos(epsilon) - math.tan(betasun) * math.sin(epsilon)
x = math.cos(lambdasun2)

alphaprime = trueAtan(x, y)
alphaprime = math.degrees(alphaprime)
if alphaprime < 0:
    alphaprime = alphaprime + 360

alphahours2 = alphaprime / 15

## lambda, delta, and alpha all in radians

## step one and two of program done -- do all time conversions next
