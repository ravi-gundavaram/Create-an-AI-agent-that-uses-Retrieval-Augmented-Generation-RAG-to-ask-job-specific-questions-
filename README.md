# AI Interview Agent Using RAG and GPT-4

## Overview
This project is an AI-driven interview agent that uses **Retrieval-Augmented Generation (RAG)** with **GPT-4** to generate interview questions and evaluate responses. The system takes a job description and a resume, retrieves relevant information, and then generates personalized interview questions. It can also evaluate candidate responses based on predefined questions.

The application uses the following technologies:
- **GPT-4** from OpenAI for question generation and response evaluation.
- **LangChain** for building RAG (retrieval and generation) pipelines.
- **FAISS** for efficient vector-based similarity search.
- **Streamlit** for creating a user-friendly web interface.
- **Selenium** (optional) for LinkedIn profile scraping to enrich the context.

## Features
- Generate job-specific interview questions using a job description and candidate resume.
- Use Retrieval-Augmented Generation (RAG) to improve question relevance.
- Evaluate candidate responses and provide feedback on a scale of 1-10.
- Deployable using **Streamlit Community Cloud** with a live public URL.

## Technologies Used
- **Python 3.10+**
- **OpenAI GPT-4**
- **LangChain Community Libraries**
- **FAISS** for document retrieval
- **Streamlit** for the web interface
- **Selenium** for LinkedIn profile integration (optional)
- **Webdriver-Manager** to manage ChromeDriver

## Prerequisites
- **Python 3.10 or above** should be installed.
- A valid **OpenAI API key** to use GPT-4.
- **Google Chrome** installed for Selenium web scraping.
- **GitHub** account for deployment (for Streamlit Community Cloud).

## Installation

### Clone the Repository
First, clone this repository to your local machine:
```sh
git clone <repository-url>
cd Agent-RAG-LLM-GPT-BERT-Code
Create a Virtual Environment
Create and activate a virtual environment to manage dependencies:

python -m venv env
# For Windows
env\Scripts\activate
# For Linux/macOS
source env/bin/activate
Install Dependencies
Install all the required Python dependencies using pip:

pip install -r requirements.txt
The requirements.txt should contain:

openai
streamlit
PyPDF2
langchain-community
langchain-openai
faiss-cpu
selenium
webdriver-manager
linkedin-scraper
Setting Up the OpenAI API Key
Make sure your OpenAI API key is set as an environment variable:

export OPENAI_API_KEY="your-openai-api-key"
On Windows PowerShell, use:

$env:OPENAI_API_KEY="your-openai-api-key"
Alternatively, you can add this in a .env file and load it in the script using the dotenv library (optional).

Running the Application Locally
To run the application locally, execute:

streamlit run app.py
This will open your browser, and the app will be available at http://localhost:8501.

Deployment on Streamlit Community Cloud
To deploy your application on Streamlit Community Cloud:

Push Your Code to GitHub: Make sure all the files (app.py, requirements.txt, etc.) are pushed to a public GitHub repository.

Create a Streamlit Community Cloud Account:

Sign up or log in at Streamlit Community Cloud.
Link your GitHub repository.
Configure the deployment settings and secrets:
Add OPENAI_API_KEY under Secrets for security.
Deploy: After configuration, deploy the application. Streamlit will provide a public URL to access the application.

Project Structure

Agent-RAG-LLM-GPT-BERT-Code/
├── app.py               # Main Streamlit application script
├── requirements.txt     # Python dependencies
├── env/                 # Virtual environment folder (optional)
└── README.md            # This readme file
Usage Instructions
Enter Job Description:

Paste the job description in the provided text area.
Upload Resume:

Upload the candidate's resume as a PDF or TXT file.
Generate Interview Questions:

Click on "Generate Interview Questions" to receive personalized questions generated using the job description and resume.
Evaluate Responses:

Enter a specific interview question and the candidate's response.
Click on "Evaluate Response" to get a score and feedback based on the quality of the answer.
Optional: LinkedIn Profile Integration
This feature allows you to provide more personalized interview questions by scraping a candidate's LinkedIn profile:

LinkedIn Scraping:
Provide the LinkedIn profile URL.
Selenium will use the webdriver-manager to initialize ChromeDriver and extract profile information like experience and education.
Prerequisites for LinkedIn Integration
Google Chrome must be installed.
ChromeDriver should be managed using webdriver-manager to avoid version mismatches.
LinkedIn Usage Warning
Please ensure you comply with LinkedIn's terms of service when scraping profiles. Unauthorized scraping may violate the terms and result in your account being restricted or banned.

Troubleshooting
Common Issues and Fixes
Deprecation Warnings: If you encounter LangChain deprecation warnings, ensure that you are using the latest imports:

python

from langchain_openai import OpenAIEmbeddings
WebDriver executable_path Error:

Ensure that you use the updated WebDriver initialization:
python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
OpenAI Authentication:

Ensure the API key is set correctly as an environment variable.
Logs and Debugging
Use the Streamlit console logs to check for any errors.
For WebDriver issues, ensure that ChromeDriver is installed and compatible with your Chrome browser version.
Future Enhancements
User Authentication: Add user authentication to control access to the application.
Advanced Evaluation: Improve the evaluation mechanism using a fine-tuned GPT model.
Save and Export: Add functionality to save generated questions and evaluations as PDF/CSV files.
Multi-Language Support: Expand support for generating questions in different languages.
License
This project is licensed under the MIT License.

Credits
OpenAI for GPT-4.
LangChain for RAG and retrieval utilities.
FAISS for vector-based similarity search.
Streamlit for a simple, interactive UI.
Selenium for LinkedIn integration.
Contact
For further questions, reach out via:

Email: ravi.gundavarapudevops@gmail.com
GitHub: GitHub Profile
