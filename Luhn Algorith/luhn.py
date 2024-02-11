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
    
    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_even_digits + sum_of_odd_digits
    print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'

    #maketrans method replaces characters in a string eg. - will be replaced with nospace and space will be replaced with no space as well
    card_translation = str.maketrans({'-' : '', ' ':''})

    #translating the card number using the specified translation
    translated_card_number  = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('Valid Card')
    else:
        print('Invalid Card')

main()
