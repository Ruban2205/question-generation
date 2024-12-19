import openai
import json
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load workout data
with open("workout_data.json", "r") as file:
    workout_data = json.load(file)

def create_prompt(workout):
    """
    Create a detailed prompt using all attributes of the workout plan.
    """
    prompt = f"""
    Generate a list of thoughtful and detailed questions a user might ask about the following workout plan.
    Consider all provided attributes, including title, plan phase, workout purpose, workout category, description, duration, nutrition, coach's message, and structured training details.

    Title: {workout.get("title", "N/A")}
    Plan Phase: {workout.get("plan_phase", "N/A")}
    Workout Purpose: {workout.get("workout_purpose", "N/A")}
    Workout Category: {workout.get("workout_category", "N/A")}
    Description: {workout.get("description", "N/A")}
    Duration: {workout.get("duration_min", "N/A")} - {workout.get("duration_max", "N/A")} minutes
    Nutrition: {workout.get("workout_nutrition", "N/A")}
    Coach's Message: {workout.get("coaches_message", "N/A")}
    Structured Training:
    - Bike: {workout.get("structured_bike", "N/A")}
    - Run: {workout.get("structured_run", "N/A")}
    - Swim: {workout.get("structured_swim", "N/A")}
    """
    return prompt.strip()

def generate_questions(prompt, model="gpt-3.5-turbo", max_tokens=200):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a fitness enthusiast looking to get more details about workout plans. Frame your questions as if you are genuinely curious about various aspects of these plans, including exercises, duration, frequency, intensity, dietary recommendations, or any special considerations. Be specific in your queries to get the most relevant and actionable responses. Focus on practical details that someone following the workout plan would want to know."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

# Loop through each workout in the JSON and generate questions
for workout in workout_data:
    prompt = create_prompt(workout)
    questions = generate_questions(prompt)
    print(f"Workout Title: {workout.get('title', 'N/A')}")
    print("Generated Questions:")
    print(questions)
    print("-" * 80)