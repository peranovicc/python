"""
DOC STRING
"""

# Document strings must be first thing in a file or a function (for it to work with __doc__)


print("Hello")

x = 5

if x < 6: 
    print('x is less than 6') # Important! : Indentation acts as code block: {} in some languages 
    # some commands

else:
    print('x is not less than 6')



# Functions

def funn():
    """
    Detailed explanation of a function
    """
    print('foo bar')

print(funn.__doc__) # Printing of doc-comment of a funn function

some_str = "hello"
some_int = 5
some_float = 4.32

print(type(some_str),type(some_int),type(some_float))


# i++ is not a valid syntax (there are no unary increment/decrements)
# You can however use shorthand assigment  i += 1

# You can explicitly cast to type

number_string = "55"
print(int(number_string) + 1)
print(float(number_string) + 1)
print(str(number_string) + "1")


# Substring shorthand syntax

some_long_string = "How are you Doing?"
print(some_long_string[0:5]) # Returns a string from position 0 to 5 (excluding 5)
print(some_long_string[-5]) # Returns one character at position 5 counting from last letter backwards
print(some_long_string[-5:]) # Returns a string from -5 to the end
print(some_long_string[:-5]) # Returns a string from beginning to -5 (excluding -5)

print("  some example with whitespace    ".strip()) # strips whitespace from beginning and end of a string (javascript trim())


# len, upper, lower

print(len(some_long_string)) # there is no .length / .len
print(some_long_string.upper())
print(some_long_string.lower())


