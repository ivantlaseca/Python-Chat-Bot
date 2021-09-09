import random
import os
import webbrowser


def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + ' for my creator\'s AI course.')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "!")


def related(request):
    if "name" in request:
        understood = "What's your name?"
    elif "uplift" in request or "cheer" in request:
        understood = "Uplift me."
    elif "open" in request:
        understood = "Open webpage."
    elif "do" in request and "homework" in request:
        understood = "Pranked."
    elif "how" in request and "are" in request and "age" not in request and "old" not in request:
        understood = "How are you doing?"
    elif "guess" in request and "my" in request and "age" in request or "old" in request:
        understood = "How old am I?"
    else:
        understood = "Idk"

    return understood


def openWebpage(websiteName):
    webbrowser.open("http://" + websiteName + ".com", new=1)


def uplifts():
    encouragements = ["You're the best!",
                      "You've got this!",
                      "You look handsome today!",
                      "Don't give up. Suffer now and live the rest of your life as a champion.",
                      "Prove them wrong.",
                      "Remember your \"why\". Remember who you do this for.",
                      "You are a winner. Go out and win it all!"]

    randomEncouragement = random.choice(encouragements)

    print(randomEncouragement)


def howAmI():
    moods = ["I've had better days.",
             "Having the best day ever!",
             "Glad to be talking to you.",
             "Talking to you just made my day a lot better!",
             "Kinda hungry tbh...",
             "I'm doing good!.",
             "Life is amazing it is what it should be."]

    randomMood = random.choice(moods)

    print(randomMood)


def functions(name):
    print("How can I help you today, " + name + "? (\"Exit\" to quit)")
    request = input()
    request = request.lower()

    while request != "exit":
        understood = related(request)
        if understood == "What's your name?":
            print("My name is Blex!")
        elif understood == "Uplift me.":
            uplifts()
        elif understood == "Open webpage.":
            openWebpage(request.split(" ")[1])
        elif understood == "Pranked.":
            print("Ha! Good one. Get to work!")
        elif understood == "How are you doing?":
            howAmI()
        elif understood == "How old am I?":
            guess_age()
        else:
            print("Not sure if I can help with that at the moment.")
        print("How else can I help?")
        request = input()
        request = request.lower()


def main():
    greet('Blex', '2021')
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')
    functions(name)

    print("Goodbye!")


main()
