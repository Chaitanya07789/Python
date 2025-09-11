import re

def valide_email(email):
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}$'
    if re.match(pattern, email):
        return True
    else:
        return False
    

# Test emails
emails = [
    "user.name123@gmail.com",
    "username@domain",
    "user@domain.org",
    "user@domain.c"
]

for email in emails:
    print(F"{email} -> {'Valid' if valide_email(email) else 'Invalid'}")