i=1
while i<=3:
    print("mewo")
    i=i+1 #or i+=1


i=3
for i in range(3):
    print("mewo")

print("meow\n"*3,end="")

while True:
    n=int(input("What's n? "))
    if n>0:
        break
for i in range(n):
    print("meow")



def main():
    number= get_number()
    meow(number)

def meow(n):
    for i in range(n):
        print("meow")

def get_number():
    while True:
        n=int(input("what the n? "))
        if n >0:
            break
    return n 
main()
    