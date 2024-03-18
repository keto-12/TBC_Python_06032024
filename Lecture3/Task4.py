#Task4
#დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს,
# როცა მომხმარებელმა იყიდა ბიტკოინი,
# ასევე მიიღებს დოლარში თანხას, რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად
# და ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა
# დღევანდელი ფასის გათვალისწინებით. იხ module forex-python

import datetime

from forex_python.bitcoin import BtcConverter
b = BtcConverter() # force_decimal=True to get Decimal rates

year_bought = int(input(" Please enter the year you bought a bitcoin:"))
if year_bought <= 2014:
    print(int(input("Please enter a valid year that is the year after 2014:")))
    exit(1)
month_bought = int(input("Please enter the month you bought a bitcoin:"))
if month_bought <1 or month_bought >12:
    print(int("Please enter the correct month you bought a bitcoin That is number between 1 and 12:"))
    exit(1)
day_bought =int(input("Please enter the day you bought a bitcoin :"))
if day_bought <1 or day_bought>31:
    print(int(input("Please, enter a valid day that is between 1 and 31:")))

date_bought= datetime.datetime(year_bought, month_bought, day_bought)
print(date_bought)

amount_paid=float(input("How much have you paid for a bitcoin :"))
print(amount_paid)

purchase_price = b.get_previous_price('USD',date_bought)
print(purchase_price)

latest_rate=b.get_latest_price("USD")
print(latest_rate)


purchased_volume = amount_paid/purchase_price #აქაა შეცდომა

if (purchased_volume * latest_rate) - (purchased_volume * purchase_price) > 0:
    print(f"Your profit is ${(purchased_volume * latest_rate) - (purchased_volume * purchase_price)}")
else:
    print(f"Your loss is ${(purchased_volume * latest_rate) - (purchased_volume * purchase_price)}")

