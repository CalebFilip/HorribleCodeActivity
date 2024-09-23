def add(a, c):
    #counter for while loop
    d = 0
    #loop to determine how much should be added
    while c > d:
        #add 1 to first number every iteration
        a += 1
        d +=1
    #returns total
    return a

def sub(a,c):
    #same thing as add method but opposite :P
    # counter for while loop
    d = 0
    # loop to determine how much should be added
    while c > d:
        # add 1 to first number every iteration
        a -= 1
        d += 1
    # returns total
    return a

def mul(a,c):
    # counter for while loop
    d = 1
    #setting e to the number that needs to be added
    e = a
    # loop to determine how much should be added
    while c > d:
        # add 1 to first number every iteration
        a += e
        d += 1
    # returns total
    return a



#getting input for first number
a = int(input('Enter First Number: '))
#getting operator
b = input('Enter Operator(+, -, /, *): ')
#getting input for second number
c= int(input('Enter Second Number: '))

#checking to see what operator was inputted
if b == '+':
    print(add(a,c))

#checking to see what operator was inputted
elif b == '-':
    print(sub(a,c))

#checking to see what operator was inputted
elif b == '/':
    print()

#checking to see what operator was inputted
elif b == '*':
    print(mul(a,c))

else:
    print('invalid operator')