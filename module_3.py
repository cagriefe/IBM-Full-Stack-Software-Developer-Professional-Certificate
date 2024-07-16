###Conditions and Branching

##Condition Statements

# Condition Equal
a = 5
a == 6

# Greater than Sign
i = 6
i > 5

# Greater than Sign
i = 2
i > 5

# Inequality Sign
i = 2
i != 6

# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson"

# Compare characters
'B' > 'A'   #ASCII

# Compare characters
'BA' > 'AB'
#Note: Upper Case Letters have different ASCII code than Lower Case Letters, which means the comparison between the letters in Python is case-sensitive.


##Branching


# If statement example
age = 19
#age = 18

#expression that can be true or false
if age > 18:
    
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )

#The statements after the if statement will run regardless if the condition is true or false 
print("move on")


# Else statement example
age = 18
# age = 19

if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
    
print("move on")


# Elif statment example
age = 18

if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )
    
print("move on")


# Condition statement example
album_year = 1983
album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
    
print('do something..')


# Condition statement example
album_year = 1983
#album_year = 1970

if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")

print('do something..')


##Logic Operations

# Condition statement example AND (&) (FFF)
album_year = 1980

if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")
    
print("")
print("Do Stuff..")


# Condition statement example OR (TTT)
album_year = 1990

if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")


# Condition statement example NOT 
album_year = 1983

if not (album_year == 1984):
    print ("Album year is not 1984")

    
#---------------------------------------------------------------------#


###Loops

# Use the range
range(3)


# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     
    
# Exmaple of for loop, loop through list
for year in dates:  
    print(year)

    
# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])
    

# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)
  
    
##While loop

count = 1
while count <= 5:
    print(count)
    count += 1
    
    
# While Loop Example
dates = [1982, 1980, 1973, 2000]

i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    

print("It took ", i ,"repetitions to get out of loop.")


###Functions

# First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return (b)

# Get a help on add function
# help(add)

# Call the function add()
add(1)



# Define a function for multiple two numbers
def Mult(a, b):
    c = a * b
    return(c)
    print('This is not printed')
    
result = Mult(12,2)
print(result)

# Use mult() multiply two integers
Mult(2, 3)

# Use mult() multiply two floats
Mult(10.0, 3.14)

# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")



##Variables

# Function Definition
def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)


# Initializes Global variable  
x = 3
# Makes function call and return function a y
y = square(x)
y

# Directly enter a number as parameter
square(2)



# Define functions, one with return value None and other without return value
def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output
MJ()
MJ1()

# See what functions returns are
print(MJ())
print(MJ1())



# Define the function for combining strings
def con(a, b):
    return(a + b)

# Test on the con() function
con("This ", "is")



##Pre-defined functions

# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)

# Use sum() to add every element in a list or tuple together
sum(album_ratings)

# Show the length of the list or tuple
len(album_ratings)


##In-Built functions

#You will see below will return an error as integer alone is not considered while using a function.It either has to be in the form of tuple, list or a set.
sum(1,2)


# Define a tuple or list
a = (1, 2)
# Pass the tuple to the sum function and store the result in a variable
c = sum(a)
# Print the result
print(f"The sum of the elements in the tuple {a} is {c}.")




# Function example

def type_of_album(artist, album, year_released):
    
    print(artist, album, year_released)
    if year_released > 1980:
        return "Modern"
    else:
        return "Oldie"
    
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)


# Print the list using for loop
def PrintList(the_list):
    for element in the_list:
        print(element)
        
# Implement the printlist function
PrintList(['1', 1, 'the man', "abc"])




#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"

# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'

check_string("Michael Jackson is the best")





#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return 1
    
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"

# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)

#Use if else statement to compare the string
if check==1:
    print("\nString Matched")
else:
    print("\nString not Matched")
    





# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")




# Example for setting param with default value
def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

# Test the value with default value and with input

isGoodRating()
isGoodRating(10)



##Global Variables

# Example of global variable

artist = "Michael Jackson"
def printer1(artist):
    internal_var1 = artist
    print(artist, "is an artist")
    
printer1(artist)
# try runningthe following code
#printer1(internal_var1)  #Name Error: name 'internal_var' is not defined. Why? It's because all the variables we create in the function is a local variable, meaning that the variable assignment does not persist outside the function.



artist = "Michael Jackson"

def printer(artist):
    global internal_var 
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)





# Example of global variable
myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:", getBandRating("AC/DC"))
print("Deep Purple's rating is:",getBandRating("Deep Purple"))
print("My favourite band is:", myFavouriteBand)




# Deleting the variable "myFavouriteBand" from the previous example to demonstrate an example of a local variable 

del myFavouriteBand

# Example of local variable

def getBandRating(bandname):
    myFavouriteBand = "AC/DC"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is: ", getBandRating("AC/DC"))
print("Deep Purple's rating is: ", getBandRating("Deep Purple"))
print("My favourite band is", myFavouriteBand)



# Example of global variable and local variable with the same name

myFavouriteBand = "AC/DC"

def getBandRating(bandname):
    myFavouriteBand = "Deep Purple"
    if bandname == myFavouriteBand:
        return 10.0
    else:
        return 0.0

print("AC/DC's rating is:",getBandRating("AC/DC"))
print("Deep Purple's rating is: ",getBandRating("Deep Purple"))
print("My favourite band is:",myFavouriteBand)



##Collections and Functions


# All the arguments are 'packed' into args which can be treated like a tuple
def printAll(*args):
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')



# All the arguments are 'packed' into args which can be treated like a dictionary
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')




def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]

addItems(myList)

myList
    
    
    
    
# Python Program to Count words in a String using Dictionary
def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)

#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")





###Exception Handling


#ZeroDivisionError occurs when you try to divide by zero.
1/0 


#NameError -- in this case, it means that you tried to use the variable a when it was not defined.
y = a + 5


#IndexError -- in this case, it occured because you tried to access data from a list using an index that does not exist for this list.
a = [1, 2, 3]
a[10]



# Try Except Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")
        



# Try Except Specific
# potential code before try catch
'''
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
    
# code that will execute if there is no exception or a one that we are handling
'''



#Try Except Specific Example
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
    
    

#Try Except Else and Finally


# potential code before try catch
'''
try:
    # code to try to execute
except ZeroDivisionError:
    # code to execute if there is a ZeroDivisionError
except NameError:
    # code to execute if there is a NameError
except:
    # code to execute if ther is any exception
else:
    # code to execute if there is no exception
finally:
    # code to execute at the end of the try except no matter what
    
# code that will execute if there is no exception or a one that we are handling
'''


#Try Except Else and Finally Example

a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
    



  
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
    
    



def safe_divide(numerator,denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
# Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator,denominator))






import math
def sq_root(number1):
    try:
        result = math.sqrt(number1)
        return result
    except ValueError:
        print("Invalid input! Please enter a positive integer or a float value.")
        return None

number1 = int or float(input("Enter the number:"))
print(sq_root(number1))






def calc(num):
    try:
        result = num / (num-5)
        print(result)
    except Exception as e:
        print("Error")

user_input= float(input("Enter a num"))
calc(user_input)




### Classes and Objects

##Creating a Class

# Import the library
import matplotlib.pyplot as plt


# Create a class Circle
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color 
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
        

# Create an instance of a class Circle

# Create an object RedCircle
RedCircle = Circle(10, 'red')

# Find out the methods can be used on the object RedCircle
dir(RedCircle)

# Print the object attribute radius
RedCircle.radius
RedCircle.color

# Set the object attribute radius
RedCircle.radius = 1
RedCircle.radius

# Call the method drawCircle
RedCircle.drawCircle()

# Use method to change the object attribute radius
print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)


# Create a blue circle with a given radius
BlueCircle = Circle(radius=100)

# Print the object attributes
BlueCircle.radius
BlueCircle.color

# Call the method drawCircle
BlueCircle.drawCircle()



##Create a class Rectangle

# Create a new Rectangle class for creating a rectangle object
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
        

# Create a new object rectangle
SkinnyBlueRectangle = Rectangle(2, 3, 'blue')