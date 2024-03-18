# Task1
# გადაჭერით მეხუთე დავალების მეორე ამოცანა while ციკლის გამოყენებით
# 2.	დაწერეთ პროგრამა რომელიც დაბეჭდავს გამრავლების ტაბულას 1 და 9 ის ჩათვლით.
# ტაბულა უნდა იყოს სვეტებად შედგენილი. ყოველ მომდევნო სვეტში არ უნდა
# იყოს გამეორებული ნამრავლი წინა სვეტიდან. Გავიხილოთ 1x3 ის მაგალითი
# 1 * 1 = 1
# 1 * 2 = 2     2 * 2 = 4
# 1 * 3 = 3     2 * 3 = 6     3 * 3 = 9
# print("\n")

# Nested While Loop (Left-to-Right Format)
row = 1
while row <= 10:
     col = 1
     while col <= row:
         result = col * row
         print(f"{col} x {row} = {result}", end="\t")
         col += 1
     print()  # Move to the next line for the next row
     row += 1

