def intro():    
    print("    THE  FINAL  COUNTDOWN    ")
    print("We were in the locker room,It was 6:45 and the game of our lives at home (PPG Paints Area) aginst the capitals a division rival, it decided if we would advance to the playoffs.")
    print("We were sitting there in the freezing locker room waiting for our names to come running through the announcers mic. ")
    print("Then with the cheer of the crowd we heard names being called,they called my name, Please Welcome Blake Tillman")
    print("As soon as it came through I frozed in place, I was the most nervous I had ever been for a game even for being a rookie that year")
    print("I skated out on the ice and the game had begun")
    option1 = input(" Get the puck ,  Give the puck off")

    if option1 == "Get the puck":
        print("We had won the puck drop for the first period, my teammate Johnny Woo passed to me and I hit a slapshot for the first goal")
        print("We were up 1-0 within the first 2 minutes with 18 to go and things were off to a good start")
        drop()
    if option1 == "Give the puck off":
        print("They won the puck drop and chewed clock keeping the puck mostly on are side of the ice for about 4 minutes and then scored, they were up 1-0")
        scoredon()


def drop():
    print("We had won the puck drop again and Johnny passed to me and with a swift thought I")
    option2 = input("Go for the goal, pass it off")

    if option2 == "Go for the goal":
        print("shot the puck and missed and they took it for a breakaway they missed the first shot but played good defense and ended up scoring a couple minutes later , we were tied 1-1.")
        print)"After that the game went back and forth from one side of the ice to the other and no one scored again that period"

    if option2 == "pass it off":
        print("I passed it to other teammate Szander, are center. He took the shot and made it we were up 2-0 ")
        print)"After that the game went back and forth from one side of the ice to the other and no one scored again that period"

        


def scoredon():
    print("There was one thing that went are way though, My teammate johnny won the puck drop this time")
    print("He passed to me and with a swift though I")
    if option2 == "Go for the goal":
        print("shot the puck and missed and they took it for a breakaway, they missed the first shot but played good defense and ended up scoring a couple minutes later, we were down 2-0.")
        print)"After that the game went back and forth from one side of the ice to the other and no one scored again that period"


    if option2 == "pass it off":
        print("I passed it to other teammate Szander, are center. He took the shot and made it we were tied 1-1")
        print)"After that the game went back and forth from one side of the ice to the other and no one scored again that period"

    
intro()

