#Task_3
#float გამოვიყენე, რომ არამთელი რიცხვების გამოყენებისას კოდში შეცდომა ამერიდებინა :)
print("Hello, let's calculate a perimeter and area of a triangle!")
a=float(input("Please, give us the length of the first side. Enter a number :"))
if  float(a):
    print("Thanks")
b=float(input("Now, please, give us the length of the second side. Enter a number:"))
if float(b):
    print("Thanks")
c=float(input("It's time to give us the length of the third side. Enter a number :"))
if float(c):
    print("Thanks")
perimeter = a+b+c
semi_perimeter = perimeter/2
area =(semi_perimeter*(semi_perimeter-a)*(semi_perimeter-b)*(semi_perimeter-c))**0.5
print("The perimeter of the triangle is",perimeter)
print("The area of the triange is",area)
