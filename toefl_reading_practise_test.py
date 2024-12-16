"""
# Step 1: Set and import model, libraries etc.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv
import venv
 

# .env dosyasıdan çevre değişkenlerini yükle
load_dotenv()

# Gemini API key getir
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

if not GEMINI_API_KEY:
    raise EnvironmentError("Gemini API key not found. Please add GEMINI_API_KEY to your .env file.")
else:
    print("Gemini API key added.")

model = genai.GenerativeModel("gemini-1.5-flash")

import pathlib
import textwrap
import google.generativeai as genai


"""# Step2: generate a TOEFL Reading text

        - Take a {topic} from user.
        - Use the {topic} to generate a TOEFL Reading text.
        - save the generated TOEFL Reading text as {generated_text}
"""
# Define a function to generate TOEFL passage
def generate_toefl_text(topic):
    prompt = f"""
    Create a 700-word academic text in the style of a TOEFL iBT Reading passage on the topic of “{topic}.” The text should resemble college-level introductory texts or academic articles, written in a clear, formal, and accessible manner suitable for comprehension testing by advanced English learners. Please ensure the text follows the format of TOEFL passages by including:

    - **A single main title with no subtitles** in the text.

    - A well-organized structure that could follow one of these types, depending on the topic:
    - **Exposition:** Offering clear, objective explanations of key concepts, terms, and developments.
    - **Argumentation:** Presenting multiple perspectives on a topic or issue, contrasting viewpoints or debating positions.
    - **Historical:** Tracing the evolution or development of the topic, highlighting major events, figures, or turning points.

    The language should be formal and objective, using minimal technical jargon. The content should be understandable to readers unfamiliar with the topic. Additionally, organize the information using classification, comparison/contrast, cause/effect, or problem/solution structures as relevant.

    ### Sample 1:
    topic: The rise of Teotihuacán was driven by its strategic location, abundant obsidian resources, and skilled elite, which together fostered economic growth, population influx, and religious influence across Mesoamerica.
    text: The Rise of Teotihuacán
    The city of Teotihuacán, which lay about 50 kilometers northeast of modern-day Mexico City, began its growth by 200–100 B.C. At its height, between about A.D. 150 and 700, it probably had a population of more than 125,000 people and covered at least 20 square kilometers. It had over 2,000 apartment complexes, a great market, a large number of industrial workshops, an administrative center, a number of massive religious edifices, and a regular grid pattern of streets and buildings. Clearly, much planning and central control were involved in the expansion and ordering of this great metropolis. Moreover, the city had economic and perhaps religious contacts with most parts of Mesoamerica (modern Central America and Mexico).
    How did this tremendous development take place, and why did it happen in the Teotihuacán Valley? Among the main factors are Teotihuacán’s geographic location on a natural trade route to the south and east of the Valley of Mexico, the obsidian resources in the Teotihuacán Valley itself, and the valley’s potential for extensive irrigation. The exact role of other factors is much more difficult to pinpoint—for instance, Teotihuacán’s religious significance as a shrine, the historical situation in and around the Valley of Mexico toward the end of the first millennium B.C., the ingenuity and foresightedness of Teotihuacán’s elite, and, finally, the impact of natural disasters, such as the volcanic eruptions of the late first millennium B.C.
    This last factor is at least circumstantially implicated in Teotihuacán’s rise. Prior to 200 B.C., a number of relatively small centers coexisted in and near the Valley of Mexico. Around this time, the largest of these centers, Cuicuilco, was seriously affected by a volcanic eruption, with much of its agricultural land covered by lava. With Cuicuilco eliminated as a potential rival, any one of a number of relatively modest towns might have emerged as a leading economic and political power in Central Mexico. The archaeological evidence clearly indicates, though, that Teotihuacán was the center that did arise as the predominant force in the area by the first century A.D.
    It seems likely that Teotihuacán’s natural resources—along with the city elite’s ability to recognize their potential—gave the city a competitive edge over its neighbors. The valley, like many other places in Mexican and Guatemalan highlands, was rich in obsidian. The hard volcanic stone was a resource that had been in great demand for many years, at least since the rise of the Olmecs (a people who flourished between 1200 and 400 B.C.), and it apparently had a secure market. Moreover, recent research on obsidian tools found at Olmec sites has shown that some of the obsidian obtained by the Olmecs originated near Teotihuacán. Teotihuacán obsidian must have been recognized as a valuable commodity for many centuries before the great city arose.
    Long-distance trade in obsidian probably gave the elite residents of Teotihuacán access to a wide variety of exotic goods, as well as a relatively prosperous life. Such success may have attracted immigrants to Teotihuacán. In addition, Teotihuacán’s elite may have consciously attempted to attract new inhabitants. It is also probable that as early as 200 B.C. Teotihuacán may have achieved some religious significance and its shrine (or shrines) may have served as an additional population magnet. Finally, the growing population was probably fed by increasing the number and size of irrigated fields.
    The picture of Teotihuacán that emerges is a classic picture of positive feedback among obsidian mining and working, trade, population growth, irrigation, and religious tourism. The thriving obsidian operation, for example, would necessitate more miners, additional manufacturers of obsidian tools, and additional traders to carry the goods to new markets. All this led to increased wealth, which in turn would attract more immigrants to Teotihuacán. The growing power of the elite, who controlled the economy, would give them the means to physically coerce people to move to Teotihuacán and serve as additions to the labor force. More irrigation works would have to be built to feed the growing population, and this resulted in more power and wealth for the elite.

    ### Sample 2:
    topic: The extinction of the dinosaurs is believed to have been caused by a massive asteroid impact that drastically altered Earth’s climate and disrupted the food chain, leading to their rapid demise.
    text: Extinction of the Dinosaurs
    Paleontologists have argued for a long time that the demise of the dinosaurs was caused by climatic alterations associated with slow changes in the positions of continents and seas resulting from plate tectonics. Off and on throughout the Cretaceous (the last period of the Mesozoic era, during which dinosaurs flourished), large shallow seas covered extensive areas of the continents. Data from diverse sources, including geochemical evidence preserved in seafloor sediments, indicate that the Late Cretaceous climate was milder than today’s. The days were not too hot, nor the nights too cold. The summers were not too warm, nor the winters too frigid. The shallow seas on the continents probably buffered the temperature of the nearby air, keeping it relatively constant.
    At the end of the Cretaceous, the geological record shows that these seaways retreated from the continents back into the major ocean basins. No one knows why. Over a period of about 100,000 years, while the seas pulled back, climates around the world became dramatically more extreme: warmer days, cooler nights; hotter summers, colder winters. Perhaps dinosaurs could not tolerate these extreme temperature changes and became extinct.
    If true, though, why did cold-blooded animals such as snakes, lizards, turtles, and crocodiles survive the freezing winters and torrid summers? These animals are at the mercy of the climate to maintain a livable body temperature. It’s hard to understand why they would not be affected, whereas dinosaurs were left too crippled to cope, especially if, as some scientists believe, dinosaurs were warm-blooded. Critics also point out that the shallow seaways had retreated from and advanced on the continents numerous times during the Mesozoic, so why did the dinosaurs survive the climatic changes associated with the earlier fluctuations but not with this one? Although initially appealing, the hypothesis of a simple climatic change related to sea levels is insufficient to explain all the data.
    Dissatisfaction with conventional explanations for dinosaur extinctions led to a surprising observation that, in turn, has suggested a new hypothesis. Many plants and animals disappear abruptly from the fossil record as one moves from layers of rock documenting the end of the Cretaceous up into rocks representing the beginning of the Cenozoic (the era after the Mesozoic). Between the last layer of Cretaceous rock and the first layer of Cenozoic rock, there is often a thin layer of clay. Scientists felt that they could get an idea of how long the extinctions took by determining how long it took to deposit this one centimeter of clay and they thought they could determine the time it took to deposit the clay by determining the amount of the element iridium (Ir) it contained.
    Ir has not been common at Earth’s surface since the very beginning of the planet’s history. Because it usually exists in a metallic state, it was preferentially incorporated in Earth’s core as the planet cooled and consolidated. Ir is found in high concentrations in some meteorites, in which the solar system’s original chemical composition is preserved. Even today, microscopic meteorites continually bombard Earth, falling on both land and sea. By measuring how many of these meteorites fall to Earth over a given period of time, scientists can estimate how long it might have taken to deposit the observed amount of Ir in the boundary clay. These calculations suggest that a period of about one million years would have been required. However, other reliable evidence suggests that the deposition of the boundary clay could not have taken one million years. So the unusually high concentration of Ir seems to require a special explanation.
    In view of these facts, scientists hypothesized that a single large asteroid, about 10 to 15 kilometers across, collided with Earth, and the resulting fallout created the boundary clay. Their calculations show that the impact kicked up a dust cloud that cut off sunlight for several months, inhibiting photosynthesis in plants; decreased surface temperatures on continents to below freezing; caused extreme episodes of acid rain; and significantly raised long-term global temperatures through the greenhouse effect. This disruption of the food chain and climate would have eradicated the dinosaurs and other organisms in less than fifty years.

    ### Sample 3:
    topic: {topic}
    text:
    """
    generated_content = model.generate_content(prompt)
    generated_text = generated_content.text
    print(f"Generated TOEFL Reading Text about {topic}")
    
    return generated_text

"""# Step 3: Generate Questions

    - Take amount of the question types as {question_types_count} from user.,
    - Use the {generated_text},  {question_types_count} and Prompt Engineering to generate 10 TOEFL Reading Questions.
    - save the generated 10 TOEFL Reading Questions as {generated_questions}

There are 10 types in TOEFL Reading Question Types.

	  Basic Information and Inferencing questions:
 			1. Factual Information questions (2 to 5 questions per set)
 			2. Negative Factual Information questions (0 to 2 questions per set)
 			3. Inference questions (1 to 2 questions per set)
 			4. Rhetorical Purpose questions (1 to 2 questions per set)
 			5. Vocabulary questions (1 to 2 questions per set)
 			6. Reference questions (0 to 2 questions per set)
 			7. Sentence Simplification question (0 or 1 question per set)
 			8. Insert Text question (1 question per set)
 		Reading to Learn questions (1 per set):
			9. Prose Summary
 		  10. Fill in a Table

### Take amount of the question types
"""

def question_types_count(prose_summary_or_fill_table, factual_information_questions, negative_factual_information_questions, inference_questions, rhetorical_purpose_questions, vocabulary_questions, reference_questions, sentence_simplification_question, insert_text_question):
    # Define the question types and their counts
    question_types_count = {
        "Prose Summary or Fill in a Table": prose_summary_or_fill_table,
        "Insert Text": insert_text_question,
        "Factual Information": factual_information_questions,
        "Negative Factual Information": negative_factual_information_questions,
        "Inference": inference_questions,
        "Rhetorical Purpose": rhetorical_purpose_questions,
        "Vocabulary": vocabulary_questions,
        "Reference": reference_questions,
        "Sentence Simplification": sentence_simplification_question
    }
    print("Question types and counts:", question_types_count)
    
    return question_types_count


def generate_question(generated_text, question_types_count):
    prompt = f"""
    Use the provided text and the question types count to generate `10` TOEFL Reading-style questions. The questions should test a variety of skills, including vocabulary, reference, sentence simplification, and prose summary.

    #### Text:
    {generated_text}

    #### Question Types and Counts:
    {question_types_count}

    Ensure that all questions are related to the content and meaning of the passage and that answer choices are relevant and challenging.

    ### Output Format:
    Generate questions with the following structure:
    1.**Question**: [The question itself]"\n\n"
        A) [Choice A]"\n"
        B) [Choice B]"\n"
        C) [Choice C]"\n"
        D) [Choice D]"\n"

    """

    response = model.generate_content(prompt)
    generated_questions = response.text
    print("TOEFL Reading Questions Generated")
    
    return generated_questions

"""# Step 4: Generate Answers and Explanations of each question

    - Use the {generated_text} and {generated_questions} to generate Answers AND Explanations of each question.
    - save the generated Answers and Explanations of each question as {generated_answers_explanations}

### Fine tune Gemini-1.5 model with Question-Explanation dataset on Google AI Studio

![question-explanation-googleaistudio.png](attachment:question-explanation-googleaistudio.png)
"""

def generate_explanations_answers(generated_text, generated_questions):
    model2 = genai.GenerativeModel("tunedModels/questionexplanation-bmsqw4oa8ml2")

    prompt = f"""
    Use the {generated_text} and {generated_questions} to generate Answers AND Explanations of each question.

    ### Sample:
    text:
    THE ORIGINS OF CETACEANS
    It should be obvious that cetaceans—whales, porpoises, and dolphins—are mammals...
    ...
    (This sample text can continue for any necessary context in the same format as you had above)

    questions:
    1. According to the passage, all of the following were effects of the Industrial Revolution EXCEPT:
    A. Increased rural population
    B. Urbanization
    C. Poor living conditions in cities
    D. Technological advancements
    ...
    (Make sure this continues with all the questions you’d like as part of the sample for formatting guidance)

    explanations and answers:
    Explanation: The passage explicitly states that the Industrial Revolution led to urbanization and technological advancements. It also mentions the negative consequences of rapid urbanization, such as overcrowding and poor living conditions. However, it does not mention an increase in rural population. In fact, the opposite occurred as people migrated from rural areas to urban centers.
    Answer: A

    ###Output:
    text: {generated_text}
    questions: {generated_questions}
    explanations and answers:

    """

    response = model2.generate_content(prompt)
    generated_explanations_answers = response.text
    print("Explanations and Answers Generated")
    
    return generated_explanations_answers


"""# Step 5: Save all outputs in a pdf document

    - save all outputs in a pdf document with the order belov:
        {generated_text},
        {generated_questions},
        {generated_explanations_answers},
        {question_types_count}
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_toefl_pdf(generated_text, generated_questions, generated_explanations_answers, question_types_count, pdf_path="TOEFL_Reading_Content.pdf"):
    """
    Generate a PDF containing TOEFL reading content, questions, answers, and question type counts.

    Parameters:
    - generated_text (str): The text content for the TOEFL reading passage.
    - generated_questions (str): The generated TOEFL questions.
    - generated_explanations_answers (str): Explanations and answers for the questions.
    - question_types_count (dict): A dictionary containing the counts of each question type.
    - pdf_path (str): Path to save the generated PDF (default is 'TOEFL_Reading_Content.pdf').

    Returns:
    - str: Path of the saved PDF file.
    """

    # Save the output PDF file
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)

    # Define styles
    styles = getSampleStyleSheet()
    style_heading = styles['Heading1']
    style_text = styles['BodyText']

    # Add content to the document
    content = []

    # Ensure that generated_text is a string
    if hasattr(generated_text, 'content'):
        generated_text_str = generated_text.content  # If it's a Markdown object
    else:
        generated_text_str = str(generated_text)  # Fallback to string conversion

    # Add generated text
    content.append(Paragraph("TOEFL Reading Text:", style_heading))
    cleaned_text = generated_text_str.replace("## ", "")
    content.append(Paragraph(cleaned_text, style_text))
    content.append(Spacer(1, 12))

    # Ensure generated_questions is a string
    if hasattr(generated_questions, 'content'):
        generated_questions_str = generated_questions.content  # If it's a Markdown object
    else:
        generated_questions_str = str(generated_questions)  # Fallback to string conversion

    # Add generated questions
    content.append(Paragraph("TOEFL Reading Questions:", style_heading))
    for question in generated_questions_str.split('\n'):
        cleaned_question = question.replace("## TOEFL Reading Questions:", "").replace("**", "")
        content.append(Paragraph(cleaned_question, style_text))
    content.append(Spacer(1, 12))

    # Ensure generated_explanations_answers is a string
    if hasattr(generated_explanations_answers, 'content'):
        generated_explanations_answers_str = generated_explanations_answers.content  # If it's a Markdown object
    else:
        generated_explanations_answers_str = str(generated_explanations_answers)  # Fallback to string conversion

    # Add explanations and answers
    content.append(Paragraph("Explanations and Answers:", style_heading))
    for explanation in generated_explanations_answers_str.split('\n'):
        cleaned_explanation = explanation.replace("## Explanations and Answers", "").replace("**", "").replace("*", "")
        content.append(Paragraph(cleaned_explanation, style_text))
    content.append(Spacer(1, 12))

    # Add question types count
    content.append(Paragraph("Question Types Count:", style_heading))
    for qtype, count in question_types_count.items():
        content.append(Paragraph(f"{qtype}: {count}", style_text))

    # Build PDF
    doc.build(content)
    print(f"PDF saved at: {pdf_path}")
    
    return pdf_path


'''# Step 6: User Interface'''
'''
topic = input("Please enter a topic: ")
generated_text = generate_toefl_text(topic)

# Initialize counters and remaining questions
counter = 0
number_of_remaining_questions = 10

# Fixed question
insert_text_question = 1
counter += insert_text_question
number_of_remaining_questions -= insert_text_question

# Prose Summary or Fill in a Table
prose_summary, fill_in_a_table = 0, 0
prose_summary_OR_fill_in_a_table = input(f"(Number of remaining questions {number_of_remaining_questions}.) Prose Summary or Fill in a Table question (only one of the two question types for each set). Please write either 'p' for Prose Summary or 'f' for Fill in a Table: ")
if prose_summary_OR_fill_in_a_table == "p":
    prose_summary = 1
    fill_in_a_table = 0
elif prose_summary_OR_fill_in_a_table == "f":
    prose_summary = 0
    fill_in_a_table = 1
counter += prose_summary + fill_in_a_table
number_of_remaining_questions -= 1

# Collect and validate input for each question type
factual_information_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Factual Information questions (2 to 5 questions per set). Please write a number from 2 to 5: "))
counter += factual_information_questions
number_of_remaining_questions -= factual_information_questions

negative_factual_information_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Negative Factual Information questions (0 to 2 questions per set). Please write a number from 0 to 2: "))
counter += negative_factual_information_questions
number_of_remaining_questions -= negative_factual_information_questions

inference_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Inference questions (1 to 2 questions per set). Please write a number from 1 to 2: "))
counter += inference_questions
number_of_remaining_questions -= inference_questions

rhetorical_purpose_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Rhetorical Purpose questions (1 to 2 questions per set). Please write a number from 1 to 2: "))
counter += rhetorical_purpose_questions
number_of_remaining_questions -= rhetorical_purpose_questions

vocabulary_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Vocabulary questions (1 to 2 questions per set). Please write a number from 1 to 2: "))
counter += vocabulary_questions
number_of_remaining_questions -= vocabulary_questions

reference_questions = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Reference questions (0 to 2 questions per set). Please write a number from 0 to 2: "))
counter += reference_questions
number_of_remaining_questions -= reference_questions

sentence_simplification_question = int(input(f"(Number of remaining questions {number_of_remaining_questions}.) Sentence Simplification question (0 or 1 question per set). Please write a number from 0 to 1: "))
counter += sentence_simplification_question
number_of_remaining_questions -= sentence_simplification_question

question_types_count = question_types_count(prose_summary_OR_fill_in_a_table, factual_information_questions, negative_factual_information_questions, inference_questions, rhetorical_purpose_questions, vocabulary_questions, reference_questions, sentence_simplification_question)

generated_questions = generate_question(generated_text, question_types_count)

generated_explanations_answers= generate_explanations_answers(generated_text, generated_questions)

generate_toefl_pdf(generated_text, generated_questions, generated_explanations_answers, question_types_count, pdf_path="TOEFL_Reading_Content.pdf")

generated_questions = generate_question(generated_text, question_types_count)

generated_explanations_answers= generate_explanations_answers(generated_text, generated_questions)

generate_toefl_pdf(generated_text, generated_questions, generated_explanations_answers, question_types_count, pdf_path="TOEFL_Reading_Content.pdf")
''' 