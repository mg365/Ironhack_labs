"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from zero to five')
a = input('Please choose your first number (zero to five): ')
b = input('What do you want to do? plus or minus: ')
c = input('Please choose your second number (zero to five): ')


x=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
x1=["zero","one","two","three","four","five"]

if b=="plus":
    
    #any number plus any number
    
    if a in x1 and c in x1:
        result=x.index(a)+x.index(c)
        print(a,"plus",c,"equals",x[result])
    else:
        print("I am not able to answer this question. Check your input")
    
    #any number minus any number
    
elif b=="minus":
    if a in x1 and c in x1 and x.index(a)>x.index(c):
        result=x.index(a)-x.index(c)
        print(a,"minus",c,"equals",x[abs(result)])
        
    elif a in x1 and c in x1 and x.index(a)<x.index(c):
        result=x.index(a)-x.index(c)
        print(a,"minus",c,"equals","negative",x[abs(result)])
    
    else:
        print("I am not able to answer this question. Check your input")
else:
    print("You can only sum (write plus) or subtract (write minus).Check your input")
print("Thanks for using this calculator, goodbye :)")