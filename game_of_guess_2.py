def computer_guess(min_c, max_c):
    return int((max_c - min_c) // 2) + min_c


def guess_game_two():
    print("Think about number and i will guess it in ten moves.")
    min_answer = 0
    max_answer = 1000
    counter = 1
    while True:
        guess = computer_guess(min_answer, max_answer)
        try:
            user_answer = int(input(f"""I'm guessing: {guess}
Pick you answer:
1 - to big
2 - too small
3 - you guessed!
"""))
        except ValueError:
            print("Please answer using: 1, 2 or 3")
            continue
        if user_answer == 3:
            counter += 1
            return print("I won!")
        elif user_answer == 2:
            counter += 1
            min_answer = guess
        elif user_answer == 1:
            counter += 1
            max_answer = guess

        if counter > 10:
            print("Don't cheat!")


guess_game_two()
