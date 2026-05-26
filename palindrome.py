def check_palindrome(str):

    clean_string = (str.replace(" ","")).lower()
    reverse_string = clean_string[::-1]
    
    return clean_string==reverse_string


str = input("Enter the string : ")
if check_palindrome(str):
    print("It is a palindrome")
else:
    print("Not a palindrome")

