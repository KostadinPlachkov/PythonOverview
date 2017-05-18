"""
0.80
1.23
0.78
0.50
"""
import math

try:

    area_of_paper = float(input())
    height = float(input())
    width = float(input())
    depth = float(input())
    paper_loss = 1 + 9.8 / 100

    area_of_paper_for_box = 2 * (height * width) + 2 * (height * depth) + 2 * (width * depth)
    area_with_losses = area_of_paper_for_box * paper_loss
    # print(area_of_paper_for_box)
    number_of_papers = area_with_losses / area_of_paper
    print("{}".format(math.ceil(number_of_papers)))

except:
    print("INVALID INPUT")