def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special = "!@#$%^&*()"

    for char in password:
        if char.islower():
            has_lower=True
        if char.isupper():
            has_upper=True
        if char.isdigit():
            has_digit=True
        if char in special:
            has_special=True
    score=0
    if len(password)>8:
        score+=1
    if has_lower:
        score+=1
    if has_upper:
        score+=1
    if has_digit:
        score+=1
    if has_special:
        score+=1

    if score==5:
        return "Strong"
    elif score>=3:
        return "Moderate"
    else:
        return "Weak"

print(check_password_strength("Hello123!"))   # Strong
print(check_password_strength("Hello123"))    # Moderate
print(check_password_strength("hello"))  


