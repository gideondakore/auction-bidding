import random

hangman = """
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

hangman0 = """
+----+
|    |
     |
     |
     |
     |
     |
"""

hangman1 = """
 +----+
 |    |
 O    |
      |
      |
      |
      |
"""
hangman2 = """
  +----+
  |    |
  O    |
 /     |
       |
       |
       |
"""
hangman3 = """
  +----+
  |    |
  O    |
 / |   |
       |
       |
       |
"""

hangman4 = """
  +----+
  |    |
  O    |
 / |   |
  |    |
       |
       |
"""

hangman5 = """
  +----+
  |    |
  O    |
 / |   |
  |    |
 /     |
       |
"""

hangman6 = """
 ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \/
| |          ||  `/,|
| |          (\/\`_.'
| |         .-`--'.
| |        /Y . . Y\/
| |       // |   | \/\/
| |      //  | . |  \/\/
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \/
""""""""""|_`-' `-'  |"""
"|\|""""""\ \       '"|"|
| |        \ \        | | 
: :         \ \       : : 
. .          `'       . .
"""

guest_list = ["Enigma", "Zephyr", "Cryptic", "Nebula", "Labyrinth", "Quasar", "Vortex", "Sphinx", "Pandemonium", "Obsidian"]
hangman_list = [hangman0, hangman1, hangman2, hangman3, hangman4, hangman5, hangman6]

underscores = "_"
rand_word = random.choice(guest_list).lower()
# index_of_word = guest_list.index(rand_word)

life = 6
print(hangman)

def footer(val):
    print(hangman_list[(len(hangman_list)-1)-val])
    print(f"""
====================
***************************{val}/6 LIVES LEFT************************
""")

word_length = underscores * (len(rand_word))


def guess_interface():
    global word_length
    global life
    print(f"Words to guess: {word_length}")
    guess_char = input(f"Guessed a letter: ").lower()
    if rand_word.find(guess_char) != -1:
        pos = rand_word.find(guess_char)
        if rand_word[pos] == word_length[pos] and (len(rand_word)-1) >= pos+1:
            if rand_word.find(guess_char, pos+1) != -1:
                pos = rand_word.find(guess_char, pos+1)
        word_length = word_length[:pos] + guess_char + word_length[pos+1:]
        print(word_length)
        footer(life)
    else:
        print(f"You guessed {guess_char}, that's not in the word. You lose a life. {rand_word}")
        life -= 1
        footer(life)
        if life == 0:
            print("You lose")


while life > 0:
    guess_interface()
    if word_length == rand_word:
        life = 0
        print("You Win!")
