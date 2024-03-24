#Task2
#2.	დაწერეთ პროგრამა რომელიც მიიღებს ორ სტიქონს.
# Პროგრამამ უნდა შეამოწმოს არის თუ არა შესაძლებელი ერთი სტრიქოქნის სიმბოლოების გამოყენებით მეორე სტრიქონის მიღება.
# მაგალითი 1.
# 	Input:
# 	listen
# 	silent
# 	Output: YES
# მაგალითი 2.
# 	Input:
# 	a gentleman
# 	elegant man
# 	Output: YES
# მაგალითი 3.
# 	Input:
# 	dormitory
# 	dirty room
# 	Output: NO
# მაგალითი 4.
# 	Input:
# 	election
# 	collection
# 	Output: NO

user_input_1 = input("Please enter a string:")
user_input_2 =input("Please enter the second string:")

#ვარიანტი N 1
if len(user_input_1)==len(user_input_2) and user_input_1.isalnum()==user_input_2.isalnum() and user_input_1.isspace()==user_input_2.isspace():
    print("YES")
else:
    print("NO")

# ვარიანტი N2

if len(user_input_1)==len(user_input_2) and set(user_input_1).issubset(set(user_input_2)):
    #ვამოწმებ სტრიქონის სიგრძით და პირველის სეთი მეორის საბსეთია
    print("YES")
else:
    print("NO")
