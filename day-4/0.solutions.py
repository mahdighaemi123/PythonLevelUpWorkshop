# solution 1
import random
result_map = {
    "Rock": {
        "Rock": "eqaul",
        "Paper": "computer",
        "Scissors": "human",
    },
    "Paper": {
        "Rock": "human",
        "Paper": "eqaul",
        "Scissors": "computer",
    },
    "Scissors": {
        "Rock": "computer",
        "Paper": "human",
        "Scissors": "eqaul",
    },
}

message_map = {
    "computer": "you lose :(",
    "human": "you win :)",
    "eqaul": "tie"
}

game_options = ["Rock", "Paper", "Scissors"]

welcome_message = """
------------------------
Rock Paper Scissors Game
------------------------
You can play with:
1.Rock
2.Paper
3.Scissors
------------------------
"""


def main():
    print(welcome_message)
    while 1:
        try:
            i = input("> what do you pick: ")
            i = i.capitalize()

            if i == "Exit":
                # break
                exit()

            r = random.choice(game_options)
            print(i, r)

            result = result_map[i][r]
            # result = result_map.get(i,{}).get(r,"")

            message = message_map[result]
            # message = message_map.get(result,"Error")

            print(message)
        except:
            print("error happend")


main()
