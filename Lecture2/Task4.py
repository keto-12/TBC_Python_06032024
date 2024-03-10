#Lecture2_Task4
#ვცადე ცვლადები დისქრიპთივ გამეხადა -ამ მცდელობაში ძალიან გრძელი სახელები ხომ არ გამომივიდა?
# Დაწერეთ პროგრამა რომელიც არგუმენტად მიიღებს მანქანის სიჩქარეს,
#განსაზღვრავს მისი სიჩქარის კატეგორიას და დაბეჭდავს ეკრანზე.
#Სიჩქარის კატეგორიები განისაზღვრება შემდეგნაირად.
#Თუ ავტომობილის სიჩქარე 30 კმ/სთ-ზე ნაკლებია, მისი კატეგორიაა - SLOW.
#Როცა ავტომობილის სიჩქარე  120 კმ/სთ-ზე მეტია, მისი კატეგორიაა - VERY FAST.
#Თუ ავტომობილის სიჩქარე მეტია 60 კმ/სთ-ზე, მისი კატეგორიაა - FAST.
#Ხოლო თუ ავტომობილის სიჩქარე მეტია 30 კმ/სთ-ზე, მისი კატეგორიაა - MODERATE.
#(თუ ავტომობლი ხვდება ორ კატეგორაიში, უნდა შეირჩეს უფრო სწრაფი კატეგორია)

car_speed=int(input("Please, write a speed of a car in the range from 5 to 300 km/h:"))
car_speed_category_less_than_or_equel_to_30="slow"
car_speed_category_more_than_30_and_less_or_equel_to_60="moderate"
car_speed_category_more_than_60_and_less_than_or_equel_to_120="fast"
car_speed_category_more_than_120="very fast"

if car_speed<=30:
    print(car_speed_category_less_than_or_equel_to_30)
elif car_speed>30 and car_speed<=120:
    if car_speed<=60:
       print(car_speed_category_more_than_30_and_less_or_equel_to_60)
    else:
       print(car_speed_category_more_than_60_and_less_than_or_equel_to_120)
else:
    print(car_speed_category_more_than_120)
