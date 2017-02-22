""" Converts Gallons to Liters"""
gallons_user_input = 4
#gallons_user_input
#gal
#drawline(color, origin, angle, equation, intensity, fade, owner)
gallons_in = input("How many gallons do you want to convert?")
rounded_liters = round(float(gallons_in) / .264172, 3)
print (gallons_in + " gallons is " + str( rounded_liters  ) + " liters." )
#print ('%s gallons is %f liters.' % (Gallons_In, rounded_liters))
