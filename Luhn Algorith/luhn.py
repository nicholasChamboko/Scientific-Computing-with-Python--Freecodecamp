"""
    This algorithm is used to validate a variety of identification numbers
"""
def verify_card_number(card_number):
    sum_of_odd_digits = 0

    #Card numbers in reverse order
    card_number_reversed = card_number[::-1]

    #skipping one number of the card number
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    
    print(sum_of_odd_digits)

def main():
    card_number = '4111-1111-4555-1142'

    #maketrans method replaces characters in a string eg. - will be replaced with nospace and space will be replaced with no space as well
    card_translation = str.maketrans({'-' : '', ' ':''})

    #translating the card number using the specified translation
    translated_card_number  = card_number.translate(card_translation)

    verify_card_number(translated_card_number)

main()
