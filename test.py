import random
rock = """
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""

scissors = """
 
            ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

"""

paper = """
               _  / |
              / \ | | /\/
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
               |     |
"""

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rock_paper_scissor = [rock, paper, scissors]

rand_num = random.randint(0, 2)

if not 0 <= choice < 3:
    print("Invalid input")
    # print(f"Choice: {choice} : Random: {rand_num}")
else:
    print(f"{rock_paper_scissor[choice]}\n")
    print("Computer chose:\n")
    print(f"{rock_paper_scissor[rand_num]}\n")
    if choice == rand_num:
        print("Draw")
    elif (choice == 0 and rand_num == 1) or (choice == 1 and rand_num == 2) or (choice == 2 and rand_num == 0):
        print("You lose")
    else:
        print("You Win")
