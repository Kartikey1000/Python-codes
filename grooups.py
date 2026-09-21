import re
locations= {"+1":"US and Canda","+62":"Indone","+505":"NIC"}


def main():
    pattern= r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.search(pattern,number)
    if match:
        country_code=match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")


main()