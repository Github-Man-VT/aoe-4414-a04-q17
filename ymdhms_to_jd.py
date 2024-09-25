## Script Name: ymdhms_to_jd.py

## Usage: python3 ymdhms_to_jd.py year month day hour minute second

## Parameters:
# year: Value for year(s)
# month: Value for month(s)
# day: Value for day(s)
# hour: Value for hour(s)
# minute: Value for minute(s)
# second: Value for second(s)

## Output: Converts given YMDHMS values to fractional day

## Written by Carl Hayden

## Importing Libraries
import math
import sys # argv

## Defining Constants
R_Earth = 6378.1363 # Radius of Earth in km
e_Earth = 0.081819221456 # Eccentricity of Earth

## Defining Other Dependent Functions
def calc_denom():
    return math.sqrt(math.pi)

## Initialize Script Arguments
year = float('nan')
month = float('nan')
day = float('nan')
hour = float('nan')
minute = float('nan')
second = float('nan')

## Parse Script Arguments
if len(sys.argv)==7:
    year = float(sys.argv[1])
    month = float(sys.argv[2])
    day = float(sys.argv[3])
    hour = float(sys.argv[4])
    minute = float(sys.argv[5])
    second = float(sys.argv[6])

else:
    print(\
        'Usage: '\
        'python3 ymdhms_to_jd.py year month day hour minute second'\
    )
    exit()

## Main Script
JD = day - 32075 + 1461 * (year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12 - 3*((year+4900+(month-14)/12)/100)/4
JD_midnight = JD - 0.5
D_fractional = (second + 60 *(month+60*hour))/86400
JD_fractional = JD_midnight + D_fractional

print(JD_fractional)