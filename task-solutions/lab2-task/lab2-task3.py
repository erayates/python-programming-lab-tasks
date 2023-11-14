# Task 3
intA = int(input("Enter an integer number: "))
intB = int(input("Enter an integer number again: "))

if intA > intB:
    print("%i > %i" % (intA,intB))
elif intA == intB:
    print("%i = %i" % (intA,intB))
else:
    print("%i < %i" % (intA,intB))