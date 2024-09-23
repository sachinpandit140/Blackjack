from random import randint

var={1:[11,"an Ace"],2:[2,"a 2"],3:[3,"a 3"],4:[4,"a 4"],5:[5,"a 5"],6:[6,"a 6"],7:[7,"a 7"],
    8:[8,"an 8"],9:[9,"a 9"],10:[10,"a 10"],11:[10,"a Jack"],12:[10,"a Queen"],13:[10,"a King"]}
def main():
    print("-----------\nYOUR TURN\n-----------")
    card=user_game()
    print("-----------\nDEALER TURN\n-----------")
    dealer=dealer_game()
    print("-----------\nGAME RESULT\n-----------")
    if card>21:
        print("Dealer wins!")
    elif card==21 and dealer==21:
        print("Push.")
    elif card>dealer:
        print("You win!")
    elif card==dealer:
        print("Push.")
    else:
        print("Dealer wins!")
    
def card_name(c):
    return var[c][1]
def card_rank(c):
    return var[c][0]
def card_draw():
    card=randint(1,13)
    name=card_name(card)
    rank=card_rank(card)
    print(f"Drew {name}")
    return rank
def user_game():
    c1=card_draw()
    c2=card_draw()
    hand_value=c1+c2
    if hand_value==21:
        print("Final hand: 21.")
        print("BLACKJACK!")
        return 21
    elif hand_value==22:
        print("Final hand: 22.")
        print("BUST.")
        return 22
    else:
        yn=input(f"You have {hand_value}. Hit (y/n)? ").strip()
        while hand_value<21 and (yn=="y" or yn!="n"):
            if yn=="y":
                card=card_draw()
                hand_value+=card
                if hand_value>=21:
                    break
                yn=input(f"You have {hand_value}. Hit (y/n)? ").strip()
            elif yn!="n":
                print("Sorry I didn't get that.")
                yn=input(f"You have {hand_value}. Hit (y/n)? ").strip()
        if yn=="n":
            print(f"Final hand: {hand_value}.")
            if hand_value==21:
                print("BLACKJACK!")
            return hand_value
        if hand_value>21:
            print(f"Final hand: {hand_value}.")
            print("BUST.")
            return hand_value
        elif hand_value==21:
            print("Final hand: 21.")
            print("BLACKJACK!")
            return 21
        return hand_value

def dealer_game():
    c1=card_draw()
    c2=card_draw()
    hand_value=c1+c2
    if hand_value==21:
        print("Final hand: 21.")
        print("BLACKJACK!")
        return 21
    elif hand_value==22:
        print("Final hand: 22.")
        print("BUST.")
        return 22
    elif hand_value<17:
        print(f"Dealer has {hand_value}.")
        while hand_value<17 :
            card=card_draw()
            hand_value+=card
            if 17<=hand_value<=21:
                break
            print(f"Dealer has {hand_value}")
        if hand_value==21:
            print("BLACKJACK!")
            return hand_value
        elif hand_value>21:
            print(f"Final hand: {hand_value}.")
            print("BUST.")
            return hand_value
        else:
            print(f"Final hand: {hand_value}.")
            return hand_value
    else:
        print(f"Final hand: {hand_value}.")
        return hand_value
main()


        
                    


