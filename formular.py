import math

"""
v= velocity
t = angle
m = mass
L = length
G = gravity
"""

def FirstAcceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = -G * (2 * m1 + m2) * math.sin(t1)
    numerator2 = -m2 * G * math.sin(t1 - 2 * t2)
    numerator3 = -2 * math.sin(t1-t2)
    numerator4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * math.cos(t1-t2))
    numerator = numerator1 + numerator2 + (numerator3 * numerator4)
    denominator = L1 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return float(numerator/denominator)

def SecondAcceleration(t1, t2, m1, m2, L1, L2, G, v1, v2):
    numerator1 = 2 * math.sin(t1 - t2)
    numerator2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1+ m2) * math.cos(t1)
    numerator3 = (v2 * v2) * L2 * m2 * math.cos(t1-t2)

    numerator = numerator1 * (numerator2 + numerator3)
    denominator = L2 * (2 * m1 + m2 - m2 * math.cos(2 * t1 - 2 * t2))

    return float(numerator/denominator)
