#Lecture4_Task2
#დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n.
# Პროგრამამ, უნდა დააგენერიროს n ცალი შემთვევით მთელი რიცხვი 0 – 1000 და
# ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30.

import random

number_input = int(input("Please, enter a positive integer between 0 and 30:"))
if number_input==0 or number_input>30:
    print("Please, enter a positive integer between 0 and 30")
elif number_input<0:
    print("Please, enter a positive integer between 0 and 30")
else:
    print(max([random.randint(0,1000)for i in range(number_input) ]))
