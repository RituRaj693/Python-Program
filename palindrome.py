string = input('enter the string :')
reverse_string = string[::-1]
if string == reverse_string:
    print('it is palindrome :',reverse_string)
else:
    print('it is not palindrome :',reverse_string)
