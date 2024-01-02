# solution 1
intro ="""
---------------------------
        Length-Counter
---------------------------
Supported actions:
1. count alphabet characters ([a-z],[A-Z])
2. count numberic characters ([0-9])
3. count words (split by " ")
4. count sentances (split by ".")
---------------------------
"""

def alphabet_count(text):
    count = 0
    for char in text:
        if(char.isalpha()):
            count+=1
    return count      

def numberic_count(text):
    count = 0
    for char in text:
        if(char.isnumeric()):
            count+=1
    return count     

def words_count(text):
    words = text.split(" ")
    count = len(words)
    return count
    
def sentences_count(text):
    sentences = text.split(".")
    count = len(sentences)-1
    return count

actions = {
    "1": alphabet_count,
    "2": numberic_count,
    "3": words_count,
    "4": sentences_count
}


def main():
    print(intro)
    while (1):
        try:

            print("Enter your text or exit: ")

            text = input("> ")
            if text == "exit":
                exit()

            print("Enter your target actions: ")
            input_actions = input("> ")
           
            for action in actions.keys():
                if action in input_actions:
                    func = actions[action]
                    name = func.__name__
                    count = func(text)
                    print(f"{name} is: {count}")

            print()

        except Exception as e:
            print(e)


main()
