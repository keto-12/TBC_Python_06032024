#Task3
#დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n,
# სადაც 0 < n < 50. Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე
#სიმბოლოებით *,  /, | და \ . Მაგალითად n = 4
n=int(input("Please enter a size of the christmas three between 0 and 50:"))
if n <0 or n >50:
    print("Please enter a number between 0 and 50")
for i in range (n):
    #line=(("/ "*(i+1))+"|"+(i*2+1)*"*")
    #line = (("/ " * (n - i)) + "|" + (i * 2 + 1) * " \ ")
    line = (("/ " * (i)) + "|" + (i * 2 + 1) * " \ ")
    #line = (("/ " * (i*2+1)) + "|" + (i * 2 + 1) * " \ ")
    print(line)


