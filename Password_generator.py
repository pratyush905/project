import string
import random

def generate_password(min_len , num = True , special_char = True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
    characters = letters
    if num:
        characters+= digits
    if special_char:
        characters+= special
        
    pwd = ""
    meets_criteria = False
    has_num = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_len:
        new_char = random.choice(characters)
        pwd += new_char
        
        if new_char in digits:
            has_num = True 
        elif new_char in special:
            has_special = True 
            
        meets_criteria = has_num and has_special
        if num:
            meets_criteria = has_num
        if special_char:
            meets_criteria = meets_criteria and has_special
        
    return pwd

min_len = int(input("Enter the minimum length of password required: "))
has_num = input("Do you require numbers in the password? (y/n): ").lower() == 'y'
has_special = input("Do you require special characters in the passwors? (y/n): ").lower() == 'y'
pwd = generate_password(min_len , has_num , has_special)
print("Password suggested : " , pwd)

        
        