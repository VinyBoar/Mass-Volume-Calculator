#Project 1


print("Welcome to Kyle's Mass Calculator".center(50,'-'), # Here I looked up how to format the line to make the program look better.
      "\nAble to calculate the following 3D figures\n",   # Using \n to create new lines to form a list 
      "\n2.     Rectagnular Prism\n",                     # I formated the code so that each option was on its own line, yet there was only one print statment.
      "\n3.     Cylinder\n", 
      "\n4.     Sphere\n",
      "\n5.     Cube\n",
      "\n6.     Triangular Prism"    )



pi = 3.141592653589793 #Using pi as a variable to calculate formaulas later on

figure = input("Please input desired figured as written ") #Assigning variable figure to the inpu that the user has entered. Stated as written to eliminate bugs.

print('Please select the material of the figure', # Once again used a singular print statement for all of the options
      '\n1.     Ash, black\n',                    # used \n again to make new lines for each of the options
      '\n2.     Ash, European\n'
      '\n3.     Aspen\n',
      '\n4.     Balsa\n'
               )

material = input("Please input the type of wood as written ") # Assigning material to the input the user selects, again used as written to eliminate bugs

if figure == ('Rectangular Prism') or figure == ('Rectangular prism') or figure == ('rectangular prism') or figure ==  ("1"): # Using an if statement to determine the figure being calculated, used or statements to allow different variations of text.

    height = float(input("Please input the Rectangular Prism's height in feet ")) # All the values needed to calculate the volume are written as float input statements allowing for decimals.
    width = float(input("Please input the Rectangular Prism's width in feet "))   # Using meters as the unit of length 
    length = float(input("Please input the Rectangular Prism's length in feet "))

    figure_volume = height * width * length # Calculating the rectangular prisms volume and stores under figure_volume

elif figure == ('Cylinder') or figure == ('cylinder') or figure == ('2'): # Used elif statements to make the program more compact

    radius = float(input("Please input the radius of the Cylinder in feet ")) 
    height = float(input("Please input the height of the Cylinder in feet "))

    figure_volume = pi * (radius * radius) * height # Calculating the cylinder's volume using the variable pi and storing as figure_volume

elif figure == ('Sphere') or figure == ('sphere')or figure == ('3'): 

    radius = float(input("Please input the radius of the Sphere in inches "))

    figure_volume = (4/3) * pi * (radius ** 3) # Calculating the spheres volume using the pi variable and storing as figure_volume

elif figure == ('Cube') or figure == ('cube') or figure == ('4'): 

    length = float(input("Plese input one of the side lengths of the Cube in feet "))

    figure_volume = (length ** 3) # Calculating the cube's volume and storing it under the variable figure_volume

elif figure == ('Triangular Prism') or figure == ('Triangular prism') or ('triangular prism') or figure == ('5'):

    base = float(input("Please input the base of the Triangular Prism in feet "))
    height = float(input("Please input the height of the Triangular Prism in feet "))
    length = float(input("Please input the length of the Triangular Prism in feet "))

    figure_volume = (1/2) * base * height * length # Calculating the triangular prism's volume and storing it under the variable figure_volume

else:
    print('Please pick a shape listed') # This will print if the user does not pick a shape that is listed. 

if material == ('Ash, black') or material == ('ash, black') or material == ('1'): # Using variable material to determine which denisty to use 
    density = 33
    material == ('Ash, black')

elif material == ('Ash, White') or material == ('ash, White') or material == ('Ash, white') or material == ('ash, white') or material == ('2'): # Used many or operators to make sure that there would not be an error
    density = 46.5 # Simply assigning the variable denisty to the density of the material listed
    material == ('Ash, European')
elif material == ('Aspen') or material == ('aspen') or material == ('3'):
    density = 26
    material == ('Aspen')
elif material == ('Balsa') or material == ('balsa') or material == ('4'):
    density = 8
    material == ('Balsa')
else:
    print('Please pick a material listed')
mass = (density * figure_volume) # Set the mass to get stored as a variable
print(figure_volume, 'ft³') # Printing each of the products
print("The density of", material, "is" ,density, "lb/ft³")
print(mass, "lb")
    
    
