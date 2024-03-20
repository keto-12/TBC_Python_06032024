#Task 1.
# პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
# დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო,
# გარდა "e"- სიმბოლოსი.

user_input=input("Please, enter a word:")

for c in range (len(user_input)):
    if c % 2 ==0 and user_input[c]!="e":
        print (user_input[c],end=" ")
