def sum(num1,num2):
    sum = num1 + num2
    print("Sum of " + str(num1) + " and " + str(num2) + " is: " + str(sum))

sum(21,22)


print(7250//3600)

print("7" < "number")

def attempts(n):
    x = 1
    while x<=n:
        print("Attempt " + str(x))
        x+=1
    print("Done")

attempts(1)

x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1
print(x)
product = 1
while x < 10:
    product = product * x
    x = x + 1

print(str(sum) + str(product))

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]" , end=" ")
    print()


#zip example with lists
list1 = ["one", "two", "three"]
list2 = [1,2]
zippedlist = zip(list1,list2)
print(zippedlist)
print(list(zippedlist))
print(type(zippedlist))


#factorial example using recursive call to a function

def factorial(n):
#  print("Factorial called with " + str(n))
  if n < 2:
#    print("Returning 1")
    return 1
  result = n * factorial(n-1)
#  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

print(str(factorial(4)))
#print(str(factorial(999)))

# factorial(1000) will return and error as maximum depth of recursion would have exceeded

# another good recursion example to check if a given number is a power of a given base
# keep dividing the number by base until result is 1. If true, then its a power, else, its not
def is_power_of(number, base):
 # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return (number == 1)

    # Recursive case: keep dividing number by base.
    return is_power_of(number / base, base)


print(is_power_of(8,2))     # Should be True
print(is_power_of(64,4))    # Should be True
print(is_power_of(70,10))   # Should be False


# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_10(end):
    # Initializeq the "count" variable as a string.
    count = ""

    # The range function parameters instruct Python to start the count  
    # at 0 and stop at the variable given as the upper end of the range. 
    # Since the value of the high end of a range is excluded by default,  
    # you can make Python include the "end" value by adding +1 to it. 
    # The third parameter tells Python to increment the count by 10.
    for number in range(0,end+1,10):

        # Although the variable "count" will hold a count of integers,  
        # this example will be converted to a string using "str(number)" 
        # in order to display the incremental count from 0 to the "end" 
        # value on the same line with a space " " separating each 
        # number.  
        count += str(number) + " "
        
    # The .strip() method will trim the final space " " from the end of 
    # the string "count"  
    return count.strip()


# Call the function with 1 integer parameter.
print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100

# recursion function to find out number of digits in a number
def x_figure_salary(salary):
    
    if salary < 10:
        return 1
    else:
        return 1 + x_figure_salary(salary/10)

salary = 5000000
print("Number of digits in salary of", salary, "is =", (x_figure_salary(salary)))


# example of formatting the output using string format options
def to_celcius(farenheit):
    return (farenheit - 32)*5/9

for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celcius(x)))
    
# This function accepts a given string and checks each character of 
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty 
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards" 
    # variable will hold the same letters as "forwards", but in  
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

        # The if-statement checks if the character is not a space.
        if character.isalpha():

            # If True, the body of the loop adds the character to the
            # to the end of "forwards" and to the front of
            # "backwards". 
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action
        # is needed. This coding approach results prevents any 
        # non-alphabetical characters from being written to the
        # "forwards" and "backwards" variables. The for loop will 
        # restart until all characters in "my_string" have been
        # processed.
        
    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will 
    # need to be converted to use the same case for this comparison. 
    if forwards.lower() == backwards.lower():
        return True
    return False
 
print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or a cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True

# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 
def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "p" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "old_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the 
        # old date replaced by the new date. The schedule[:-p] part of 
        # the code trims the "old_date" substring from "schedule" 
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as 
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The 
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.  
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the schedule with the new date.
        return new_schedule
        
    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule
 
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"


#Sample code to print all characters before a specified character
weather = "Rainfall"
print(weather[:weather.index("f")])
print(type(weather))


numbers = ["one","two","three"]
print(numbers)
print(type(numbers))

numbers.pop(2)
print(numbers)

numbers.append("four")
numbers.append(5)

print(numbers)

# exmaple of enumerate function

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

# another enumerate example to only display every other element in the output

def skip_elements(elements):
	# code goes here
	result = []
	for index, element in enumerate(elements):
		if index % 2 == 0:
			result.append(element)
	return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


#example of creating lists with comprehension

z = [x for x in range(0,101,) if x % 3 == 0]
print(z)

def squares(start, end):
    return [x**2 for x in range(start,end+1)]


print(squares(2, 3))    # Should print [4, 9]
print(squares(1, 5))    # Should print [1, 4, 9, 16, 25]
print(squares(0, 10))   # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# returning multiple values from functions

def calculate_numbers(a, b):
    return a+b, a-b, a*b, a/b

add_result, sub_result, mul_result, div_result = calculate_numbers(10, 2)
print(add_result)  # Outputs: 12
print(sub_result)  # Outputs: 8

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]


# pig latin text conversion example
def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for index in range(len(words)):
    # Create the pig latin word and add it to the list
    word = words[index]
    say = word[1:] + word[0] + "ay"
    words[index] = say
    # Turn the list back into a phrase
  return " ".join(words)
    
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"


# dictionary example:

def count_letters(text): # receive a string of characters
  result = {} # create an empty dictionary
  for letter in text: # iterate over each character in the string
    if letter not in result: # initialize each key (i.e. character that has previously not been counted) value to 0
      result[letter] = 0
    result[letter] += 1 # increment the current character count by 1 from the string for a matching key denoted by letter
  return result
print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))
print(count_letters("Will this work for numbers as well 1234123422"))


# This function returns the total time, with minutes represented as 
# decimals (example: 1 hour 30 minutes = 1.5), for all end user time
# spent accessing a server in a given day. 


def sum_server_use_time(Server):

    # Initialize the variable as a float data type, which will be used
    # to hold the sum of the total hours and minutes of server usage by
    # end users in a day.
    total_use_time = 0.0

    # Iterate through the "Server" dictionary’s key and value items 
    # using a for loop.
    for key,value in Server.items():

        # For each end user key, add the associated time value to the
        # total sum of all end user use time.
        total_use_time += Server[key]
        
    # Round the return value and limit to 2 decimal places.
    return round(total_use_time, 2)  

FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

print(sum_server_use_time(FileServer)) # Should print 20.1

# This function receives a dictionary, which contains common employee 
# last names as keys, and a list of employee first names as values. 
# The function generates a new list that contains each employees’ full
# name (First_name Last_Name). For example, the key "Garcia" with the 
# values ["Maria", "Hugo", "Lucia"] should be converted to a list 
# that contains ["Maria Garcia", "Hugo Garcia", "Lucia Garcia"].


def list_full_names(employee_dictionary):
    # Initialize the "full_names" variable as a list data type using
    # empty [] square brackets.  
    full_names = []

    # The outer for loop iterates through each "last_name" key and 
    # associated "first_name" values, in the "employee_dictionary" items.
    for last_name, first_names in employee_dictionary.items():

        # The inner for loop iterates over each "first_name" value in 
        # the list of "first_names" for one "last_name" key at a time.
        for first_name in first_names:

            # Append the new "full_names" list with the "first_name" value
            # concatenated with a space " ", and the key "last_name". 
            full_names.append(first_name+" "+last_name)
            
    # Return the new "full_names" list once the outer for loop has 
    # completed all iterations. 
    return(full_names)


print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']


# This function receives a dictionary, which contains resource 
# categories (keys) with a list of available resources (values) for a 
# company’s IT Department. The resources belong to multiple categories.
# The function should reverse the keys and values to show which 
# categories (values) each resource (key) belongs to. 


def invert_resource_dict(resource_dictionary):
  # Initialize a "new_dictionary" variable as a dict data type using
  # empty {} curly brackets. 
    new_dictionary = {}
    # The outer for loop iterates through each "resource_group" and 
    # associated "resources" in the "resource_dictionary" items.
    for resource_group, resources in resource_dictionary.items():
        # The inner for loop iterates over each "resource" value in 
        # the list of "resources" for one "resource_group" key at a time.
        for resource in resources:
            # The if-statement checks if the current "resource" value has 
            # been appended as a key to the "new_dictionary" yet.
            if resource in new_dictionary:
                # If True, then append the "resource_group" as a value to the
                # "resource", which is now the key.
                new_dictionary[resource].append(resource_group)
            # If False (else), then add the "resource" as a new key with the 
            # "resource_group" as a value for that key.
            else:
                new_dictionary[resource] = [resource_group]
    # Return the new dictionary once the outer for loop has completed  
    # all iterations.
    return(new_dictionary)


print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
        "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}

#creating a new list from a dictionary which has key and lists as values

def email_list(domains):
    emails = []
    for domain,users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user,domain))
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

# The network() function accepts a dictionary "servers" as a parameter.
def network(servers):

    # A string variable is initialized to hold the "result". 
    result = ""

    # For each "hostname" (key) and "IP address" (value) in the "servers" dictionary items...
    for hostname, IP_address in servers.items():

        # A string identifying the hostname and IP address for each server is added
        # to the "result" variable. The string .format() function and is used to plug
        # the hostname and IP_address variables into the designated {} placeholders
        # within the string.
        result += "The IP address of the {} server is {}".format(hostname, IP_address) + "\n"
    
    # Return the "result" variable string.
    return result 

# Call the "network" function with the dictionary. 
print(network({"Domain Name Server":"8.8.8.8", "Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33", "Mail Server":"192.168.1.190"}))

# Should print:
# The IP address of the Domain Name Server server is 8.8.8.8
# The IP address of the Gateway Server server is 192.168.1.1
# The IP address of the Print Server server is 192.168.1.33
# The IP address of the Mail Server server is 192.168.1.190


# example of how to create a class in python with default initializationg dunder method and string dunder method
class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
    


honeycrisp = Apple("red", "sweet")
print(honeycrisp)
# prints "an apple which is red and sweet"


# example of a class with a special operator method add/multiply
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()
    def __mul__(self,other):
        return self.area() * other.area()
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)
print("The product of area of both triangles is:", triangle1*triangle2)


# a short sort example with strings and length of strings:

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(sorted(names))
print(names)
print(sorted(names, key=len))

print(sorted(names,reverse=True))