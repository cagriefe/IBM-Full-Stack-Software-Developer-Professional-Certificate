# Module 1: Python Basics
# About the Course
# Types
# Expressions and Variables
# String Operations


# Python uses clear and readable syntax
# • Python has a huge global community and a wealth of documentation
# • For data science you can use Python's scientific computing libraries like Pandas, NumPy, SciPy, and Matplotlib
# • Python can also be used for Natural Language Processing (NLP)
# using the Natural Language Toolkit (NLTK)
# • Python community has a well-documented history of paving the way for diversity and inclusion efforts in the tech industry as a whole

print("Hello, world!")

# Types
# 11 int
# 21.213 float
# type("Hello World") str
# True False Boolean


###String

##Slicing

name= "Michael Jackson"
print(name[0:4]) # Take the slice on variable name with only index 0 to index 3
print(name[::2]) # Get every second element. The elments on index 1, 3, 5 ...
print(name[0:5:2]) # Get every second element in the range from index 0 to index 4


##Concatenate Strings

statement = name + " is the best"
print(statement) # Michael Jackson is the best
print(3 * name) #Michael JacksonMichael JacksonMichael Jackson

name = "Michael Jackson"
name = name + " is the best"
print(name) # Michael Jackson is the best


##Escape Sequences

print(" Michael Jackson \n is the best" )   # New line escape sequence
print(" Michael Jackson \t is the best" )   # Tab escape sequence
print(" Michael Jackson \\ is the best" )   # Include back slash in string
print(r" Michael Jackson \ is the best" )   # r will tell python that string will be display as raw string

#  Michael Jackson 
#  is the best
#  Michael Jackson         is the best
#  Michael Jackson \ is the best
#  Michael Jackson \ is the best


##String Manipulation Operations

# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Replace the old substring with the new target substring is the segment has been found in the string
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson" 
print(name.find('el'))

# Find the substring in the string.
print(name.find('Jack'))

# If cannot find the substring in the string
print(name.find('Jasdfasdasdf'))

#Split the substring into list
name = "Michael Jackson"
split_string = (name.split())
print(split_string)


##RegEx

import re


s1 = "Michael Jackson is the best"

# Define the pattern to search for
pattern = r"Jackson"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")
    

# Special Sequence	Meaning	                                                                Example
# \d                Matches any digit character (0-9)	                                    "123" matches "\d\d\d"
# \D	            Matches any non-digit character	                                        "hello" matches "\D\D\D\D\D"
# \w	            Matches any word character (a-z, A-Z, 0-9, and _)	                    "hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
# \W	            Matches any non-word character	                                        "@#$%" matches "\W\W\W\W"
# \s	            Matches any whitespace character (space, tab, newline, etc.)	        "hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
# \S	            Matches any non-whitespace character	                                "hello_world" matches "\S\S\S\S\S\S\S\S\S"
# \b	            Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
# \B	            Matches any position that is not a word boundary	                    "cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"


pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
    
#

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)

#

s2 = "Michael Jackson was a singer and known as the 'King of Pop'"


# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)

#

# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array) 

#

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 


