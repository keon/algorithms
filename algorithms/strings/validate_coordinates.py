""""
Create a function that will validate if given parameters are valid geographical coordinates.
Valid coordinates look like the following: "23.32353342, -32.543534534". The return value should be either true or false.
Latitude (which is first float) can be between 0 and 90, positive or negative. Longitude (which is second float) can be between 0 and 180, positive or negative.
Coordinates can only contain digits, or one of the following symbols (including space after comma) -, .
There should be no space between the minus "-" sign and the digit after it.

Here are some valid coordinates:
-23, 25
43.91343345, 143
4, -3

And some invalid ones:
23.234, - 23.4234
N23.43345, E32.6457
6.325624, 43.34345.345
0, 1,2

"""
# I'll be adding my attempt as well as my friend's solution (took us ~ 1 hour)

# my attempt
import re
def is_valid_coordinates_0(coordinates):
    for char in coordinates:
        if not (char.isdigit() or char in ['-', '.', ',', ' ']):
            return False
    l = coordinates.split(", ")
    if len(l) != 2:
        return False
    try:
        latitude = float(l[0])
        longitude = float(l[1])
    except:
        return False
    return -90 <= latitude <= 90 and -180 <= longitude <= 180

# friends solutions
def is_valid_coordinates_1(coordinates):
    try:
        lat, lng = [abs(float(c)) for c in coordinates.split(',') if 'e' not in c]
    except ValueError:
        return False

    return lat <= 90 and lng <= 180

# using regular expression
def is_valid_coordinates_regular_expression(coordinates):
    return bool(re.match("-?(\d|[1-8]\d|90)\.?\d*, -?(\d|[1-9]\d|1[0-7]\d|180)\.?\d*$", coordinates))  
