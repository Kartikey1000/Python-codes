def main():
    names=["Mario","luigi","Daisy","Yoshi"]
    for i in range(len(names)):
        print(write_letter(names[i],"Princess peach"))

def write_letter(reciever,sender):
    return f"""
==================================
Dear {reciever},
You are invited!

Sincerely,
{sender}

==================================

"""

main()