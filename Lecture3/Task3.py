#Task3
#3.	დაწერეთ პროგრამა რომელიც გაშვებისას
# დაბეჭდავს:
#ბანქოს შემთხვევით მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა:
#4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠))
#და 13 მნიშვნელობა (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))

import random

card_colors = "♣", "♦", "♥", "♠"
card_values = 2, 3, 4, 5, 6, 7, 8, 9, 10,"J","Q", "K", "A"

def random_card():
     card_color = random.choices(card_colors)
     card_value = random.choices(card_values)
     return (f" {card_color}, {card_value} ")
print(random_card())

