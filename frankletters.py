import sys
import random
from pyfiglet import Figlet
def main():
    figlet= Figlet()

    if len(sys.argv)==1:
        figlet.setFont(font=random.choice(figlet.getFonts()))

    elif len(sys.argv)==3:
        if sys.argv[1] not in ["-f","--font"]:
            sys.exit("Invalid usage")

        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid font")

        figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    text= input("input: ")
    print(figlet.renderText(text))

main()
        

