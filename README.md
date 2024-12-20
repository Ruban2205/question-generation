<br />
<div align="center">

  <h1 align="center">Coach MO: Question Generation</h1>

  <p align="center">
    This repository provides a solution for generating detailed and thoughtful questions based on workout plans and evaluating their quality using the **G-Eval** metric. It is designed to assist fitness enthusiasts, trainers, and developers working with structured workout plans in improving the clarity, relevance, and usability of their fitness-related questions.
    <br />
    <br />
    <a href="report/MM811___Project_Report___Coach_MO__Question_Generation.pdf">View Final Report</a>
    ·
    <a href="ppt/MM811_Presentation.pdf">View PPT</a>
    ·
    <a href="results/evaluation_results.csv">View Results</a>
  </p>
</div>

---

## Features

### 1. **Workout Question Generation**

- **Script**: `generate_questions.py`
- **Description**:
  - Automatically generates thoughtful questions based on attributes of workout plans, such as title, phase, purpose, duration, and more.
  - Utilizes **Few-shot + Chain-of-Thought Prompting** with OpenAI's GPT-3.5-turbo model for generating specific and context-aware questions.
- **Input**: JSON file containing workout plans (`data/workout_data.json`).
- **Output**: Generated questions saved in a text file (`outputqns/generated_questions.txt`).

### 2. **Question Evaluation**

- **Script**: `test_geval.py`
- **Description**:
  - Evaluates the quality of the generated questions using the **G-Eval** metric.
  - The evaluation focuses on correctness, relevance, and alignment with the context of workout plans.
  - Results are saved in a CSV file (`results/evaluation_results.csv`) for further analysis.
- **Metrics Used**:
  - **Correctness**: Ensures the questions are factually accurate and relevant.

---

## File Structure

```plaintext
project-root/
│
├── data/
│   └── workout_data.json    # Input JSON with workout plan details.
│
├── outputqns/
│   └── generated_questions.txt  # Text file containing generated questions.
│
├── results/
│   └── evaluation_results.csv   # CSV file with evaluation results.
│
├── generate_questions.py    # Script for generating workout questions.
├── test_geval.py            # Script for evaluating generated questions.
└── README.md                # Project documentation.
```

## Requirements

### Libraries and Tools

- Python 3.8+
- OpenAI Package
- DeepEval Package for metrics evaluation
- Pandas for result processing

## Python Packages

Install the the required packages using pip:

```bash
pip install -r requirements.txt
```

or

```bash
pip install pandas openai deepeval
```

## Setup and Usage

### 1. Environment Variables

Ensure that you are having the following environment variable

- `OPENAI_API_KEY:` API Key for OpenAI GPT Models.

### 2. Running the Question Generation

Execute the script `generate_questions.py` to generate questions based on the workout data:

```bash
python generate_questions.py
```

- **Note:** Use `openai==0.28` for this script.

### 3. Running the Evaluation

Run the `test_geval.py` script to evaluate the generated questions.

- **Note:** Use Deepeval framework to Run

```bash
pip install -U deepeval
```

```bash
deepeval login
```

- **Note:** Paste the DeepEval API Key if prompted.

```bash
deepeval test run test_geval.py
```

- **Note:** Use the above script to run the evaluation file.
- Also, ensure that the latest version of `openai` is installed for this script.

## Authors

- Ruban Gino Singh Arul Peppin Raj - [rubangin@ualberta.ca](https://mailto:rubangin@ualberta.ca)
- Raja Priya Mariappan - [rajapriy@ualberta.ca](https://rajapriy@ualberta.ca)
- Raju Bhattarai - [raju2@ualberta.ca](https://mailto:raju2@ualberta.ca)

---
