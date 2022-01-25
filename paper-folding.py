import sys

PAPER_HEIGHT = 0.00015 # in meter, 0.15mm
DECIMAL_PLACES = 2

MM = 0.001
CM = 0.01
METER = 1
KILOMETER = 1000 # m
EARTH_DIAMETER = 12742 # km
DISTANCE_TO_MOON = 384400 # km
LIGHTYEAR = 1.057 * (10**18) # km
MILKY_WAY_DIAMETER = 105700 # lightyears

def unit_conversion(height, factor):
    value = round((height / factor), DECIMAL_PLACES)
    if(value > 1000000):
        return "> 1 000 000"
    else:
        return str(value)

print()
print("Paper thickness: " + unit_conversion(PAPER_HEIGHT, MM) + "mm")
try:
    totalFoldings = int(input("Number of Foldings: "))
except ValueError:
    print("Please enter an integer!")
    sys.exit()
if totalFoldings < 0:
    print("Please enter a non negative number!")
    sys.exit()

height = PAPER_HEIGHT * (2 ** float(totalFoldings)) # in meter

print()
print(f' {"Height": <11}  Unit')
print(' ----------------------')
print(f' {unit_conversion(height, MM): <13}' + "mm")
print(f' {unit_conversion(height, CM): <13}' + "cm")
print(f' {unit_conversion(height, METER): <13}' + "m")
print(f' {unit_conversion(height, KILOMETER): <13}' + "km")
print(f' {unit_conversion(height, KILOMETER * EARTH_DIAMETER): <13}' + "Earth Diameters")
print(f' {unit_conversion(height, KILOMETER * DISTANCE_TO_MOON): <13}' + "Distance to Moon")
print(f' {unit_conversion(height, LIGHTYEAR): <13}' + "Lightyears")
print(f' {unit_conversion(height, LIGHTYEAR * MILKY_WAY_DIAMETER): <13}' + "Milky Way Diameters (105700 lightyears)")
print()
