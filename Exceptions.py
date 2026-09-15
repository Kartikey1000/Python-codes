'''try:
    x=int(input("What's X? "))
    print(f"x is {x}")

except ValueError:
    print("xi is not a integer")


try:
    x=int(input("What's X? "))
except ValueError:
    print("xi is not a integer")
else:
    print(f"x is {x}")

while True:
    try:
        x=int(input("What's X? "))
    except ValueError:
        print("xi is not a integer")
    else:
        break

print(f"x is {x}") 
'''
def main():
    x= get_in()
    print(f"x is {x}") 


def get_in():
    while True:
        try:
            return int(input("What's X? "))
        except ValueError:
            print("xi is not a integer") #we can use the pass if not want to print statement
        
main()