import pandas as pd
import random

# Load predefined diet and workout datasets from CSV files
diets = pd.read_csv("data/diets.csv")
workouts = pd.read_csv("data/workouts.csv")


# Fitness function to evaluate how suitable a (diet, workout) pair is for a given user
def fitness(user, diet, workout):
    score = 0

    # +1 if the diet matches the user's dietary preference (e.g., vegan)
    if diet['type'] == user['preference']:
        score += 1

    # Calculate net calorie intake (diet calories minus workout calories)
    total_calories = diet['calories'] - workout['calories']

    # +1 if the net calorie goal aligns with the user's goal
    if user['goal'] == 'weight_loss' and total_calories < 2000:
        score += 1
    elif user['goal'] == 'muscle_gain' and total_calories > 2500:
        score += 1
    elif user['goal'] == 'maintenance' and 2000 <= total_calories <= 2500:
        score += 1

    # +1 if muscle gain requires high protein and medium/high workout intensity
    if user['goal'] == 'muscle_gain' and diet['protein'] >= 100 and workout['intensity'] in ['medium', 'high']:
        score += 1

    return score  # Maximum possible score is 4


# Generate an initial population of random (diet, workout) pairs
def generate_population(size=20):
    population = []
    for _ in range(size):
        diet = diets.sample(1).iloc[0]  # Random diet from dataset
        workout = workouts.sample(1).iloc[0]  # Random workout from dataset
        population.append((diet, workout))  # Pair them and add to population
    return population


# Evolve the population over several generations to find the best plan
def evolve(user, population, generations=10):
    for _ in range(generations):
        # Evaluate fitness for each individual (diet + workout)
        scored = [(individual, fitness(user, individual[0], individual[1])) for individual in population]

        # Sort individuals by fitness score, descending
        scored.sort(key=lambda x: x[1], reverse=True)

        # Select the top 10 as parents for next generation
        population = [x[0] for x in scored[:10]]

        # Crossover: create new individuals (children) by combining parts of parents
        children = []
        while len(children) < 10:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = (
                random.choice([parent1[0], parent2[0]]),  # diet from parent1 or parent2
                random.choice([parent1[1], parent2[1]])  # workout from parent1 or parent2
            )
            children.append(child)

        # Mutation: randomly alter some children for variety
        for i in range(len(children)):
            if random.random() < 0.3:
                children[i] = (
                    diets.sample(1).iloc[0],  # new random diet
                    children[i][1]
                )
            if random.random() < 0.3:
                children[i] = (
                    children[i][0],
                    workouts.sample(1).iloc[0]  # new random workout
                )

        # Add children to current population
        population += children

    # After evolution, return the best individual based on fitness
    best = max(population, key=lambda ind: fitness(user, ind[0], ind[1]))
    return best
