from math import *

WallHeight = int(input("How much is wall height: "))
WallWidth = int(input("How much is wall width: "))
CanCoverage = 5

def calculate(Height, Width, Coverage):
    result = ceil((Height * Width) / Coverage)
    print(f"You Need {result} cans of paint")

calculate(WallHeight, WallWidth, CanCoverage)