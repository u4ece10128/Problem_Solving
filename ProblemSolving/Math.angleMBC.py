import math

side_AB = float(input())
side_BC = float(input())

# calculate length of hypo
side_AC = math.sqrt((side_AB*side_AB) + (side_BC*side_BC))
side_MC = side_AC / 2

# print(side_MC, side_BC)

theta = math.degrees(math.acos(side_MC/side_BC))

print(str(round(180 - 90 - theta)) + '°')

