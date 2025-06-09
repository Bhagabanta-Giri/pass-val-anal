import string
from random import randint, choice, shuffle

def is_spl(x):
    if x.isalnum():
        return False
    else:
        return True

print("Choose Password Type:")
print("Very Weak: 1")
print("Weak: 2")
print("Average: 3")
print("Strong: 4")
print("Very Strong: 5")
print("I don't want a password: 0")

proper = {1, 2, 3, 4, 5}
ch_chest = []
password = []
num = 0
alpha = 0
spl = 0

def lvl_input():
    try:
        lvl = int(input())
        if lvl not in range(6):
            raise ValueError
        return lvl
    except ValueError:
        print(".....You had 1 job. Enter a valid input!")
        return lvl_input()

def length_of_pw():
    try:
        length = int(input("What should be the length of your password? (min. = 7)"))
        if length < 7:
            raise ValueError
        return length
    except ValueError:
        print("Enter a valid input")
        return length_of_pw()

lvl = lvl_input()

if lvl == 1:
    req = input("Do you want an alphabetic password? (Y/N)").upper()
    if req.startswith("Y"):
        case = input("Uppercase or Lowercase? (U/L)").upper()
        if case.startswith("U"):
            ch_chest.extend(string.ascii_uppercase)
        else:
            ch_chest.extend(string.ascii_lowercase)
    else:
        ch_chest.extend(string.digits)

elif lvl == 2:
    req = input("Do you want a purely alphabetic password? [Y/N]").upper()
    if req.startswith("Y"):
        password.append(choice(string.ascii_lowercase))
        password.append(choice(string.ascii_uppercase))
        ch_chest.extend(string.ascii_letters)
    else:
        case = input("For any alphabet in your password, should it be upper or lower case? [U/L]").upper()
        if case.startswith("U"):
            ch_chest.extend(string.ascii_uppercase)
            password.append(choice(string.ascii_uppercase))
        else:
            ch_chest.extend(string.ascii_lowercase)
            password.append(choice(string.ascii_uppercase)) 
        ch_chest.extend(string.digits)
        password.append(choice(string.digits)) #2 here

elif lvl == 3:
    req = input("Do you want special characters in your password? [Y/N]").upper()
    if req.startswith("Y"):
        ch_chest.extend(string.punctuation)
        password.append(choice(string.punctuation))
        case = input("For any alphabet in your password, should it be upper or lower case? [U/L]").upper()
        if case.startswith("U"):
            ch_chest.extend(string.ascii_uppercase)
            password.append(choice(string.ascii_uppercase))
        else:
            ch_chest.extend(string.ascii_lowercase)
            password.append(choice(string.ascii_lowercase)) #2 here
    else:
        ch_chest.extend(string.digits)
        password.append(choice(string.digits))
        ch_chest.extend(string.ascii_letters)
        password.append(choice(string.ascii_uppercase))
        password.append(choice(string.ascii_lowercase)) #3 here

elif lvl == 4:
    ch_chest.extend(string.ascii_letters)
    ch_chest.extend(string.digits)
    ch_chest.extend(string.punctuation)
    password.append(choice(string.ascii_uppercase))
    password.append(choice(string.ascii_lowercase))
    password.append(choice(string.digits))
    password.append(choice(string.punctuation))

elif lvl == 5:
    length = length_of_pw()
    ch_chest.extend(string.ascii_letters)
    ch_chest.extend(string.digits)
    ch_chest.extend(string.punctuation)
    password.append(choice(string.ascii_uppercase))
    password.append(choice(string.ascii_lowercase))
    password.append(choice(string.digits))
    password.append(choice(string.punctuation))

else:
    ch_chest.extend(" ")

if lvl != 5:
    range_of_pw = randint(0,3)    
    for i in range(range_of_pw):
        password.extend(choice(ch_chest))
else:
    for i in range(length):
        password.extend(choice(ch_chest))

password_final = shuffle(str("".join(password)))

print("Your Password is:", password_final)

if lvl not in proper:
    print("Its empty....Just like your brain!")
else:
    for ch in password_final:
        if ch.isdigit():
            num += 1
        elif ch.isalpha():
            alpha += 1
        elif is_spl(ch):
            spl += 1
        
    print("Your Password Statistics:")
    print("Alphabets:", str(alpha))
    print("Numbers:", str(num))
    print("Special Characters (including spaces):", str(spl))