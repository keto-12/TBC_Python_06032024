#Task 3
#პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, პირველი და შუა ასოები 5-ჯერ while ლუპით.
# თუ შემოყვანილი ტექსტის ზომა არის ლუწი,მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო.

user_input =input("Please, enter a word:")

c=-1
length=len(user_input)

while c<= length:

    if  length%2!=0:
        if c==0 or c==int(length/2) or c==length-1 :
           print(user_input[c]*5, end=" ")
        c += 1

    if length%2==0:
        if c==0 or c==length/2 or c==length/2-1 or c==length-1:
            print(user_input[c]*5, end=" ")
        c+=1
