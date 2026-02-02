import pandas as pd
from genetic_algorithm import generate_population, evolve

# Uploading users
users = pd.read_csv("data/users.csv")
example_user = users.sample(1).iloc[0]  # Берём первого пользователя

# Generate the initial population and start evolution
initial_pop = generate_population()
best_diet, best_workout = evolve(example_user, initial_pop)

# Output the result
print(f"User Goal: {example_user['goal']}")
print(f"User Preference: {example_user['preference']}")
print(f"Recommended Diet: {best_diet['name']} ({best_diet['calories']} kcal)")
print(f"Recommended Workout: {best_workout['name']} ({best_workout['calories']} kcal)")
print(f"Net Calories: {best_diet['calories'] - best_workout['calories']}")
