import random

deck = ['2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'Jack' , 'Queen' , 'King' , 'Ace']

point_values = {'2':2 , '3':3 , '4':4 , '5':5 , '6':6 , '7':7 , '8':8 , '9':9 , '10':10 , 'Jack':10 , 'Queen':10 , 'King':10 , 'Ace':11}

dealer = []
player1 = []
player1_stack = 100



#draws a random card and appends that card to the list of a player's hand.
def draw_card(x):
    new_card = random.choice(deck)
    x.append(new_card)

#will deal cards at the beginning of the round
def deal_cards():
    i = 1
    while i < 3:
        draw_card(dealer)
        draw_card(player1)
        i = i + 1

#checks the point total of a player
def check_points(x):
    total_points = 0
    for i in x:
        total_points = total_points + point_values[i]
    if total_points > 21 and 'Ace' in x:
        point_values['Ace'] = 1
        total_points = 0
        for i in x:
            total_points = total_points + point_values[i]
        point_values['Ace'] = 11
    else:
        return total_points
    return total_points


#checks whether a player has gone over 21
def check_bust(x):
    if check_points(x) > 21:
        return True
    else:
        return False

#checks for win
def check_win(x):
    if check_points(x) == 21:
        return True
    else:
        return False

#asks for the player's move
def player_move():
    move = raw_input("Hit or stand? Enter 'hit' for hit and 'stand' for stand: ")
    if move == 'hit':
        draw_card(player1)
        print ('You hit.')
        return False
    elif move == 'stand':
        print ('You stood.')
        return True
    else:
        move = raw_input("Please enter either 'hit' or 'stand': ")
        if move == 'hit':
            print ('You hit.')
            draw_card(player1)
            return False
        else:
            print ('You stood.')
            return True

#determines whether computer hits or stands
def computer_move():
    if check_points(dealer) < 17:
        draw_card(dealer)
        print ('Dealer hit.')
        return False
    elif check_points(dealer) > 21 and check_points(dealer) > 16 and 'Ace' in dealer:
        print('Dealer stood.')
        return True
    elif check_points(player1) > check_points(dealer):
        draw_card(dealer)
        print ('Dealer hit.')
        return False
    else:
        print ('Dealer stood.')
        return True


#prints all hands
def print_board():
    print ("Dealer's hand: FACE DOWN CARD , {0}".format(dealer[1:]))
    print ("Your hand: {0}".format(player1))

#prints board with dealer's full hand
def print_board_up():
    print ("Dealer's hand:")
    for i in dealer:
        print (i)
    print ("Player 1's hand: ")
    for i in player1:
        print (i)

#clears hands
def clear_board():
    global dealer
    global player1
    dealer = []
    player1 = []

#takes player's bet
def player_bet():
    global player1_stack
    global bet
    bet = int(raw_input("You currently have {0} chips in your stack. How much will you bet? ".format(player1_stack)))
    while bet > player1_stack or bet < 1:
        bet = int(raw_input("Please bet a value less than {0} and more than 0. How much will you bet? ".format(player1_stack + 1)))
    player1_stack = player1_stack - bet


#main loop
while True:
    if player1_stack > 0:
        print ("NEW ROUND:")
        player_bet()
        deal_cards()
        print_board()
        while True:
            player1_stands = 0
            if check_win(player1) == True:
                if bet % 2 == 0:
                    print('Your hand is a natural, you win {0} chips.'.format(bet * 1.5))
                    player1_stack = player1_stack + 1.5 * bet
                else:
                    print('Your hand is a natural, you win {0} chips.'.format(bet * 1.5 + 0.5))
                    player1_stack = player1_stack + 1.5 * bet + 0.5
                clear_board()
                break
            if player_move() == True:
                player1_stands = player1_stands + 1
            if check_bust(player1) == True:
                print_board()
                print ("Your hand is a bust, you lose.")
                clear_board()
                break
            if check_win(player1) == True:
                print_board()
                print ('You have 21, you win {0} chips. '.format(bet * 2))
                player1_stack = player1_stack + 2 * bet
                clear_board()
                break
            print_board()
            if player1_stands > 0:
                computer_stands = 0
                while computer_stands == 0:
                    if computer_move() == True:
                        computer_stands = computer_stands + 1
                    print_board()
                    if check_bust(dealer) == True:
                        print_board_up()
                        print ("Dealer's hand is a bust, you win {0} chips.".format(bet * 2))
                        player1_stack = player1_stack + 2 * bet
                        clear_board()
                        break
                    if check_win(dealer) == True:
                        print_board_up()
                        print ('Dealer has 21, you lose.')
                        clear_board()
                        break
                if computer_stands > 0:
                    if check_points(dealer) < check_points(player1):
                        print_board_up()
                        print ('Your hand is closer to 21, you win {0} chips.'.format(bet * 2))
                        player1_stack = player1_stack + 2 * bet
                        clear_board()
                        break
                    elif check_points(dealer) > check_points(player1):
                        print_board_up()
                        print ("Dealer's hand is closer to 21, you lose.")
                        clear_board()
                        break
                    else:
                        print_board_up()
                        print ("You and dealer tie, it's a push.")
                        player1_stack = player1_stack + bet
                        clear_board()
                        break
                    break
                break
    else:
        print('You ran out of chips. Game over.')
        break