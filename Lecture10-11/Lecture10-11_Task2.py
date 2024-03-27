#Task 2
# 2.	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1.
# პროგრამამ უნდა დააგენერიროს n ცალი წყვილი შემთხვევითი რიცხვი a,b, სადაც 0<a<1 და 0<b<1. Შემოიღეთ მთვლელი counter,
# თუ დაგენერირებული რიცხვი აკმაყოფილებს პირობას math.sqrt(a ** 2 + b ** 2) <=1,
# counter-ის მნიშვნელობა გაზარდეთ 1-ით. ეკრანზე დაბეჭდეთ 4 * counter / n.
# გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 100000, 10000000. Რას ამჩნევთ?

import random
import math


n=int(input("Please, enter a natural number that is greater than one: "))

if n <=1:
    print("The number is not correct. Please enter a natural number that is greated than one")
    exit(1)


for n in range (100000000):
    a, b =random.random(), random.random()
    if b<a:
        a,b = b,a
    print(a)
    print(b)
    print(a,b)

    counter = 0
    if n ==math.sqrt(a ** 2 + b ** 2) <=1:
        counter+=1
        print (4 * counter / n)
    else:
         exit(1)