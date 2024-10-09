import os

calc_logo = """
 _____________________
|  _________________  |    
| | JO  3.141592654 | |
| |_________________| |
|  __ __ __ __ __ __  |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
| |__|__|__|__|__|__| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""
calculator_art = """
    _______      ____      .---.        _______     ___    _   .---.        ____   ,---------.    ,-----.    .-------.     
   /   __  \   .'  __ `.   | ,_|       /   __  \  .'   |  | |  | ,_|      .'  __ `.\          \ .'  .-,  '.  |  _ _   \    
  | ,_/  \__) /   '  \  \,-./  )      | ,_/  \__) |   .'  | |,-./  )     /   '  \  \`--.  ,---'/ ,-.|  \ _ \ | ( ' )  |    
,-./  )       |___|  /  |\  '_ '`)  ,-./  )       .'  '_  | |\  '_ '`)   |___|  /  |   |   \  ;  \  '_ /  | :|(_ o _) /    
\  '_ '`)        _.-`   | > (_)  )  \  '_ '`)     '   ( \.-.| > (_)  )      _.-`   |   :_ _:  |  _`,/ \ _/  || (_,_).' __  
 > (_)  )  __ .'   _    |(  .  .-'   > (_)  )  __ ' (`. _` /|(  .  .-'   .'   _    |   (_I_)  : (  '\_/ \   ;|  |\ \  |  | 
(  .  .-'_/  )|  _( )_  | `-'`-'|___(  .  .-'_/  )| (_ (_) _) `-'`-'|___ |  _( )_  |  (_(=)_)  \ `"/  \  ) / |  | \ `'   / 
 `-'`-'     / \ (_ o _) /  |        \`-'`-'     /  \ /  . \ /  |        \\ (_ o _) /   (_I_)    '. \_/``".'  |  |  \    /  
   `._____.'   '.(_,_).'   `--------`  `._____.'    ``-'`-''   `--------` '.(_,_).'    '---'      '-----'    ''-'   `'-'   
                                                                                                                           
"""

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def operation(operator):
    if operator == "*":
        return multiply
    elif operator == "-":
        return subtract
    elif operator == "/":
        return divide
    else:
        return add

cumulate_result = 0.0
while True:
    print(calculator_art + calc_logo)
    f_num = float(input("What's the first number?: "))
    response = "y"
    continue_calc = True
    while continue_calc:
        print("+\n-\n*\n/")
        operator_sign = input("Pick an operation: ")
        n_num = float(input("What's the next number?: "))
        calculation = operation(operator_sign)
        result = calculation(f_num, n_num)
        cumulate_result += result
        print(f"{f_num} {operator_sign} {n_num} = {result}")
        response = input(f"Type 'y' to continue calculating with {cumulate_result}, or type 'n' to start a new calculation: ").lower()
        if response == "n":
            continue_calc = False
            cumulate_result = 0.0
            os.system("cls" if os.name == "nt" else "clear")
