x = int(input("Enter 1st number:"))
y = int(input("Enter 2nd number:"))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 

print("Sum :", add(x, y))
print("Difference :", subtract(x, y))
print("product :", multiply(x, y))
print("Quotient :", divide(x, y))