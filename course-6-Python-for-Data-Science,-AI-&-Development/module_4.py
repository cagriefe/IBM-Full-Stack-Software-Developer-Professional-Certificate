import urllib.request
import requests
import pandas as pd

# Define the URL and filename
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'example1.txt'

# Download the file using urllib
urllib.request.urlretrieve(url, filename)
print("File downloaded using urllib")

# Alternative method using requests
def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download file: {response.status_code}")

# Download the file using requests
download_file(url, filename)
print("File downloaded using requests")

# Read the file into a pandas DataFrame
df = pd.read_csv(filename)
print(df.head())



# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")


# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent


# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()



## better way to open a file

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Verify if the file is closed
file1.closed

# See the content of file
print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))
    

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))
    

# Read certain amount of characters
with open(example1, "r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))
    

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())

#example
with open(example1, "r") as file1:
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Iterate through the lines
with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
            
            
# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()
    
# Print the lines
FileasList[0]
FileasList[1]
FileasList[2]


### Write and Save Files

# Write line to file
exmp2 = 'Example2.txt'
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A")
    
# Read file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())
    
# Write lines to file
with open(exmp2, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    
# Check whether write to file
with open(exmp2, 'r') as testwritefile:
    print(testwritefile.read())


# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
Lines


# Write the strings in the list to text file
with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)
        
# Verify if writing to file is successfully executed
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

#However, note that setting the mode to w overwrites all the existing data in the file.
with open('Example2.txt', 'w') as writefile:
    writefile.write("Overwrite\n")
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())



##Appending files

# Write a new line to text file
with open('Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")
    testwritefile.write("This is line D\n")
    testwritefile.write("This is line E\n")
    

# Verify if the new line is in the text file
with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())
    

##Additional modes
# r+ : Reading and writing. Cannot truncate the file.
# w+ : Writing and reading. Truncates the file.
# a+ : Appending and Reading. Creates a new file, if none exists. You dont have to dwell on the specifics of each mode for this lab.

#a+
with open('Example2.txt', 'a+') as testwritefile:
    testwritefile.write("This is line E\n")
    print(testwritefile.read())
    


# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end

with open('Example2.txt', 'a+') as testwritefile:
    print("Initial Location: {}".format(testwritefile.tell()))
    
    data = testwritefile.read()
    if (not data):  #empty strings return false in python
            print('Read nothing') 
    else: 
            print(testwritefile.read())
            
    testwritefile.seek(0,0) # move 0 bytes from beginning.
    
    print("\nNew Location : {}".format(testwritefile.tell()))
    data = testwritefile.read()
    if (not data): 
            print('Read nothing') 
    else: 
            print(data)
    
    print("Location after read: {}".format(testwritefile.tell()) )
    



#a note on the difference between w+ and r+. Both of these modes allow access to read and write methods, however, opening a file in w+ overwrites it and deletes all pre-existing data.
#In the following code block, Run the code as it is first and then run it without the .truncate().

with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    testwritefile.seek(0,0)
    print(testwritefile.read())


# To work with a file on existing data, use r+ and a+. While using r+, it can be useful to add a .truncate() method at the end of your data. This will reduce the file to your data and delete everything that follows.

with open('Example2.txt', 'r+') as testwritefile:
    testwritefile.seek(0,0) #write at beginning of file
    testwritefile.write("Line 1" + "\n")
    testwritefile.write("Line 2" + "\n")
    testwritefile.write("Line 3" + "\n")
    testwritefile.write("Line 4" + "\n")
    testwritefile.write("finished\n")
    #Uncomment the line below
    testwritefile.truncate()
    testwritefile.seek(0,0)
    print(testwritefile.read())
    
    
    
    
### Copy a file

# Copy file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)
                

# Verify if the copy is successfully executed
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())
    



### Pandas

import pandas as pd

#Define a dictionary 'x'
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df


#Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x

#check the type of x
type(x)


#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
z

#Note : x = df[['']] ---> type is frame
#       x = df[''] ---> type is series


#example to use
x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

df = pd.DataFrame(x)

df


## loc() and iloc() functions

#loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.
#loc[row_label, column_label]


## iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.
#iloc[row_index, column_index]


# Access the value on the first row and the first column
df.iloc[0, 0]


# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[0, 'Salary']


#Let us create a new dataframe called 'df2' and assign 'df' to it. Now, let us set the "Name" column as an index column using the method set_index()

df2=df
df2=df2.set_index("Name")

#To display the first 5 rows of new dataframe
df2.head()

#Now, let us access the column using the name
df2.loc['Jane', 'Salary']

#Use the iloc() function to get the Salary of Mary in the newly created dataframe df2.
df2.iloc[3,2]


##Slicing

# let us do the slicing using old dataframe df
df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
df2.loc['Rose':'Jane', 'ID':'Department']

#using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
df.loc[2:3, 'Name':'Department']




### Pandas
# Read data from CSV file

# import pandas as pd
# #from pyodide.http import pyfetch
# import pandas as pd

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"

# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())

# df = pd.read_csv("TopSellingAlbums.csv")



# Print first five rows of the dataframe
df.head()


# Read data from Excel File and print the first five rows
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
df = pd.read_excel(xlsx_path)
df.head()


# Access to the column Length
x = df[['Length']]
x


# Get the column as a series
x = df['Length']
x

# Get the column as a dataframe
x = df[['Artist']]
type(x)
x

# Access to multiple columns
y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]


# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[0, 'Released']

# Access the column using the name
df.loc[1, 'Released']


# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']



### Numpy


# import numpy library
import numpy as np 

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

# Check NumPy version
print(np.__version__)

# Check the type of the array
type(a)

# Check the type of the values stored in numpy array
a.dtype


## Assign Value

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c

# Assign the first element to 100
c[0] = 100
c

# Assign the 5th element to 0
c[4] = 0
c


## Slicing

# Slicing the numpy array]
d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c


# We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

#If we don't pass start its considered 0
print(arr[:4])

# If we don't pass end it considers till the length of array.
print(arr[4:])

#If we don't pass step its considered 1
print(arr[1:5:])


# Print the even elements in the given array.
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr[1::2])


## Assign Value with List

# Create the index list
select = [0, 2, 3, 4]
select


# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

## Other Attributes

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
a.shape



## Numpy Statistical Functions

# Create a numpy array
a = np.array([1, -1, 1, -1])


# Get the mean(total) of numpy array
mean = a.mean()
mean

# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation


# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b

# Get the biggest value in the numpy array
max_b = b.max()
max_b

# Get the smallest value in the numpy array
min_b = b.min()
min_b


## Numpy Array Operations

# Array addition

# Numpy array u
u = np.array([1, 0])
u

# Numpy array v
v = np.array([0, 1])
v

# Numpy Array Addition
z = np.add(u, v)
z


# Plotting functions


#The operation is equivalent to vector addition:
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
# Plot numpy arrays
Plotvec1(u, z, v)
plt.show()




import numpy as np
# Array Subtraction

a = np.array([10, 20, 30])
a

b = np.array([5, 10, 15])
b

c = np.subtract(a, b)

print(c)



# Array Multiplication

x = np.array([1, 2])
x

y = np.array([2, 1])
y

# Numpy Array Multiplication
z = np.multiply(x, y)
z



# Array Division

a = np.array([10, 20, 30])
a

b = np.array([2, 10, 5])
b

# Numpy Array Division
c = np.divide(a, b)
c



# Dot Product

X = np.array([1, 2])
Y = np.array([3, 2])


# Calculate the dot product
np.dot(X, Y)

#Elements of X
print(X[0])
print(X[1])

#Elements of Y
print(Y[0])
print(Y[1])



# Adding Constant to a Numpy Array

# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
u

# Add the constant to array
u + 1



# Mathematical Functions

# The value of pi
np.pi

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])


# Calculate the sin of each elements
y = np.sin(x)
y



#Linspace

#numpy.linspace(start, stop, num = int value)
# start : start of interval range
# stop : end of interval range
# num : Number of samples to generate.


# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()



# Iterating 1-D Arrays

arr1 = np.array([1, 2, 3])
print(arr1)

for x in arr1:
  print(x)
  
  

### 2D Numpy

import numpy as np
# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A

# Show the numpy array dimensions
A.ndim

# Show the numpy array shape
A.shape

# Show the numpy array size
A.size



# Accessing different elements of a Numpy Array

# Access the element on the second row and third column
A[1, 2]

# Access the element on the second row and third column
A[1][2]

# Access the element on the first row and first column
A[0][0]

# Access the element on the first row and first and second columns
A[0][0:2]

# Access the element on the first and second rows and third column
A[0:2, 2]



# Basic Operations

# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
Y

# Add X and Y
Z = X + Y
Z

# Multiply Y with 2
Z = 2 * Y
Z

# Multiply X with Y
Z = X * Y
Z


# Create a matrix A,B
A = np.array([[0, 1, 1], [1, 0, 1]])
A

B = np.array([[1, 1], [1, 1], [-1, 1]])
B

# Calculate the dot product
Z = np.dot(A,B)
Z

# Calculate the sine of Z
np.sin(Z)


# Create a matrix C
C = np.array([[1,1],[2,2],[3,3]])
C

# Get the transposed of C
C.T