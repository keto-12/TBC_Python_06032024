#Task3
# დაწერეთ პროგრამა რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე.
# Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის.
# Თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს,
# დაბეჭდეთ You are winner. Თუ მომხმარებლის შემოყვანილი რიცხვი მეტია,
# კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. თუ მომხმარებლის შემოყვანილი რიცხვი
# ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ low.
# Მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. Თუ მომხმარებელმა 10 მცდელბაში ვერ გამოიცნო რიცხვი,
# დაბეჭდეთ Computer is winner.


guess_count=0
guess_limit=10
program_number =int(input("Program, please generate an integer between 0 and 100:"))
#user_number = int(input("User, please enter an integer between 0 and 100:"))
print(f"program number is {program_number}")
while guess_count<guess_limit:
     guess = int(input('Guess a number: '))
     guess_count += 1
     if guess == program_number:
         print("You are winner")
         break
     elif guess > program_number:
         print("High")
     else:
         print("Low")

else: #guess_count > guess_limit:
    print("Computer is winner")

