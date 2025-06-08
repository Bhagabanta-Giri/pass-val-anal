def is_spl(x):
    if x.isalnum():
        return False
    else:
        return True

pw = input()
alpha = 0
num = 0
spl = 0

lvl = 0


#Validator is here
if len(pw) >= 7:
    lvl += 1
if any(ch.isdigit() for ch in pw):
    lvl += 1
if any(ch.isupper() for ch in pw):
    lvl += 1
if any(ch.islower() for ch in pw):
    lvl += 1
if any(is_spl(ch) for ch in pw):
    lvl += 1



#Analysis is here
for ch in pw:
    if ch.isdigit():
        num += 1
    elif ch.isalpha():
        alpha += 1
    elif is_spl(ch):
        spl += 1

print("Your Password Statistics:")
print("Alphabets:", str(alpha))
print("Numbers:", str(num))
print("Special Chracters (including spaces):", str(spl))


print("Your Password Rating:")
if lvl == 1:
    print("Very Weak")
elif lvl == 2:
    print("Weak")
elif lvl == 3:
    print("Average")
elif lvl == 4:
    print("Strong")
elif lvl == 5:
    print("Very Strong")
else:
    print("Wait...is that even a password?")