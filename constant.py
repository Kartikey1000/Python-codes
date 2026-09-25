'''class Cat:
    meows=3

    def meow(self):
        for _ in range(Cat.meows):
            print("Meow")
cat=Cat()
cat.meow()
'''


def meow(n: int) -> str:
    
    return "meow\n"* n

number: int=int(input("Number: "))
meows: str =meow(number)
print(meows,end="")