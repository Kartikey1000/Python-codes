def main():
    grocery=set()

    while True:
        try:
            item=input().upper()
            grocery.add(item)

        except EOFError:
            break

    for item in sorted(grocery):
        print(item)


main()
