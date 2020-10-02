"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""


    
    
    
 
    
def RandomStringGenerator ():
    import string
    options=string.ascii_letters+string.digits
    a = int(input('Enter minimum string length(above 0): '))
    b = int(input('Enter maximum string length(below 10): '))
    n = int(input('How many random strings to generate? (max 12) '))
    
    if n<=12 and a>0 and b<10:
        n1=0
        import string
        options=string.ascii_letters+string.digits
        while n1<n:
            lst = [random.choice(options) for i in range(a,b+1)]
            word="".join(lst)
            print(word)
            n1+=1
    else:
        print("remember, the string needs to be between 0 and 10, and you can generate max 12 strings")
        RandomStringGenerator()


RandomStringGenerator()