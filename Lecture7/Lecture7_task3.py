#3.	დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n.
# 0 <= n < 10000 და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას
# და ამ რიცხვში შემავალი ციფრების ჯამს. გამოიყენეთ while ციკლი
# მაგალითი:
# enter number: 7923
# reversed number is 3297
# sum of digits: 21

input_number =int(input("Please, enter an integer between 0 and 10000:"))

if input_number <0 or input_number > 10000:
    print(int(input("That is not correct input. Please, enter positive integer between 0 and 1000:" )))
    exit(1)

revers_number = 0
sum =0

while input_number != 0 :
    remainder = input_number % 10
    sum = sum + remainder
    revers_number = revers_number * 10 + remainder
    input_number = input_number // 10

print(revers_number)
print (sum)
