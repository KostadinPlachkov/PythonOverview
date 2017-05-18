import math
try:
    sray_for_m2 = 1.76
    w = float(input())
    h = float(input())
    area = w * h
    num_sprays = area / sray_for_m2
    print(math.ceil(num_sprays))


except:
    print("INVALID INPUT")
