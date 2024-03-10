#Lecture2_Task3
# Დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს.
# Პროგრამამ უნდა დაბეჭდოს ყველა ყველა მარტივი გამყოფი ერთ ხაზზე.
# Შემოსული რიცხვის მაქსიმალური მნიშვნელობა უნდა იყოს 10.
# Მაგალითი: თუ პროგრამას გადავეცით 6, გამოსავალზე უნდა დაიბეჭდოს 2, 3.
# ახსნა: 6 იყოფა 2-ზეც და 3-ზეც. 2 და 3 არის მარტივი რიცხვები.
# Დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.

number=int(input("Please, enter a positive integer with the maximum possible value of ten:"))
PRIME_DEVISOR_2=2
PRIME_DEVISOR_3=3
PRIME_DEVISOR_5=5
PRIME_DEVISOR_7=7
PRIME_DEVISOR_9=9
if number<=0:
    print("Enter a positive integer with the maximum possible value of ten ")
if number==1:
    print("Number does not have prime devisors")
if number>1 and number<=10:
    if number==2 or number==4 or number==8:
        print(PRIME_DEVISOR_2)
    elif number==3 or number==9:
        print(PRIME_DEVISOR_3)
    elif number==5:
        print(PRIME_DEVISOR_5)
    elif number==6:
        print(PRIME_DEVISOR_2,PRIME_DEVISOR_3)
    elif number==7:
        print(PRIME_DEVISOR_7)
    else:
        print(PRIME_DEVISOR_2,PRIME_DEVISOR_5)
if number>10:
    print("Enter a positive integer with the maximum possible value of ten ")
