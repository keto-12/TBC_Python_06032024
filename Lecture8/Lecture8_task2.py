#Task2.	პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ
# თანხმოვანი ასოები.

user_input= input("Please, enter a word:")

for i in user_input:
    if i!="a" and i!="u" and i!="y" and i!="o" and i!="i" and i!="e":
        print(i, end=" ")
