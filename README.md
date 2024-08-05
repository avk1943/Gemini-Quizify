# Gemini Quizify

Gemini Quizify is an AI-powered quiz platform crafted to offer students and learners an interactive way to solidify their grasp of different subjects. Using advanced AI, the tool generates quizzes from documents users provide, giving immediate feedback and thorough explanations to aid in better understanding and memory retention, thereby enriching the learning process.

## Project Objective

There is a lack of accessible and effective means for students and learners to reinforce their understanding of various topics. Recognizing the challenge of obtaining timely feedback and engaging in unlimited practice, the team is developing an AI-generated assessment and quiz tool. This tool aims to provide users with instant feedback and comprehensive explanations, thus facilitating deeper comprehension and retention of knowledge. By dynamically generating quizzes based on user-provided documents, ranging from textbooks to scholarly papers, the tool offers a tailored learning experience. The end result will be a user-friendly platform that empowers individuals to hone their skills, solidify their understanding, and ultimately excel in their academic pursuits.

## Features

- **AI-Generated Assessments and Quizzes:** Utilizing artificial intelligence, the tool will dynamically generate quizzes and assessments based on user-provided documents, such as textbooks and scholarly papers.
- **Instant Feedback:** Users will receive immediate feedback on their quiz performance, allowing them to quickly identify areas of strength and areas needing improvement.
- **Comprehensive Explanations:** Detailed explanations will be provided for each question, enabling users to understand the reasoning behind correct answers and learn from mistakes.
- **Tailored Learning Experience:** The quizzes will be customized to the content of the user-provided documents, ensuring relevance and alignment with the topics being studied.

## Technologies Used

- **Python** serves as the foundational language for crafting Gemini Quizify's backend logic.
- **Langchain** is harnessed for proficient natural language processing, empowering the tool to adeptly understand and dissect textual content.
- **Chromadb** stands as the robust database management system, ensuring swift storage and retrieval of user data and quiz content.
- **Google** Gemini plays a pivotal role in AI-driven content analysis and generation, enabling the tool to dynamically craft quizzes from user-supplied documents.
- **Streamlit** enriches the user experience by facilitating the creation of interactive web applications with Python, enhancing the accessibility and usability of Gemini Quizify.

## Project Workflow

Using scripts, the following tasks are implemented.

1. **Document Processing**: Utilizing Google Gemini for document processing.
2. **Text Embeddings**: Generating embeddings with Langchain.
3. **Authentication**: Integrating Google Service Account for secure API access.
4. **PDF Ingestion**: Loading documents using a PDF loader.
5. **User Interface**: Building an interface with Streamlit.
6. **Quiz Generation**: Creating quizzes based on user-specified topics.
7. **Answer Explanations**: Providing detailed explanations for quiz answers.
8. **Navigation Controls**: Implementing navigation within the quiz interface.
9. **Error Handling**: Ensuring robust error handling and validation.
10. **Deployment**: Considering packaging and deployment strategies.

![Implementation Workflow](https://github.com/user-attachments/assets/f788b527-31bf-47b6-be34-3560520e1966)

## Installation

To set up the Quiz Builder:

1. Clone the repository:
   ```bash
   git clone <repository-url>

2. Navigate to the project directory:

3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
3. Replace Project ID with Unique Project ID from desired AI model (In this model vertex AI Google Gemini was used over google cloud server)

## Usage

To run the Quiz Builder:

1. Start the Streamlit application:
   ```bash
    streamlit run <your_script>.py

Replace <your_script> with the name of the Python script you want to run.

Follow the instructions in the Streamlit interface to interact with the Quiz Builder.

## Acknowledgments

This project is based on [mission-quizify](https://github.com/radicalxdev/mission-quizify), developed by [radicalxdev](https://github.com/radicalxdev). We thank them for providing the foundation for this project.

- [Radical AI](https://www.radicalai.org/) - For providing the challenges and inspiration.
