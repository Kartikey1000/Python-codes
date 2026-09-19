def main():
    with open("Alice.txt","r") as f:#read te file R to write there is #w
        contents=f.read()

    #print(contents) to get all content
    chapter1=contents[52:272] #to get exact data 
    #print(chapter1[0])
    with open("chapter1.txt","w") as f:
        f.writelines(chapter1)
        

main()