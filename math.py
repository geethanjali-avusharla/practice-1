# Add implementation
def add(x,y):
    return x+y;
# Subtract implementation
def subtract(x,y):
    return x-y            #on master
# multiply implementation
def multiply(x,y):
    return x*y          #on bug456
# divide implementation
def divide(x,y):
    if y==0:            #on master
        return DIVIDE_BY_0_ERROR;
    else:
        return x/y
