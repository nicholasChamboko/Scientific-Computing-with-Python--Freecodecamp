"""
    This algorithm is used to validate a variety of identification numbers
"""
def main():
    card_number = '4111-1111-4555-1142'

    #maketrans method replaces characters in a string eg. - will be replaced with nospace and space will be replaced with no space as well
    card_translation = str.maketrans({'-' : '', ' ':''})

    #translating the card number using the specified translation
    translated_card_number  = card_number.translate(card_translation)

    print(translated_card_number)

main()
