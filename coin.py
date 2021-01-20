import random

def choose_coin():
    number = random.randint(0,100)
    return "unfair" if number == 100 else "fair"

def experiment():
    coin = choose_coin()
    if coin == "unfair":
        return coin, 10

    count = 0    
    for i in range(10):
        if random.randint(0,1) == 0:
            count += 1
    return coin, count

def a_lot_of_experiment(n):
    counter = {}
    counter["fair"] = 0
    counter["unfair"] = 0
    for i in range(n):
        coin, count = experiment()
        if count == 10:
            counter[coin] += 1

    return counter["fair"], counter["unfair"]

number_of_experiment = 500000
fair, unfair = a_lot_of_experiment(number_of_experiment)
print("Total Experiment :", fair + unfair)
print("Fair Coin        :", fair)
print("Unfair Coin      :", unfair)
print("Answer           :", 100 * unfair / (fair + unfair))