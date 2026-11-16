import random


def play() -> None:
    balance = 5000

    random_list = [1, 2, 3, 4, 5, 6, 7]

    random.shuffle(random_list)

    while True:
        user_input = input("Do you want to play (y/n)?\n").lower()

        if user_input != "y":
            quit()

        if balance < 1:
            print("You run out of money!")
            quit()

        first = random.choice(random_list)
        second = random.choice(random_list)
        third = random.choice(random_list)

        print(f"{first} {second} {third}")

        if first == second and second == third:
            print("Conrulations!")
            balance += first * 1000
            print(f"Balance: {balance}")
        else:
            balance -= 500
            print(f"Balance: {balance}")


play()
