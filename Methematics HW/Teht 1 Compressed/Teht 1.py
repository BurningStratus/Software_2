import numpy as np


### Teht 1 - 1
# a
print("1 - 1")

rad = 2.493
print(f"a: {np.rad2deg(rad):.1f}")
# b

rad = 0.911

print(f"b: {np.rad2deg(rad):.1f}\n")
### Teht 1 - 2
# a
print("1 - 2")

deg = 137.7

print(f"a: {np.deg2rad(deg):.1f}")
# b

deg = 62.3

print(f"b: {np.deg2rad(34.567):.1f}\n")
### Teht 1 - 3
print("1 - 3")

degree_list = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
rad_dict = {}

for degrees in degree_list:
    adder = float(f"{np.deg2rad(degrees):0.1f}")
    rad_dict[degrees] = adder

for records in rad_dict:
    print(f"Asteet: {records} Radiaanit: {rad_dict[records]}")

print(f"Hypoteuusan pituus on: {np.hypot(1.6, 2.3):.2f}")
