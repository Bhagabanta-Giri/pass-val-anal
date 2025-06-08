# Utility function to check if a character is special (non-alphanumeric)
def is_spl(x):
    if x.isalnum():
        return False
    else:
        return True

u_input = input()

if any(is_spl(x) for x in u_input):
    print(True)
else:
    print(False)