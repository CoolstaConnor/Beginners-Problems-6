def triangletest(side1, side2, side3):
    if sum > side3:
        print(f"It is",True,"that this is a triangle")
    else:
        print(f"It is",False,"that this is a triangle")
    
side1 = int(input("Enter an angle for a side of a triangle: "))
side2 = int(input("Enter another angle for a side of a triangle: "))
side3 = int(input("Enter another angle for a side of a triangle: "))
sum = side1 + side2
triangletest(side1, side2, side3)