"""
    Building a case converter program between camelCase to snake_case and PascalCase to snake_case
"""

def convert_to_snake_case(pascal_or_camel_cased_string):
    """
        Function to comvert a string to snake case
    """
    #using list comprehension to append to list
    snake_case_char_list = [
        #Append an underscore and lowercased ver of char if the char is in uppercase
        '_' + char.lower() if char.isupper()
        else char
        #object we are will actually iterate upon
        for char in pascal_or_camel_cased_string
    ]
    #Return joined characters in the list as a string
    return ''.join(snake_case_char_list).strip('_')

def main():
    print(convert_to_snake_case('NicholasChamboko'))

if __name__ == '__main__':
    main()