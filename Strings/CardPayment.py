def CardPayment(Card):
    if len(Card) == 19:
            return Card[15:]
    else: return 'Invalid Card'

CardNumber = input('Enter the card number: ')
stars = '*' * 4 + ' '


print('Card Details:',stars * 3 + CardPayment(CardNumber))
