import sys

PAPER_HEIGHT_DEFAULT = 0.15 # in mm, 0.15mm
DECIMAL_PLACES = 2

MM = 0.001
CM = 0.01
METER = 1
WHITE_HOUSE_HEIGHT = 21 # m
EIFFEL_TOWER_HEIGHT = 300 # m
KILOMETER = 1000 # m
MOUNT_EVEREST_HEIGHT = 8848 # m
MARIANA_TRENCH = 10984 # m
EARTH_DIAMETER = 12742 # km
DISTANCE_TO_MOON = 384400 # km
DISTANCE_TO_SUN = 150000000 # km
LIGHTYEAR = 1.057 * (10**18) # km
MILKY_WAY_DIAMETER = 105700 # lightyears

def unit_conversion(height, factor):
    value = round((height / factor), DECIMAL_PLACES)
    if(value > 10000000):
        return "> 10 000 000"
    else:
        return str(value)

paperHeight = PAPER_HEIGHT_DEFAULT

if len(sys.argv) == 3:
	try:
		totalFoldings = int(sys.argv[1])
		paperHeight = float(sys.argv[2])
	except ValueError:
		print("Please enter a valid integer for total number of foldings and a valid float for the paper height!")
		sys.exit()
	if totalFoldings < 0 or paperHeight < 0:
		print("Please enter a non negative number!")
		sys.exit()
elif len(sys.argv) == 2:
	try:
		totalFoldings = int(sys.argv[1])
	except ValueError:
		print("Please enter a valid integer for total number of foldings!")
		sys.exit()
	if totalFoldings < 0:
		print("Please enter a non negative number!")
		sys.exit()
elif len(sys.argv) == 1:
	print("Usage: " + sys.argv[0] + " <number_of_foldings> optional: <paper_height_in_mm>")
	sys.exit()

print()

print("Paper thickness: " + str(paperHeight) + "mm")
print("Number of foldings: " + str(totalFoldings))

height = (paperHeight / 1000.0) * (2 ** float(totalFoldings)) # in meter

print()
print(f' {"Height": <11}  Unit')
print(' ----------------------')
print(f' {unit_conversion(height, MM): <13}' + "mm")
print(f' {unit_conversion(height, CM): <13}' + "cm")
print(f' {unit_conversion(height, METER): <13}' + "m")
print(f' {unit_conversion(height, METER * WHITE_HOUSE_HEIGHT): <13}' + "White houses")
print(f' {unit_conversion(height, METER * EIFFEL_TOWER_HEIGHT): <13}' + "Eiffel towers")
print(f' {unit_conversion(height, KILOMETER): <13}' + "km")
print(f' {unit_conversion(height, METER * MOUNT_EVEREST_HEIGHT): <13}' + "Mount Everests")
print(f' {unit_conversion(height, METER * MARIANA_TRENCH): <13}' + "Mariana trenches")
print(f' {unit_conversion(height, KILOMETER * EARTH_DIAMETER): <13}' + "Earth Diameters")
print(f' {unit_conversion(height, KILOMETER * DISTANCE_TO_MOON): <13}' + "Distances to moon")
print(f' {unit_conversion(height, KILOMETER * DISTANCE_TO_SUN): <13}' + "Distances to sun")
print(f' {unit_conversion(height, LIGHTYEAR): <13}' + "Lightyears")
print(f' {unit_conversion(height, LIGHTYEAR * MILKY_WAY_DIAMETER): <13}' + "Milky Way Diameters (105700 lightyears)")
print()
