# solution 1
import time
import random

intro = """"
------------------------
       Memory Game
------------------------
save numbers in your
memory, then we ask
what was the numbers
------------------------
"""


def check_answer(memory, answer):
    if memory == answer:
        print("you win correct answer!")
    else:
        print(f"you lose answer is: {' '.join(answer)}")


def main():
    print(intro)
    while (1):
        try:
            memory = []
            for _ in range(0, 3):
                random_number = random.randint(0, 9)
                memory.append(str(random_number))

            print(f"numbers are: {' '.join(memory)}")
            time.sleep(3)

            for _ in range(10):
                print()

            print("enter numbers or exit")

            answer = input("> ")
            if answer == "exit":
                exit()

            answer = answer.split()

            # answer = [int(num) for num in answer.split(" ")]
            # answer = map(int,answer.split())

            check_answer(memory, answer)

        except Exception as e:
            print(e)


main()
