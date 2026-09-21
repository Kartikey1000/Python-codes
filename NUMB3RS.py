import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$",ip)

    if not match :
        return False

    for number in match.groups():
        if int(number)>225:
            return False

    return False

if __name__=="__main__":
    main()
