# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods
name = 'collins'
age = 45
print ('Hello I am ' + name +' and i am ' + str(age))


# String Formatting
# Arguments by position
#print('{1}, {2}, {0}'.format('a','b','c'))     #they go in position

#Arguments by name
print('My name is {name} and I am {age}'.format(name='Brad', age='45'))

#F- Strings  (only in 3.6+)
print(f'My name is {name} and I am {age}')


# String Methods
s ='hello there world '
print(s.capitalize())
print(s.upper())
print(s.lower())

#swpa  case
print(s.swapcase())  #swaps lowere for upper and the other way round

#Get length
print(len(s))

#Replace
print(s.replace('world','wooooorld'))  # replce world in the string for woooorld.

# Count
sub = 'h'
print(s.count(sub))  #counts how may h are in hello world- lower case.

#Starts with
print(s.startswith('hello'))

#Ends with
print(s.endswith('d'))  #it will return with True

#Split into a list
print(s.split())

#Find a position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
