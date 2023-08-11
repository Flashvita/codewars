"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. 
Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples:

    "TestController"  -->  "test_controller"
    "MoviesAndBooks"  -->  "movies_and_books"
    "App7Test"        -->  "app7_test"
    1                 -->  "1"
    
"""
import re

def to_underscore(string):
    return str(string) if isinstance(string, int) else ("_".join(re.findall(r'[A-Z][^A-Z]*',  string))).lower()


print(to_underscore("TestController"))
print(to_underscore("MoviesAndBooks"))
print(to_underscore("1"))

