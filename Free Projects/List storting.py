
import math

def vector(deg, len):
    x = len * (math.sin(deg))
    y = len * (math.cos(deg))
    return x, y

def coord(sinus, cosine):
    len = math.sqrt(sinus ** 2 + cosine ** 2)
    x = str(len) + "(" + str(sinus/len) + "+" + "i" + str(cosine/len) + ")"
    return x


print(vector(0.278, 71.3))
print(vector(185, 117.1))
print(vector(6.52, 13.2))

print(coord(0.65, -0.85))
print(coord(-1.27, 3.04))
print(coord(8.52, -11.31))
print(coord(-93, -137))

tested