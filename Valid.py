'''email=input("what's your email? ").strip()

username, domain=email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")'''

import re

email=input("what's your email? ").strip()

#if re.search(r"^.+@.+\.edu$",email):#.indicated any character
#if re.search(r"^[^@]+@[^@]+\.edu$",email):
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$",email):
#if re.search(r"^(\w|\s)+@\w+\.(com|edu|gov|)$",email):
#if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
    print("valid")
else:
    print("Invalid")

#\d - decimal digit
#\D - not a decimal digit
#\s - whitespace characters
#\S-not whitespace characters
#\w -word character as well number and underscore 
#\W not wa word character 





