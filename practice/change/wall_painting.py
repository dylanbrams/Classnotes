import math
SQUARE_FT_PER_GALLON = 375.5
total_gallons = 0
more_walls = True
while (more_walls == True):
    wall_height = int(input("Please enter the width of the wall in feet: "))
    wall_width = int(input("Please enter the height of the wall in feet: "))
    cost_per_gallon = int(input("Please enter the cost per gallon of paint: "))
    number_coats = int(input("Please enter the number of coats of paint: "))

    wall_area_painted = wall_height * wall_width * number_coats
    gallons_this_wall = wall_area_painted / SQUARE_FT_PER_GALLON
    total_gallons += gallons_this_wall
    print("This wall's area painted: " + str(wall_area_painted))
    print("This wall's gallons of paint: " + str(gallons_this_wall) + "  This wall's price: "
          + str(gallons_this_wall * cost_per_gallon))
    print ("Total gallons to purchase so far: " + str(total_gallons) + "  All walls' price: "
           + str(total_gallons * cost_per_gallon))
    continue_painting = input ("Would you like to calculate paint for more walls?")
    if continue_painting != "Yes":
        more_walls = False

    total_gallons = math.ceil(total_gallons)
    print ("Final total gallons: " + str(total_gallons) + " Final total price: " + str(total_gallons * cost_per_gallon))