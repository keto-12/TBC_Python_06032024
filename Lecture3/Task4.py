#Task4
#დაწერეთ პროგრამა რომელიც მიიღებს წელს, თვეს და დღეს,
# როცა მომხმარებელმა იყიდა ბიტკოინი,
# ასევე მიიღებს დოლარში თანხას, რომელიც შემოყვანილ თარიღში გადაიხადა ბიტკოინის შესაძენად
# და ეკრანზე გამოიტანს დოლარში თანხას რომელიც მოიგო ან დაკარგა
# დღევანდელი ფასის გათვალისწინებით. იხ module forex-python

import requests

date_bought=str(input("What date have you bought bitcoins.e.g.2020-12-31:"))