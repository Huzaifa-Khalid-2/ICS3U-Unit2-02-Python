#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: February 2022
# This program calculates the area and perimeter of a rectangle
#    with integers inputted by user 



def main():
    # this function calculates the area and perimeter

    # input
    Length = int(input("Enter length of the rectangle (mm): "))
    Width = int(input("Enter width of the rectangle (mm): "))
    
    # process
    area = Length * Width
    perimeter = 2 * (Length + Width)
    print("If the circle has a radius of 15 mm: ")
    print("")
    print("Area is {} mm².".format(math.pi * 15**2))
    print("Perimeter is {} mm.".format(2 * math.pi * 15))


if __name__ == "__main__":
    main()
