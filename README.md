# HealthyLifestyleGA 
# Healthy Lifestyle Recommendation System using Genetic Algorithm

This project implements an AI-based recommendation system that generates personalized **diet** and **workout plans** for users based on their physical profile, goals, and preferences. It uses a **Genetic Algorithm** to find the best combination of plans that match the user’s needs.

## 🧠 Project Goal

To apply a basic artificial intelligence method (Genetic Algorithm) to solve a **real-world problem**: recommending training and diet plans that help users achieve goals such as weight loss, muscle gain, or health maintenance.


## 🔧 Requirements

- Python 3.7+
- pandas


▶️ How to Run
Run the recommendation engine:
python main.py

Output Example:
User Goal: weight_loss
User Preference: vegetarian
Recommended Diet: Balanced Vegetarian (2200 kcal)
Recommended Workout: Strength Basic (300 kcal)
Net Calories: 1900


💡 How It Works
A population of random diet/workout pairs is created.

Each pair is evaluated using a fitness function that scores how well it fits the user's profile.

The best combinations are selected and used to create the next generation.

Through selection, crossover, and mutation, the population evolves over 10 generations.

The final output is the optimal plan for the given user.


🧪 Example Use Case
User:

Age: 25

Weight: 75 kg

Height: 175 cm

Goal: muscle_gain

Preference: omnivore

The system recommends:

A high-protein diet

An intense workout plan

Total calories adjusted for muscle growth

📌 Notes
The project is for educational purposes and uses randomly generated data.

The structure can be extended to real user inputs, advanced metrics, and web/AI integrations.

📍 Author
Created for an Artificial Intelligence course – Task No. 3

Arif Zarbaliyev (Student ID: 48232)
Bozhena Hlotko (Student ID: 47122)

May 2025