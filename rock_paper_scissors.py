def rock_paper_scissors():
    rounds = random.randint(1, 5)
    print(f"We will make a competition of {rounds} rounds. The computer chosed so ")
    x = 0
    pointu = 0
    pointc = 0
    print(f"We start with computer : {pointc} to you : {pointu}")
    while x != rounds :
        turn = random.choice('rps')
        your_turn = input("Chose between rock(r), paper(p) or scissors(s) : ").lower()
        if turn == 'r' and your_turn == 's' or turn == 's' and your_turn == 'p' or turn == 'p' and your_turn == 'r' :
            pointc += 1
            print(f"You played {your_turn} and the computer played {turn}. \nThe computer gains one point. It is now {pointc} to {pointu}")
        elif your_turn == 'r' and turn == 's' or your_turn == 's' and turn == 'p' or your_turn == 'p' and turn == 'r' :
            pointu += 1
            print(f"You played {your_turn} and the computer played {turn}. \nYou gain one point. It is now {pointc} to {pointu}")
        else :
            print("You played {your_turn} and the computer played {turn}. \nIt's a tie. No points")
        x += 1
    if pointc > pointu :
        print(f"The computer wins with {pointc} points over {rounds} rounds") 
    elif pointu > pointc :
        print(f"You win with {pointu} points over {rounds} rounds")
    else :
        print(f"It's a tie over {rounds} rounds")
rock_paper_scissors()       