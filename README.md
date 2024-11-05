# TOEFL-Reading-Question-Generator

## Overview

This project is designed to generate TOEFL Reading questions, answers, and explanations using Google's Generative AI models. The notebook `model.ipynb` demonstrates the process of generating content, fine-tuning models, and saving the generated outputs.

## Project Structure

- `assets/`: Directory containing additional assets.
- `datasets/`: Directory containing datasets used for fine-tuning.
  - `Question-Explanation.xlsx`
  - `Question-Types.xlsx`
- `model.ipynb`: Jupyter notebook demonstrating the content generation process.
- `README.md`: Project documentation.

## Setup

1. Install the required libraries:

   ```sh
   pip install -q -U google-generativeai
   ```

2. Configure the API key for Google Generative AI:
   ```python
   import google.generativeai as genai
   from google.colab import userdata
   GEMINI_API_KEY = userdata.get("GEMINI_API_KEY")
   genai.configure(api_key=GEMINI_API_KEY)
   ```

## Usage

1. **Generate TOEFL Reading Text:**

   - Input a topic to generate a TOEFL Reading text.
   - Save the generated text as `generated_text`.

2. **Generate Questions:**

   - Use the generated text to create TOEFL Reading questions.
   - Save the generated questions as `generated_questions`.

3. **Generate Answers and Explanations:**
   - Use the generated text and questions to create answers and explanations.
   - Save the generated answers and explanations as `generated_answers_explanations`.

## Fine-Tuning Models

The notebook demonstrates fine-tuning the Gemini-1.5 model with different datasets:

1. **Question-Type Dataset:**

   - Fine-tune the model using `Question-Types.xlsx`.

2. **Question-Explanation Dataset:**
   - Fine-tune the model using `Question-Explanation.xlsx`.

## Example

An example workflow is provided in the notebook, including sample prompts and outputs for generating TOEFL Reading questions, answers, and explanations.

## License

This project is licensed under the MIT License.
