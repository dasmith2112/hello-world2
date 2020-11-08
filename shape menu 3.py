#numbercheck tests to see if a string is an integer within an acceptable range
# it takes three arguments
# the input to be checked (string)
# the lower acceptable bound
# the upper acceptable bound

# the function returns a tuple.  The first element is boolean and indicates
# whether the input passed.  The second element is a message to the user
# indicating success or why their input failed

def numbercheck(text,lower,higher):
    answer_valid = text.isdigit() #True if integer entered
    if answer_valid == True: #check to see that number entered is integer
        number=int(text)#as we know text is number turn into integer
        if (number>=lower and number<=higher):
            message="Thank you!"
        elif number<lower: #to get here the number must be out of range
            message="This number is too low"
            answer_valid=False
        else:
            message="This number is too high"
            answer_valid=False
    else: #to get here a non-integer has been entered
        message="This is not an integer!"

    return answer_valid, message


# square takes one argument and draws a square with that width
def square(number):
    number=int(number)
    row=1   #counter to keep track of which row we are currently drawing
    string = "*" * number #create string of suitable length
    while (row<=number): #loop until all rows are completed
        print(string)
        row=row+1 #increase row count


# rectangle takes two arguments and draws a rectangle with that width and height
def rectangle(width, height):
    xwidth=int(width)
    yheight = int(height)
    string = "*"*xwidth #create string of suitable length
    row=1 #counter to keep track of which column we are currently drawing in
    while (row<=yheight): #loop until all rows are completed
        print(string) #we have reached the end of the row so move to next row
        row=row+1 #increase row count


# tl_triangle takes one argument and draws a right angled triangle with the right angle
# in the top left corner and with an opposite and adjacent of length number
def tl_triangle(number):
    stars = int(number) #the top line of the triangle is all stars
    while (stars!=0): #loop until there are no stars in the row
        print("*"*stars) #the current row has this many stars
        stars=stars-1 #the number of stars each row reduces by 1


# bl_triangle takes one argument and draws a right angled triangle with the right angle
# in the bottom left corner and with an opposite and adjacent of length number
def bl_triangle(number):
    number=int(number)
    stars = 1 #the number of stars in the first row
    while (stars<=number): #loop until we reach the final row which contains
                        #as many stars as the number entered
        print("*"*stars) #the current row has this many stars
        stars=stars+1 #move to next row which has one more star than the last row


# tr_triangle takes one argument and draws a right angled triangle with the right angle
# in the top right corner and with an opposite and adjacent of length number
def tr_triangle(number):
    number=int(number)
    stars = number #the first row contains only stars
    while (stars!=0): #loop until row which would contain no stars
        print(" "*(number-stars)+"*"*stars)#fill the string with sufficient spaces
                                            #before adding stars
        stars=stars-1 #each row contains one fewer star


# br_triangle takes one argument and draws a right angled triangle with the right angle
# in the bottom right corner and with an opposite and adjacent of length number
def br_triangle(number):
    number=int(number)
    stars = 1 #first row contains only one star
    while (stars<=number): #keep looping until we reach the final row which is all stars
        print(" "*(number-stars)+"*"*stars) #add sufficient spaces before adding stars
        stars=stars+1 #the next row contains one more star than the previous


#diamond takes one argument and draws a diamond of that height and width
def diamond(number):
    number=int(number)
    stars=-1
    while (stars!=number): #stop when reach middle row and all stars
        stars=stars+2
        spaces=int((number-stars)/2)
        string=" "*spaces+"*"*stars+" "*spaces
        print(string)


    #bottom part of diamond where the number of diamons each row decreases by 2
    stars=number
    while (stars!=1): #stop when reach back to one star
        stars=stars-2
        spaces=int((number-stars)/2)
        string=" "*spaces+"*"*stars+" "*spaces
        print(string)



        
#menu program

selection="1" # need to set a value for selection to enter while loop

while(selection!="X"):
    print("1 - Square")
    print("2 - Rectangle")
    print("3 - Triangle with right angle in top left")
    print("4 - Triangle with right angle in bottom left")
    print("5 - Triangle with right angle in top right")
    print("6 - Triangle with right angle in bottom right")
    print("7 - Diamond")
    print("X - Exit")
          
    selection = input("Please choose option 1 to 7 or enter X to exit: ")
    if selection =="X": #check to see if user wants to exit
        print("Goodbye!!!")
    else:
        checkselection = numbercheck(selection,1,7)
        if checkselection[0] == True:
            selection = int(selection)
            
            if selection==1:
                min_width=1     #minimum width allowed.  This means that prompt
                                #and check stay constant
                max_width=20    #maximum width allowed
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the square (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        square(width)
            
            elif selection == 2:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):  #check width before asking
                                                #for height
                    width = input("Please enter the width of the rectangle (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                
                min_height=1
                max_height=20
                height_check=(False,"")
                while (height_check[0]==False):
                    height = input("Please enter the height of the rectangle (between " +
                                  str(min_height) + " and "+str(max_height)+") : ")
                    print("")
                    height_check=numbercheck(height,min_height,max_height)
                    if height_check[0]==False:
                        print(height_check[1])
                        print("")
                    
                rectangle(width, height)
                
            elif selection == 3:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the triangle (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        tl_triangle(width)
                
                
                
            elif selection == 4:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the triangle (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        bl_triangle(width)

            elif selection == 5:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the triangle (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        tr_triangle(width)

            elif selection == 6:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the triangle (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        br_triangle(width)

            elif selection == 7:
                min_width=1
                max_width=20
                width_check=(False,"")
                while (width_check[0]==False):
                    width = input("Please enter the width of the diamond (between " +
                                  str(min_width) + " and "+str(max_width)+") : ")
                    print("")
                    width_check=numbercheck(width,min_width,max_width)
                    if width_check[0]==False:
                        print(width_check[1])
                    else:
                        diamond(width)

                
        else:
            print(checkselection[1])

    print("")

 

