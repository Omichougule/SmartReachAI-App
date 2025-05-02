__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader



from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.markdown("""
    <style>
    .main-title {
        font-size: 36px;
        font-weight: 800;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 24px;
        color: #555;
        font-style: italic;
    }
    .description {
        font-size: 16px;
        color: #333;
        line-height: 1.5;
    }
    </style>
""", unsafe_allow_html=True)

    st.markdown('<div class="main-title">📫 SmartReachAI</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI-Powered Personalized Email Generator for Lead Acquisition</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">🚀 Automate Lead Generation Process by reaching Product Based Companies with smart, tailored emails.</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">📎 Email includes service-based industry\'s <b>project portfolio links</b> matching to the product company\'s job description.</div>', unsafe_allow_html=True)
    st.markdown('<div class="description">🌐 Supports <i>multiple languages</i> and <i>industries</i> with contextual accuracy.</div>', unsafe_allow_html=True)

    #st.title("📫 SmartReachAI")
    #st.subheader("AI-Powered Personalized Email Generator for Lead Acquisition")
    #st.markdown("#### Automate Lead Generation Process by reaching Product Based Companies with smart, tailored emails. ")
    #st.markdown("##### Email includes service based industry's Project Portolio links matching to the product based company's job description.")
    #st.markdown("###### Supports multiple languages and industries with contextual accuracy.")
    st.sidebar.title("⚙️ Settings")

    language = st.sidebar.selectbox("Select Email Language", ("English", "Spanish", "French"))
    url_input = st.text_input("Enter a URL:", value="https://careers.nike.com/senior-software-engineer/job/R-59014")
    #language = st.text_input("In which language would you like the email to be drafted? (e.g., German, English, French): ",value="English")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links, language)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Smart Email Generator", page_icon="📫")
    create_streamlit_app(chain, portfolio, clean_text)
