#Task1	დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს n. n > 1.
#  პროგრამამ უნდა დაითვალის რიცხვი x და დაბეჭდოს ეკრანზე.
# Რიცხვი x ის დათვლის პრინციპი ასეთია.
# x = 4 * (1 - 1/3 + 1/5 - 1/7 + 1/9 - ... (+/-)1 / (2n-1) )
#გაუშვით პროგრამა და გადაეცით შემდეგი მნიშვნელობები: 10, 100, 10000, 100000.
# რას ამჩნევთ?

import math

n=float(input("Please, enter a natural number that is greater than one: "))
if n <=1.0:
    print("The number is not correct. Please enter a natural number that is greated than one")
    exit(1)

result= 1.0
for n in range (2, 100000):
    result+=(-1)**(n-1)*(1/float(2*n-1))
    answer=4*result
    print(answer)


