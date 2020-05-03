import random

# Counts how many tries it needs to guess a number from 1 to 99.
def guess_number(number):
    count = 1
    interval = [0,100] # Searching interval. We will narrow it to find number.

    predict = round((interval[0] + interval[1]) / 2) # First try.
    while number != predict:
        count += 1 # Count tries.
        predict = round((interval[0] + interval[1]) / 2)  # Try to guess a number from interval.

        # Narrow interval.
        if number > predict:
            interval[0] = predict
        elif number < predict:
            interval[1] = predict

    return(count)

# Counts avarage amount of tries of guessing number using guess_function.
def score_game(guess_function):
    guess_results = []

    # Call guess_function 1000 times and forms result list.
    for i in range(1000):
        randomInt = random.randint(1,100)
        guess_results.append(guess_function(randomInt))

    # Count avarage amount of tries.
    score = sum(guess_results) / len(guess_results)

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

    return (score)


# Call
score_game(guess_number)