def main():
    Difficulty=input("Difficult or Casual?")
    if not (Difficulty=="Difficult"or Difficulty=="Casual"):
        print("Enter a valid Difficulty")
        return
    Player=input("Multiplayer or Single-player?")
    if not (Player=="Multiplayer"or Player=="Single-player"):
        print("Enter a valid number of player")
        return

    if Difficulty=="Difficult" and Player=="Multiplayer":
        recommend("PUBG")
    elif Difficulty=="Difficult" and Player=="Single-player":
        recommend("Snake game")
    elif Difficulty=="Casual" and Player=="Multiplayer":
        recommend("Ludo")
    else:
        recommend("Bhar jaake khelo")

def recommend(game):
    print("You might like",game)

main()
