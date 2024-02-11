"""
    This algorithm is used to validate a variety of identification numbers
"""
def main():
    card_number = '4111-1111-4555-1142'

#maketrans method replaces characters in a string
nick = 'ticholas'

print(nick)
trs = str.maketrans({'t':'c','l':'b'})
translated_string = nick.translate(trs)
print(translated_string)
