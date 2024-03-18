#Task2.
# დაწერეთ პროგრამა რომელიც მიიღებს 3 მნიშვნელობას:
# რომელ წელსაა დაბადებული ადამიანი, მერამდენე თვეშია დაბადებული
# და რა რიცხვშია დაბადებული.
# Შემდეგ კი ეკრანზე გამოიტანს კვირის
# რომელ დღესაა დაბადებული ადამიანი. იხ module datetime

import datetime

# date=str(input("Enter the date of your birth (for e.g.:09-02-2020): "))
# day, month, year = date.split('-')
# print(day,month,year)
# day_name = datetime.date(int(year), int(month), int(day))
# print("The Weekday of your birthday was {1}".format(date,day_name.strftime("%A")))

# date=str(input("Enter the date(day,month, year,for e.g.:09-02-2020): "))
# day_name= ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
# day = datetime.datetime.strptime(date, '%d-%m-%Y').weekday()
# print("The Weekday of your birthday was {1}".format(date,day_name[day]))

year_of_birth=int(input("What year were you born?:"))
month_of_birth=int(input("What month were you born? e.g.09:"))
date_of_birth=int(input("What date were you born e.g.05:"))
birth_date=datetime.date(year_of_birth,month_of_birth,date_of_birth)
print("The Weekday of your birthday was {1}".format(birth_date,birth_date.strftime("%A")))
