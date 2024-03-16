# 2.	დაწერეთ პროგრამა რომელიც მიიღებს დადებით
# მთელ რიცხვს - n. 0 < n <= 1000.
# პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა რომელიც მიიღება შემდეგი პირობით:
# თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, ხოლო თუ რიცხვი კენტია ეს რიცხვი
# უნდა გავამრავლოთ 3-ზე და დავუმატოთ 1, იქამდე სანამ არ მივიღებთ 1-ს. Მაგალითი:
# Enter number: 10
# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# 	ახსნა: 10 რადგან ლუწია გავყავით 2-ზე მივიღეთ 5
# 	5 რადგან კენტია გავამრავლეთ 3-ზე და დავუმატეთ 1. მივიღეთ 16
# 	ამის შემდეგ 16, 8, 4, 2 ლუწებია და ყველას ვყოფთ 2-ზე.

#The collatz sequence is a conjecture in mathematics that follows a sequence.
# The sequence begins with any positive integer, say n.
# If the integer n is odd, the next number in sequence would be 3n+1.
# If the integer n is even, the next number in sequence would be n/2.
#Remove square brackets from list:
#res = str(test_list)[1:-1]
#List /@ Rule @@@ lop

input_number =int(input("Please, enter an integer between 0 and 1000:"))

if input_number <0 or input_number > 1000:
    print(int(input("That is not correct input. Please, enter positive integer between 0 and 1000:" )))
    exit(1)

def Collatz(input_number):
    out = []
    # lop = out  #ვერ გავიგე როგორ გავაკეთო
    # [->} & @@@ lop
    while input_number > 1:
        if input_number % 2 == 0:
            out.append(input_number // 2)
            input_number = input_number // 2 # updating input_number

        elif input_number % 2 != 0:
            out.append((input_number * 3) + 1)
            input_number = (input_number* 3) + 1  # updating input_number
    print(str(out)[1:-1])

Collatz(input_number)
