#Lecture4_Task4*
# დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 20.
# Პროგრამამ უნდა იპოვოს მიმდევრობის n-ური წევრი.
# Მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1,
# ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. Მაგალითად:
#Enter number: 4
#3
def fib (n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(1,n):
             c = a + b
             a = b
             b = c
        return (b)

sequence_number = int(input("Please enter an integer between 0 and 20:"))
if sequence_number<0 or sequence_number>20:
    print("Please, enter an integer between 0 and 20:")
else:
    print(fib(sequence_number))


