import random
import copy
art = """    
                      ___   ___   ___   ___   ___ 
                     |A  | |K  | |Q  | |J  | |10 |
                     |(`)| |(`)| |(`)| |(`)| |(`)|
                     |_\_| |_\_| |_\_| |_\_| |_\_|
                      ___   ___   ___   ___   ___   ___ 
                     |A  | |2  | |3  | |4  | |5  | |6  |
                     | /\| | /\| | /\| | /\| | /\| | /\|
                     |_\/| |_\/| |_\/| |_\/| |_\/| |_\/|
                      ___   ___   ___   ___   ___   ___   ___
                     |A  | |2  | |3  | |4  | |5  | |6  | |7  |
                     | ^ | | ^ | | ^ | | ^ | | ^ | | ^ | | ^ |
                     |(,)| |(,)| |(,)| |(,)| |(,)| |(,)| |(,)|
                                                                               
    ,---,.   ,--,                              ,-.                                    ,-.  
  ,'  .'  \,--.'|                          ,--/ /|                                ,--/ /|  
,---.' .' ||  | :                        ,--. :/ |    .--.                      ,--. :/ |  
|   |  |: |:  : '                        :  : ' /   .--,`|                      :  : ' /   
:   :  :  /|  ' |     ,--.--.     ,---.  |  '  /    |  |.    ,--.--.     ,---.  |  '  /    
:   |    ; '  | |    /       \   /     \ '  |  :    '--`_   /       \   /     \ '  |  :    
|   :     \|  | :   .--.  .-. | /    / ' |  |   \   ,--,'| .--.  .-. | /    / ' |  |   \   
|   |   . |'  : |__  \__\/: . ..    ' /  '  : |. \  |  | '  \__\/: . ..    ' /  '  : |. \  
'   :  '; ||  | '.'| ," .--.; |'   ; :__ |  | ' \ \ :  | |  ," .--.; |'   ; :__ |  | ' \ \ 
|   |  | ; ;  :    ;/  /  ,.  |'   | '.'|'  : |--'__|  : ' /  /  ,.  |'   | '.'|'  : |--'  
|   :   /  |  ,   /;  :   .'   \   :    :;  |,' .'__/\_: |;  :   .'   \   :    :;  |,'     
|   | ,'    ---`-' |  ,     .-./\   \  / '--'   |   :    :|  ,     .-./\   \  / '--'       
`----'              `--`---'     `----'          \   \  /  `--`---'     `----'             
                                                  `--`-'                                   
"""
cards = {
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [1, 11]
}

def user_card (num):
    res = random.sample(list(cards.items()), num)
    return res

def game ():
    print(art)
    user_consent = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if user_consent == 'n':
        return

    def game_play(val, hit_pass):
        user_player = [i[0] for i in user_card(val)]
        computer_player = [i[0] for i in user_card(val)]
        rand_list = [i for i in user_player if "A" != i]

        cur_value = 0

        if "A" in user_player and val == 2:
            # print(user_player)
            if user_player[0] == "A" and user_player[1] == "A":
                cur_value = cards["A"][1] + cards["A"][0]
            elif rand_list and rand_list[0].isalpha():
                cur_value = cards[rand_list[0]] + 11
            elif rand_list and int(rand_list[0]) + 11 > 21:
                cur_value = int(rand_list[0]) + 1
            else:
                cur_value = int(rand_list[0]) + 11
        else:
            for i in user_player:
                cur_value = cards[i]

        if hit_pass == "hit":
            computer_player = []
        elif hit_pass == "pass":
            user_player = []
        else:
            print(f"Your cards: {user_player}")
            print(f"Computer's first card: {computer_player[1]}")

        return [cur_value, user_player, computer_player]


    [cur_value_game, rand_list_user, rand_list_computer] = game_play(2, "")

    if cur_value_game == 21:
        print(f"Blackjack, You Win!")
        return

    def another_game_play(user_list, computer_list):
        deep_computer_list = copy.deepcopy(computer_list)
        user_list = user_list
        computer_list.pop(0)
        computer_list_val = computer_list

        continue_game = True

        while continue_game:
            user_response = input("Type 'y' to get another card, type 'n' to pass: ").lower()

            def rep_logic():
                tmp_user = 0
                tmp_comp = 0
                for i in user_list:
                    if i == "A":
                        if tmp_user + cards[i][1] <= 21:
                            tmp_user += cards[i][1]
                        else:
                            tmp_user += cards[i][0]
                    else:
                        tmp_user += cards[i]

                for j in deep_computer_list:
                    if j == "A":
                        if tmp_comp + cards[j][1] <= 21:
                            tmp_comp += cards[j][1]
                        else:
                            tmp_comp += cards[j][0]
                    else:
                        tmp_comp += cards[j]

                return [tmp_user, tmp_comp]



            if user_response == 'y':
                [_, list_user, _] = game_play(1, "hit")
                user_list.extend(list_user)

                [user_val, computer_val] = rep_logic()

                if user_val > 21:
                    print(f"Your cards: {user_list} : Total = {user_val}")
                    print(f"Computer's cards: {deep_computer_list} : Total = {computer_val}")
                    print(f"Dealer Wins")
                    return
                elif user_val == 21:
                    print(f"Your cards: {user_list} : Total = {user_val}")
                    print(f"Computer's cards: {deep_computer_list} : Total = {computer_val}")
                    print(f"Blackjack, You Win!")
                    return
                else:
                    print(f"Your current cards: {user_list} : Total = {user_val}")
                    print(f"Computer's current list: {computer_list_val} : Total = ")

            elif user_response == "n":
                [user_val, computer_val] = rep_logic()
                [_, _, list_computer] = game_play(1, "pass")
                deep_computer_list.extend(list_computer)
                computer_list_val.extend(list_computer)

                if computer_val > 21:
                    print(f"Blackjack, You Win!")
                    print(f"Your cards: {user_list} : Total1 = {user_val}")
                    print(f"Computer's cards: {deep_computer_list} : Total1= {computer_val}")
                    return
                elif computer_val == 21:
                    print(f"Your cards: {user_list} : Total2 = {user_val}")
                    print(f"Computer's cards: {deep_computer_list} : Total2 = {computer_val}")
                    print(f"Dealer Wins")

                    return
                elif deep_computer_list[0] == "A":
                    combo0 = computer_val + cards[deep_computer_list[0]][0]
                    combo1 = computer_val + cards[deep_computer_list[0]][1]
                    if combo0 == user_val:
                        computer_val += cards[deep_computer_list[0]][0]
                        print("Draw!")
                        return
                    if combo1 == user_val:
                        computer_val += cards[deep_computer_list[0]][1]
                        print("Draw!")
                        return
                    if user_val < combo0 <= 21:
                        computer_val += cards[deep_computer_list[0]][0]
                        print(f"Your cards: {user_list} : Total3 = {user_val}")
                        print(f"Computer's cards: {deep_computer_list} : Total3 = {computer_val}")
                        print(f"Dealer Wins")
                        return
                    if user_val < combo1 <= 21:
                        computer_val += cards[deep_computer_list[0]][1]
                        print(f"Your cards: {user_list} : Total4 = {user_val}")
                        print(f"Computer's cards: {deep_computer_list} : Total4 = {computer_val}")
                        print(f"Dealer Wins")
                        return
                elif user_val < (computer_val + cards[deep_computer_list[0]]) <= 21:
                    print(f"Your cards: {user_list} : Total4 = {user_val}")
                    print(f"Computer's cards: {deep_computer_list} : Total4 = {deep_computer_list}")
                    print(f"Dealer Wins")
                    return
                elif (computer_val + cards[deep_computer_list[0]]) == user_val:
                    print("Draw!")
                    return
                elif computer_val < user_val <= 21:
                    print(f"Your cards: {user_list} : Total5 = {user_val}")
                    print(f"Computer's cards: {computer_list_val} : Total5 = {computer_val}")
                    print(f"Blackjack, You Win!")
                    return
                elif user_val < computer_val <= 21:
                    print(f"Your cards: {user_list} : Total6 = {user_val}")
                    print(f"Computer's cards: {computer_list_val} : Total6 = {computer_val}")
                    print(f"Dealer Wins")
                    return
                elif computer_val == user_val:
                    print("Draw!")
                    return

    another_game_play(rand_list_user, rand_list_computer)

game()