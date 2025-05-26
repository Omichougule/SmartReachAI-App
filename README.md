# SmartReachAI

## Description

AI-Powered Personalized Email Generator for Lead Acquisition. SmartReachAI automates the lead generation process by crafting personalized emails tailored to product-based companies. It intelligently matches job descriptions with relevant projects from a service-based industry's portfolio, highlighting suitable expertise.

## Features

- Automated Lead Generation: Fetches job descriptions from URLs.
- Personalized Email Drafting: Generates tailored emails using Groq LLM (Llama 3.3 70B).
- Portfolio Matching: Utilizes ChromaDB vector store to find and include relevant portfolio project links based on extracted skills.
- Multi-lingual Support: Capable of drafting emails in multiple languages (e.g., English, Spanish, French).
- Web-Based UI: User-friendly interface built with Streamlit.

## How it Works

The user provides a URL (e.g., a job posting) and selects a desired language for the email.
The application fetches and cleans the content from the URL.
Job details (role, experience, skills, description) are extracted using a Groq LLM via Langchain.
The system queries a ChromaDB vector database (loaded from `resource/portfolio.csv`) to find portfolio projects matching the extracted skills.
A personalized email is drafted by the LLM, incorporating the job details and relevant portfolio links.
The generated email is displayed to the user.

## Tech Stack

- Python
- Streamlit (for the web UI)
- Langchain (for LLM orchestration)
- Groq (for Large Language Model access - Llama 3.3 70B)
- ChromaDB (for vector storage and similarity search of portfolio items)
- Pandas (for data manipulation, e.g., loading portfolio)
- NLTK (likely for text processing tasks, though specific use isn't detailed in main files, it's a common NLP library)
- BeautifulSoup4 (for HTML parsing, often used by WebBaseLoader)

## Setup and Usage

### Prerequisites

- Python 3.8+
- Git
- Access to Groq API and a GROQ_API_KEY

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```
   GROQ_API_KEY="your_groq_api_key_here"
   # Add other environment variables if any
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

   ```bash
   streamlit run main.py
   ```

## File Structure

```
.
├── .devcontainer/      # Development container configuration
├── .github/            # GitHub Actions workflows
├── resource/           # Resource files (e.g., portfolio.csv)
├── vectorstore/        # Vector store for embeddings
├── README.md           # This file
├── chains.py           # Core logic for Langchain chains
├── main.py             # Main Streamlit application
├── portfolio.py        # Portfolio management
├── requirements.txt    # Python dependencies
├── utils.py            # Utility functions
└── .env                # Environment variables (needs to be created locally)
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for bugs, features, or improvements.

## License

This project is currently unlicensed. 
```
