def main():
    insert=input("Input: ")

    for i in insert:
        if i not in "aeiouAEIOU":
            output += i
    print("Output: ",output)
main()