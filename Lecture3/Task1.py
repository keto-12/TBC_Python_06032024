#Task1
# დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს (x,y)
# და დაბეჭდავს რიცხვს რომელიც მიიღება x-ის y ხარისხში აყვანით.
# იხ module math

import math
def power(x,y):
    if y==0:
       return(1)
    elif y==1:
        return(x)
    else:
        return(x*power(x,y-1))

x=int(input("Please enter a positive integer:"))
y=int (input("Please enter the second positive integer:"))
print(power(x,y))
