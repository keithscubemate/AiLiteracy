import string
import random

goal = "Keith"
pop_size = 1000
breeding_pool_size = 50
mutation_rate = 0.01

def get_rand_char() -> str:
    return random.choice(string.ascii_letters + ' ')

def get_rand_string(len: int) -> str:

    return ''.join([get_rand_char() for _ in range(len)])

def fitness(elem: str, goal: str) -> int:
    rv = 0
    for i, c in enumerate(elem):
        if goal[i] == c:
            rv += 1;

    return rv;

def breed(e1: str, e2: str) -> str:
    child = ""

    for i in range(len(e1)):
        temp = random.random()
        if (temp < mutation_rate):
            child += get_rand_char()
        elif (temp < ((1 - mutation_rate) / 2) + mutation_rate):
            child += e1[i]
        else:
            child += e2[i]
    return child

def random_chance(goal, verbose=False):
    i = 0
    while (guess:=get_rand_string(len(goal))) != goal:
        i += 1
        if verbose:
            print(i, guess)

    print(i, guess)

def genetic_alg(goal, verbose=False):

    population = [get_rand_string(len(goal)) for _ in range(pop_size)]

    i = 0
    while True:
        i += 1

        pop_fit = [(elem, fitness(elem, goal)) for elem in population]

        pop_fit = sorted(pop_fit, key=lambda t: t[1])


        fittest = [t[0] for t in pop_fit[-1 * breeding_pool_size * 2:]][::-1]
        abs_fit = fittest[0]



        if abs_fit == goal:
            print(i, fittest[0])
            return;

        if verbose:
            print()
            print(i, fittest[0])

        random.shuffle(fittest)

        pool = [(fittest[i], fittest[i + len(fittest) // 2]) for i in range(len(fittest) // 2)]
        population = []
        for papa, mama in pool:
            for _ in range(pop_size // breeding_pool_size):
                population.append(breed(papa, mama))

if __name__ == "__main__":

    print("Guessing: ", goal)

    print()
    print("Genetic Alg:")
    genetic_alg(goal)

    # print()
    # print("Random Chance:")
    # random_chance(goal)
