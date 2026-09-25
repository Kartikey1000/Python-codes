from datetime import date
import sys
import inflect

def main():
    birth_date= get_birth_date()

    today=date.today()
    difference =today -birth_date

    minutes= difference.days *24*60

    p=inflect.engine()
    words = p.number_to_words(minutes,andword="")

    print(words.capitalize(),"minutes")

def get_birth_date():
    try:
        year,month,day= input("Dat of Birth: ").split("-")
        birth_date = date(int(year),int(month),int(day))
        return birth_date
    except (ValueError,TypeError):
        sys.exit("Invalid date")

if __name__=="__main__":
    main()