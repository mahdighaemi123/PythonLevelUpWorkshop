# solution 1
intro = """
------------------------
     Temp Converter
------------------------
Converter options:
1. celsius to fahrenheit 
2. fahrenheit to celsius
------------------------
"""


def main():
    print(intro)
    while (1):
        option = input("> enter option: ")

        if option == "1":
            celsius = float(input("> enter celsius temp:"))
            fahrenheit = celsius * 9.5 + 32
            print(f"{celsius}°C = {fahrenheit}°F")

        elif option == "2":
            fahrenheit = float(input("> enter fahrenheit temp:"))
            celsius = (fahrenheit-32) / 9.5
            print(f"{fahrenheit}°F={celsius}°C")

        else:
            print("option not found")


main()
