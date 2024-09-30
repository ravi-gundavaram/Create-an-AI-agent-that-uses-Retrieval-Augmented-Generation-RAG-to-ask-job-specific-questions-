import os
import openai
from PyPDF2 import PdfReader
import streamlit as st
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import UnstructuredFileLoader
from langchain.prompts import PromptTemplate

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI embeddings for retrieval
embeddings = OpenAIEmbeddings()

# Streamlit web application setup
st.title("AI Interview Agent Using RAG and GPT-4")

# Job description input
job_description_input = st.text_area("Enter Job Description")

# Resume file upload (supports PDF or TXT)
resume_input = st.file_uploader("Upload Resume", type=["pdf", "txt"])

# Load job description and resume documents into retriever
def load_documents(job_description, resume_text):
    with open("job_description.txt", "w") as f:
        f.write(job_description)
    with open("resume.txt", "w") as f:
        f.write(resume_text)

    loader = UnstructuredFileLoader(["job_description.txt", "resume.txt"])
    documents = loader.load()
    return documents

# Extract text from resume
def extract_resume_text(file):
    if file.type == "application/pdf":
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    else:
        return file.getvalue().decode("utf-8")

# Button to generate interview questions
if st.button("Generate Interview Questions"):
    if job_description_input and resume_input:
        resume_text = extract_resume_text(resume_input)
        documents = load_documents(job_description_input, resume_text)

        # Create FAISS vector store for fast similarity search
        document_store = FAISS.from_documents(documents, embeddings)

        # Create a retriever and an LLM chain for RAG
        retriever = document_store.as_retriever()
        llm = OpenAI(model="gpt-4")
        qa_chain = RetrievalQA(llm=llm, retriever=retriever)

        # Prompt template to generate personalized questions
        prompt_template = """
        You are an interview assistant. Based on the job description and resume, generate five personalized interview questions.
        Job Description: {job_description}
        Resume: {resume}
        Questions:
        """
        prompt = PromptTemplate(
            input_variables=["job_description", "resume"],
            template=prompt_template
        )
        query = prompt.format(job_description=job_description_input, resume=resume_text)

        # Run retrieval and LLM generation
        response = qa_chain.run(query)
        questions = response.strip().split("\n")
        st.write("Generated Interview Questions:")
        for i, question in enumerate(questions, 1):
            st.write(f"{i}. {question}")

# Input for a specific question and response for evaluation
question_input = st.text_input("Enter Question")
response_input = st.text_area("Enter Candidate Response")

# Function to evaluate the response
def evaluate_response(question, response):
    prompt = f"""
    Question: {question}
    Response: {response}

    Evaluate the response on a scale of 1 to 10 and provide feedback.
    """
    evaluation = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an evaluator."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return evaluation['choices'][0]['message']['content'].strip()

# Button to evaluate the response
if st.button("Evaluate Response"):
    if question_input and response_input:
        evaluation = evaluate_response(question_input, response_input)
        st.write("Evaluation:", evaluation)

from selenium import webdriver
from linkedin_scraper import Person, actions

# Set up Selenium WebDriver (Ensure you have the correct chromedriver installed)
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Function to extract LinkedIn profile details
def extract_linkedin_profile(profile_url):
    profile = Person(profile_url, driver=driver)
    experience = profile.experiences
    education = profile.educations
    return experience, education

