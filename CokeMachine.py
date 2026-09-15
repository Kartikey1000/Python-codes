def main():
    Amount=50

    while Amount>0:
        print("Amount Due: ",Amount)
        coin=int(input("Insert Coin: "))

        if coin==25 or coin==10 or coin==5:
            Amount -= coin


    print("Change Owed: ",abs(Amount))

    
    
main()