def main():
    history=[]

    while True:
        actions=input("Action: ")
        if actions=="Undo":
            undone=history.pop()
            print(f"Undone:{undone}")
        elif actions=="Restart":
            history.clear()
        else:
            history.append(actions)
        print(history)
main()