import string
import random


symbols = list(string.ascii_letters)


card1 = [0] * 5
card2 = [0] * 5
pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
print("Position 1:", pos1)
print("Position 2:", pos2)

samesymbol = random.choice(symbols)
symbols.remove(samesymbol)


card1[pos1] = samesymbol
card2[pos1] = samesymbol


if pos1 != pos2:
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos2] = random.choice(symbols)
    symbols.remove(card2[pos2])

for i in range(5):
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2


print("Card 1: ", "".join(random.sample(card1, len(card1))))
print("Card 2: ", "".join(random.sample(card2, len(card2))))


ch = input('Spot the similar symbol: ')
if ch == samesymbol:
    print('Correct!')
else:
    print('Incorrect, the correct symbol was:', samesymbol)
