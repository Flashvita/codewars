"""
Two fishing vessels are sailing the open ocean, both on a joint ops fishing mission.

On a high stakes, high reward expedition - the ships have adopted the strategy of hanging a net between the two ships.

The net is 40 miles long. Once the straight-line distance between the ships is greater than 40 miles, the net will tear, and their valuable sea harvest will be lost! We need to know how long it will take for this to happen.
Given the bearing of each ship, find the time in minutes at which the straight-line distance between the two ships reaches 40 miles. Both ships travel at 90 miles per hour. At time 0, assume the ships have the same location.

Bearings are defined as degrees from north, counting clockwise. These will be passed to your function as integers between 0 and 359 degrees. Round your result to 2 decimal places.

If the net never breaks, return float('inf')

Happy sailing!
"""

from math import radians, sin, cos, acos

def find_time_to_break(bearing_A, bearing_B):
    l = 40
    a = bearing_A
    b = bearing_B
    earth_radius_km = 6371.009
    a_y = radians(a.y)
    b_y = radians(b.y)
    delta_x = radians(a.x - b.x)
    cos_x = (sin(a_y) * sin(b_y) +
             cos(a_y) * cos(b_y) * cos(delta_x))
    distance = acos(cos_x) * earth_radius_km * 1.609
    return round(distance, 2) if distance > 40 else float('inf')
