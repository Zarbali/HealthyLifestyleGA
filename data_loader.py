import random
import pandas as pd


# Generate a list of synthetic users with random goals and preferences
def generate_users(n=5):
    goals = ['weight_loss', 'muscle_gain', 'maintenance']  # Fitness goals
    preferences = ['vegan', 'vegetarian', 'omnivore']  # Dietary preferences
    users = []

    for i in range(n):
        user = {
            'id': i + 1,
            'age': random.randint(18, 50),  # Random age between 18 and 50
            'weight': random.randint(50, 100),  # Random weight in kg
            'height': random.randint(150, 200),  # Random height in cm
            'goal': random.choice(goals),  # Random fitness goal
            'preference': random.choice(preferences)  # Random diet preference
        }
        users.append(user)

    return pd.DataFrame(users)  # Return as a pandas DataFrame


# Define a fixed list of example diets
def generate_diets():
    return pd.DataFrame([
        {'name': 'High Protein Vegan', 'calories': 2000, 'type': 'vegan', 'protein': 100},
        {'name': 'Balanced Vegetarian', 'calories': 2200, 'type': 'vegetarian', 'protein': 80},
        {'name': 'Keto Omnivore', 'calories': 2500, 'type': 'omnivore', 'protein': 120},
        {'name': 'Low Carb Vegan', 'calories': 1800, 'type': 'vegan', 'protein': 70},
        {'name': 'Muscle Gain Omnivore', 'calories': 3000, 'type': 'omnivore', 'protein': 140},
    ])
    # Each diet includes total calories, type, and protein level


# Define a fixed list of example workouts
def generate_workouts():
    return pd.DataFrame([
        {'name': 'Cardio Light', 'duration': 30, 'intensity': 'low', 'calories': 200},
        {'name': 'Cardio Intense', 'duration': 45, 'intensity': 'high', 'calories': 400},
        {'name': 'Strength Basic', 'duration': 40, 'intensity': 'medium', 'calories': 300},
        {'name': 'HIIT Extreme', 'duration': 25, 'intensity': 'high', 'calories': 450},
        {'name': 'Yoga Flex', 'duration': 60, 'intensity': 'low', 'calories': 180},
    ])
    # Each workout includes duration, intensity level, and estimated calories burned


# Save all generated data to CSV files inside the data/ directory
def save_data():
    users_df = generate_users()  # Generate user dataset
    diets_df = generate_diets()  # Generate diet dataset
    workouts_df = generate_workouts()  # Generate workout dataset

    users_df.to_csv("data/users.csv", index=False)  # Save users to CSV
    diets_df.to_csv("data/diets.csv", index=False)  # Save diets to CSV
    workouts_df.to_csv("data/workouts.csv", index=False)  # Save workouts to CSV


# Run the script to create and save data
if __name__ == '__main__':
    save_data()
