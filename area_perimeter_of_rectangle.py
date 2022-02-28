#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: February 2022
# This program calculates the area and perimeter of a rectangle
#    with integers inputted by user 

import math


def main():
    # this function calculates the area and perimeter

    # input
    Length = int(input("Enter length of the rectangle (mm): "))
    Width = int(input("Enter width of the rectangle (mm): "))
    
    
    # process
    
    area = Length * Width
    perimeter = 2 * (Length + Width)
    
    # output 
    print("")
    print("Area is {0} mm².".format(area))
    print("Perimeter is {0} mm.".format(perimeter))
    print("")
    print("Done")
    
if __name__ == "__main__":
    main()
