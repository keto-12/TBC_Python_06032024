#Lecture2_Task2
#2.	Დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს,
# დაადგენს პირველი რიცხვი არის თუ არა მეორე რიცხვის ჯერადი და
# დაბეჭდავს ეკრანზე.
# A რიცხვს ეწოდება B რიცხვის ჯერადი, თუ A = B * n,  სადაც n ნატურალური რიცხვია.

number_1=int(input("Please, write a number:"))
number_2=int(input("Please, write the second number:"))
multiple=number_1/number_2
if number_1%number_2==0 and multiple>1 :
    print("number_1 is a multiple of number_2")
else:
    print("number_1 is not a multiple of number_2")
