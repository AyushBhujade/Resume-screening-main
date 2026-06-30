from groq import Groq
from dotenv import load_dotenv
from src.config.file_loader import file_loader
from src.data_ingestion.data_loader import pdf_loader
import re
import json
import os

load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def load_prompt_template(template_path):
    """
    Load a prompt template from a Markdown file.

    Args:
        template_path (str): The path to the Markdown file containing the prompt template.

    Returns:
        str: The loaded prompt template.
    """
    return file_loader(template_path)

def parse_resume(resume_data, job_description):
    """
    Parse the resume data and job description to generate a response using the LLM.

    Args:
        resume_data (str): The text content of the resume.
        job_description (str): The text content of the job description.

    """
    prompt=load_prompt_template("src/prompts/prompt.md")
    formatted_prompt = (
        prompt
        .replace("<<JOB_DESCRIPTION>>", job_description)
        .replace("<<RESUME_DATA>>", resume_data)
    )
    return formatted_prompt

def extract_json(raw_text: str) -> dict:
    text = raw_text.strip()

    # Remove ```json ... ``` or ``` ... ``` fences if present
    text = re.sub(r"^```(?:json)?\s*", "", text)
    text = re.sub(r"\s*```$", "", text)
    text = text.strip()

    return json.loads(text)

def ask_llm(resume_data,job_description):
    prompt = parse_resume(resume_data, job_description)
    response = groq_client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    extracted_json = extract_json(response.choices[0].message.content)
    return extracted_json


