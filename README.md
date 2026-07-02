# Resume Screening

This project is a simple AI-powered resume screening application. A user uploads a resume PDF and a job description, and the app uses an LLM to analyze the match and generate a structured screening report.

## What this project does

- Accepts a resume in PDF format
- Accepts a job description as a text file or pasted text
- Extracts text from the resume
- Sends the resume and job description to a Groq LLM
- Returns a structured report with:
  - match score
  - skill comparison
  - strengths and weaknesses
  - final recommendation

## Project structure

- app.py: Streamlit web app entry point
- requirements.txt: Python dependencies
- src/config/file_loader.py: utility to read text files
- src/data_ingestion/data_loader.py: PDF text extraction logic
- src/llm/llm.py: prompt building and LLM integration
- src/prompts/prompt.md: prompt template used for the AI analysis
- data/job_description/sample_JD.txt: sample job description
- data/resume/: sample resume files (if available)

## Tech stack

- Python
- Streamlit
- PyPDF2
- Groq API
- python-dotenv

## Prerequisites

Make sure you have the following installed:

- Python 3.9 or higher
- pip
- Git

## Setup locally

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd Resume-screening
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a environment file
   Create a file named .env in the project root and add your Groq API key:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Run the application

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## How to use the app

1. Open the app in your browser
2. Upload a resume PDF
3. Upload a job description text file or paste the job description
4. Click Analyze Resume
5. Review the generated screening report

## Sample data

You can test the app using the sample files in:

- data/job_description/sample_JD.txt

## Development notes

If you are working on this project, the main files to edit are:

- app.py for the UI flow
- src/llm/llm.py for model call behavior
- src/prompts/prompt.md for the LLM prompt structure
- src/data_ingestion/data_loader.py if resume parsing needs changes

## Troubleshooting

- If the app fails to start, make sure all dependencies are installed.
- If the LLM call fails, verify that your Groq API key is set correctly in the .env file.
- If the resume is not parsed correctly, check the PDF file and the PDF extraction logic in src/data_ingestion/data_loader.py.

## Notes

This project currently expects the LLM to return a JSON response that matches the structure used by the Streamlit report rendering in app.py.
