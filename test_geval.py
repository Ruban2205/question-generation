from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
import pandas as pd

# Define the G-Eval metric
correctness_metric = GEval(
    name="Correctness",
    criteria="Determine whether the generated question is factually correct and relevant based on the context of the workout plan.",
    evaluation_steps=[
        "Check if the generated question is clear, precise, and aligned with the context.",
        "Determine if it effectively evaluates knowledge of the workout plan's goals, structure, or other details.",
        "Penalize omissions, irrelevance, or factual inconsistency."
    ],
    evaluation_params=[
        LLMTestCaseParams.INPUT,
        LLMTestCaseParams.ACTUAL_OUTPUT,
        LLMTestCaseParams.EXPECTED_OUTPUT,
    ],
)

# Define workout plans and their generated questions
workout_plans = {
    "MAKE IT OR BREAK IT": [
        "What is the main goal of the 'MAKE IT OR BREAK IT' workout plan in the Baseline Fitness phase?",
        "How long does the entire workout session last, including warm-up, main set, and cool down?",
        "Can you explain the specific structure of the main set in detail, including the duration of each fast effort and recovery period?",
        "What is the recommended nutrition intake before starting this workout, and why is it important?",
        "How does this workout aim to help develop Vo2 Max according to the coach's message?",
        "What type of running zones are targeted during the main set, and how does this contribute to the workout's intensity?",
        "Is there a specific reason for the order and duration of the fast efforts within the main set?",
        "How can participants ensure they are properly cooling down after completing the workout?",
        "Are there any recommended modifications for individuals who may find this workout too challenging initially?",
        "How frequently should this workout be"
    ],
    "THE BUBBLE": [
        "What is the primary goal of 'THE BUBBLE' workout plan in the Baseline Fitness phase?",
        "How would you describe the intensity level of the 'Intense Bike 2' workout category in this plan?",
        "Can you explain the breakdown of the Warm Up section in terms of duration and intensity zones?",
        "What is the structure of the Main Set in terms of intervals and targeted power zones?",
        "What is the purpose of the Coach's Message focusing on developing Vo2 Max?",
        "How long is the recommended duration for completing 'THE BUBBLE' workout plan?",
        "Could you provide insights into the nutrition recommendations for pre-workout and during the workout?",
        "Where can one access the annual $80 nutrition product benefit mentioned in the plan?",
        "How is the structured training detailed for the Bike segment, and what does each abbreviation stand for (WU, A, CD)?",
        "Are there any specific recommendations for adjusting this workout plan"
    ],
    "THE DOCTOR": [
        "What is the overall goal of 'THE DOCTOR' workout plan in the Baseline Fitness phase?",
        "How does the workout purpose of 'adapt' tie into the specific intensity and structure of the Intense Bike 1 category?",
        "Can you explain the significance of the Warm Up phase, specifically targeting Zone 2 heart rate?",
        "What is the rationale behind the main set of repeating 4.5 minutes at Zone 4 effort followed by 3.5 minutes of easy spinning? How does this contribute to the workout's effectiveness?",
        "How important is the Cool Down phase in this workout plan, and why is it specifically designed for easy spinning targeting Zone 1 RPE?",
        "What is the expected duration of the entire workout, and how does the timing of each phase contribute to the overall effectiveness of the plan?",
        "Can you elaborate on the suggested pre-workout nutrition of 30-40g of carbs and the recommended light electrolyte drink during"
    ],
    "IT BURNS": [
        "What is the main purpose of the 'IT BURNS' workout plan?",
        "Can you explain the significance of the Baseline Fitness phase in relation to this workout plan?",
        "How would you describe the intensity level of the 'IT BURNS' workout, considering it falls under the Intense Run category?",
        "What are the key components of the warm-up session in this workout plan?",
        "How long does the main set portion of the workout last, and what does it involve?",
        "Can you elaborate on the cool-down segment of the workout and its importance?",
        "What is the expected total duration of the entire workout session?",
        "Could you explain the recommended pre-workout nutrition guidelines provided for this workout plan?",
        "How does the coach's message to 'adapt to Vo2 max running' impact the execution of this workout plan?",
        "In the structured training details, what specific elements are included for running, and how do they contribute to the overall"
    ]
}

# Define expected questions for comparison
expected_questions = {
    "MAKE IT OR BREAK IT": [
        "What is the purpose of the 'MAKE IT OR BREAK IT' workout in the Baseline Fitness phase?",
        "What is the total duration of the workout, including all phases?",
        "Describe the structure of the main set, including fast efforts and recovery periods.",
        "What nutrition is recommended before starting the workout, and why?",
        "How does this workout contribute to Vo2 Max development?",
        "What running zones are targeted during the main set, and how does this affect intensity?",
        "Why are the fast efforts arranged in their specific order and duration?",
        "How can participants effectively cool down after the workout?",
        "What modifications can be made for those finding the workout too challenging?",
        "How often should participants perform this workout?"
    ],
    "THE BUBBLE": [
        "What is the main focus of 'THE BUBBLE' workout?",
        "How would you rate the intensity of the 'Intense Bike 2' segment?",
        "Describe the Warm Up section, including its duration and intensity zones.",
        "What is the structure of the Main Set in terms of power zones and intervals?",
        "What is the purpose of the Coach's Message on developing Vo2 Max?",
        "How long should 'THE BUBBLE' workout plan take to complete?",
        "What nutrition is recommended before and during the workout?",
        "How can one access the $80 nutrition benefit mentioned?",
        "What details are provided for the Bike training segment (WU, A, CD)?",
        "What recommendations are there for adjusting the workout plan?"
    ],
    "THE DOCTOR": [
        "What is the main goal of 'THE DOCTOR' workout?",
        "How does the 'adapt' purpose tie into the intensity of the Intense Bike 1 segment?",
        "Why is the Warm Up phase, targeting Zone 2 heart rate, important?",
        "What is the significance of repeating 4.5 minutes at Zone 4 effort followed by 3.5 minutes of easy spinning?",
        "Why is the Cool Down phase designed for easy spinning at Zone 1 RPE?",
        "What is the expected duration of the workout, and how does the phase timing contribute to its effectiveness?",
        "What pre-workout nutrition is suggested, and why is it recommended?"
    ],
    "IT BURNS": [
        "What is the purpose of the 'IT BURNS' workout?",
        "What is the importance of the Baseline Fitness phase for this workout?",
        "Describe the intensity level of the 'IT BURNS' workout in the Intense Run category.",
        "What are the main components of the warm-up for this workout?",
        "How long is the main set portion of this workout, and what does it entail?",
        "What is the importance of the cool-down segment, and how should it be performed?",
        "What is the total expected duration of the workout?",
        "What pre-workout nutrition is recommended for this workout?",
        "How does the coach's message to 'adapt to Vo2 max running' impact the plan?",
        "What structured training details are included for running, and what do they contribute?"
    ]
}

# Store results for evaluation
results = []

# Evaluate all questions and store results
for workout_title, generated_questions in workout_plans.items():
    for i, generated_question in enumerate(generated_questions):
        # Prepare the test case
        expected_question = (
            expected_questions[workout_title][i]
            if i < len(expected_questions[workout_title])
            else ""
        )
        test_case = LLMTestCase(
            input=f"Workout Plan: {workout_title}",
            actual_output=generated_question,
            expected_output=expected_question,
        )

        # Evaluate the question
        correctness_metric.measure(test_case)

        # Calculate and round the score
        score_percentage = round(correctness_metric.score * 100, 2)

        # Append the results
        results.append({
            "Questions": generated_question,
            "Score (%)": f"{score_percentage}%",
        })

# Display results in a tabular format using pandas
df_results = pd.DataFrame(results)
print(df_results)

# Saving results in a CSV file
output_file_path = 'evaluation_results.csv'
df_results.to_csv(output_file_path, index=False)
print(f"Results saved to {output_file_path}")
