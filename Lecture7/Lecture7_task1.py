#1. დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20.
# Პროგრამამ უნდა იპოვოს მიმდევრობის 0-დან n-მდე წევრები.
# Მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1,
# ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი.
# გამოიყენეთ while ციკლი და არ შეიძლება list-ის გამოყენება. Მაგალითი: Enter number: 5 0 1 1 2 3

number_input= (int(input("Please, enter positive integer between 0 and 20:" )))

if number_input <0 or number_input >20:
    print(int(input("That is not correct input. Please, enter positive integer between 0 and 20:" )))
    exit(1)

a,b = 0,1
while b <= number_input:
     print(f"  {b}", end="\t")
     a, b = b, a+b
