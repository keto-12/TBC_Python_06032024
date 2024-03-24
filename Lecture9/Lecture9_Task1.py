#Task1
# დაწერეთ პროგრამა რომელიც მიიღებს მიიღებს სტრიქონი და დაადგენს ეს ტექსტი არის თუ არა პალინდრომი.
# Პალინდრომი არის სიტყვა რომელიც მარცხნიდან და მარჯვნიდან ერთნაირად იკითხება.
# Მაგალითად: radar, level,  racecar არის პალინდრომები. Პროგრამამ უნდა დააიდენტიფიციროს
# პალინდრომი წინადადებაც. Წინადადებიდან უნდა უგულებელყოს ყველა სიმბოლო,
# გარდა ინგლისური სიმბოლოსებისა a-z, A-Z.
# Პროგრამამ უნდა უგულებელყოს სიმბოლოს რეგისტრი, Racecar არის პალინდრომი.
# მაგალითი 1.
# 	Input: racecar
# 	Output: Is palindrome
# მაგალითი 2.
# 	Input: Python
# 	Output: Is not palindrome
# მაგალითი 3.
# 	Input: Was it a car or a cat I saw?
# 	Output: Is palindrome
# Მაგალითი 4.
# 	Input: No lemon, no melon!
# 	Output: Is palindrome

user_input= input("Please, enter a string :")


i=0                      #  i იტერაცია სწორად წასაკითხად
j=len(user_input)-1      # j იტერაცია რევერსისთვის.( -1 - სტრიქონის ბოლო ელემენტი,რადგან ათვლა 0 დან იწყება).

while i<j:
    while not user_input[i].isalnum() and i<j: # i -თუ არ არის ალფანუმერული და სტრინგის ფარგლებშია გავაგრძელო კითხვა სწორი მიმართულებით
        i+=1
    while not user_input[j].isalnum()and i<j:  # j -თუ არ არის ალფანუმერული და სტრინგის ფარგლებშია გავაგრძელო კითხვა რევერსით
        j-=1
    if user_input[::1] != user_input[::-1] and user_input[i].lower() != user_input[j].lower():
        print("Is not palindrome")
        break
    if  user_input[::1] == user_input[::-1] and user_input[i].lower()==user_input[j].lower(): #თუ ჩემი სტრიქონი არის პალინდრომი, ანუ ასოები ემთხვევა და ქეისებს ვუგულველყოფ,ვაგრძელებ კითხვას
        i+=1
        j-=1
    print ("Is palindrome")
    break
