#Task2
# ლექციაზე განხილული პაროლის შემოყვანის ამოცანა
# გადაჭერით for ციკლის გამოყენებით

DB_PASSWORD ="Georgia"
MAX_TRIES=3

for i in range (1,MAX_TRIES+1):
    input_password = input("Please enter password:")
    if (input_password == DB_PASSWORD and i<=3):
        print("Hello from Georgia")
        break
    elif (input_password != DB_PASSWORD and i<= 3):
        print("Please input correct password")

if (input_password != DB_PASSWORD and i>=3):
    print("You are blocked")
