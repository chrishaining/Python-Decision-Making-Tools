import random


def ask_for_options():
    option = input("Give me one of the options. ").lower()
    return option

def random_choice(options):
    chosen_option = random.choice(options)
    return chosen_option

def decision_bot():
    print("Welcome to the decision bot.")
    tell_me_an_option = 'y'
    options = []
    while tell_me_an_option == 'y':
        option = ask_for_options()
        options.append(option)
        while True: 
            tell_me_an_option = input("Would you like to add an option? (y/n) ")
            if tell_me_an_option == 'y' or 'n':
                break
          
    print("Okay, so your options are: ")
    for option in options:
      print('*', option)
    choice = random_choice(options)
    print("I have decided that you should choose: {}".format(choice))
    return choice


decision_bot()