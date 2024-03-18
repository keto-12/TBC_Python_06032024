#Lecture4_Task1
# დაწერეთ პროგრამა რომელიც მიიღებს
# მოთამაშეების რაოდენობას.
# Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს
# შემთხვევითი კამათლების წყვილი და დაბეჭდოს ეკრანზე. Მაგალითად:
#Enter players number: 2
#3 4
#2 1

import random

number_of_players=int(input("Write a number of players:"))

if number_of_players == 0:
    print("Please, enter a number more than 0")
if number_of_players <0:
    print("Please enter a positive number")

for i in range(number_of_players):
    print(random.randint(1,6),random.randint(1,6))
