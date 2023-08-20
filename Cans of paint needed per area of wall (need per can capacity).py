import math

def paint_calc(height, width, cover):
  cans_needed = (height * width) / cover
  print(f"You'll need {math.ceil(cans_needed)} cans of paint.")


# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5 #square meters of wall
# paint_calc(height=test_h, width=test_w, cover=coverage)

h_ = int(input("Enter your height. "))
w_ = int(input("Enter your width. "))
c_ = int(input("Enter coverage per can. "))

paint_calc(h_, w_, c_)