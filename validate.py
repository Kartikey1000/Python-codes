import re 
name= input("what's your name? ").strip()

matches= re.search(r"^(.+), *(.+)$",name)

if matches:
    name =matches.group(2)+" "+ matches.group(1)
#    last,first=matches.groups()
#    name= f"{first} {last}"

print(f"hello,{name}")