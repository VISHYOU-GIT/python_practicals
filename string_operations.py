#All string operations inbuilt in functions
string1 = "Hello, World!"
print("Original String:", string1)
print("Uppercase:", string1.upper())
print("Lowercase:", string1.lower())
print("Title Case:", string1.title())
print("Split:", string1.split(", "))
print("Replace 'World' with 'Python':", string1.replace("World", "Python"))
print("Strip whitespace:", "   Hello, World!   ".strip())
# Check if string contains only digits
print("Contains only digits:", string1.isdigit())
# Check if string is alphanumeric
print("Is alphanumeric:", string1.isalnum())
# Check if string starts with 'Hello'
print("Starts with 'Hello':", string1.startswith("Hello"))
# Check if string ends with '!'
print("Ends with '!':", string1.endswith("!"))
# Check if string contains a substring
print("Contains 'World':", "World" in string1)
# Check the length of the string
print("Length of string:", len(string1))
# Check if string is empty
print("Is string empty:", not string1)
#check if string is decimal
print("Is string a decimal:", string1.isdecimal())
#removes the leading and trailing whitespace
print("Stripped string:", "   Hello, World!   ".strip())
#removes the leading whitespace
print("Lstrip string:", "   Hello, World!   ".lstrip())
#removes the trailing whitespace
print("Rstrip string:", "   Hello, World!   ".rstrip())
#wap to implement selection sort algorithm
#wap to multiply the matrix

"""
ALGORITHM:
Demonstrates various built-in string methods available in Python:
1. Case conversion: upper(), lower(), title()
2. String splitting and joining: split(), replace()
3. Whitespace handling: strip(), lstrip(), rstrip()
4. String validation: isdigit(), isalnum(), isdecimal()
5. String searching: startswith(), endswith(), in operator
6. String properties: len(), boolean evaluation

EXAMPLE OUTPUT:
Original String: Hello, World!
Uppercase: HELLO, WORLD!
Lowercase: hello, world!
Title Case: Hello, World!
Split: ['Hello', 'World!']
Replace 'World' with 'Python': Hello, Python!
Strip whitespace: Hello, World!
Contains only digits: False
Is alphanumeric: False
Starts with 'Hello': True
Ends with '!': True
Contains 'World': True
Length of string: 13
Is string empty: False
Is string a decimal: False
Stripped string: Hello, World!
Lstrip string: Hello, World!   
Rstrip string:    Hello, World!

Time Complexity: Most operations are O(n) where n is string length
Space Complexity: Varies by operation, typically O(n) for new string creation
Note: Strings in Python are immutable
"""
