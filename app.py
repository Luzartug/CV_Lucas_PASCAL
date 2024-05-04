from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = CURRENT_DIR / "styles" / "main.css"
ASSET = CURRENT_DIR / "assets"
RESUME = ASSET / "CV_Lucas_PASCAL.pdf"
PROFILE_PICTURE = ASSET / "profile-pic.png"
FAVICON_PATH = ASSET / "favicon.ico"
FAVICON_IMG = Image.open(FAVICON_PATH)

# --- GENERAL Setting ---
PAGE_TITLE = "Digital CV  |  Lucas PASCAL"
PAGE_ICON = FAVICON_IMG
NAME= "Hi, I'm Lucas :wave:"
DESCRIPTION = """
I am a French ML Engineer consultant.
"""
EMAIL = "lucas_pascal@aol.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/lucas222pascal",
    "GitHub":"https://github.com/Luzartug",
    "Kaggle":"https://www.kaggle.com/luzartug",
    "Instagram":"https://www.instagram.com/"
}
PROJECTS = {
    "🏦 Société Générale: Market Risk Variation Algorithm Explanation":"https://wholesale.banking.societegenerale.com/en/solutions/investment-banking/",
    "👀 End-to-end data pipeline integrates monitoring, data and model versioning (mlflow), and CI/CD processes (Docker)":"https://github.com/Luzartug/ML_pipeline",
    "📚 A RAG system uses a locally quantized Mistral model and llama-ccp to analyze and interpret the French Work Laws":"https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006072050/",
    "🧠 Psychologue Asistant: Conversational (text and speech) chatbot with emotional analysis":"https://github.com/Luzartug",
    "🎧 Podcast Analysis: Summarize of a podcast, keyword search and word cloud graph":"https://github.com/Luzartug"
}
CERTIFICATION ={
    "AZ-900 certified : Azure Fundamentals":"https://www.credly.com/badges/6603caeb-7e02-4ad3-96be-048357487799/linked_in_profile",
    "AI-900 certified : Azure AI Fundamentals":"https://www.credly.com/badges/fe94c44c-4607-49c3-89af-0022d8972c59/linked_in_profile",
    "AWS Cloud Quest: Cloud Practitioner" : "https://www.credly.com/badges/555fc511-50c7-4a65-8718-71aeeb4a12c1/linked_in_profile"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.write("#")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(CSS_FILE) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(RESUME, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(PROFILE_PICTURE)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label= "📄 Download Resume",
        data = PDFbyte,
        file_name=RESUME.name,
        mime="application/octet-stream"
    )
    st.write("📩", EMAIL)

# --- SOCIAL LINKS ---
st.write("\n")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATION ---
st.write("\n")
st.subheader("About me")
st.write("""
        I have previous experiences as a software engineer (Eurostar), in finance (Société Générale), and data science consulting (Equancy, a data consulting agency).\n
        I've lived in Paris, in London and Phnom Penh.
        My education is in data science & engineering (EFREI, Panthéon Assas University) and business management.\n
        When my laptop is closed, I am also a passionate sailer and swimmer.
        """)

# --- HARD SKILLS ---
st.write("\n")
st.subheader("Hard & soft skills")
st.write(
    """
    - 💻 **Programming**: Python, SQL, Spark
    - 🤖 **Gen AI**: LangChain, LlamaIndex, RAG (Pinecone...), Fine-tuning (peft, LoRA)
    - 📚 **Data Science**: Pandas, NumPy, Scikit-Learn, SciPy, PyTorch, Streamlit/Dash
    - 🖥️ **ML/DevOps**: Git, Docker, Airflow, MLflow, DVC, Vertex, Bedrock, Azure-OpenAI
    - 💽 **Cloud**: Certifications ⬇️
    """
)

# --- CERTIF ---
st.write("\n")
st.subheader("Certifications")
for certif, link in CERTIFICATION.items():
    st.write(f"- ✅ [{certif}]({link})")


# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("\n")
st.write("🌆", "**AI Engineer | Paris, France | Equancy, EDG Groupe**")
st.write("03/2024 - 09/2024")
st.write(
    """
    - → Fine-tuning of Stable diffusion model in order to generate marketing content for Vinci Airport client
    - → Build a python package for feature selectors
    - → Build Gen AI app (RAGs, Chain and Agents)
    - → Creating a segmentation model for L'Oréal Professional
    """
)

# --- JOB 2
st.write("\n")
st.write("📈", "**Data Engineer | London, UK | Eurostor Int.**")
st.write("11/2022 - 03/2023")
st.write(
    """
    - → Involved in the Delta Project, a major European merger in the sector, integrating Eurostar and Thalys to drive synergies 
    and enhance operational efficiency
    - → Developed data-driven dashboards, improving promotional effectiveness by 15%
    - → Rotation in every team of the IS sales Team (teams in charge of eurostar.com)
    - → Creating predictive models to monitor KPIs of the company
    - → Working with stakeholders across the Digital Product team
    """
)

# --- JOB 3
st.write("\n")
st.write("🦠", "**Hotline Health Consultant | Paris, France | French Health Agency (ARS)**")
st.write("03/2020 - 06/2020")
st.write(
    """
    - → Worked during the first Covid-19 lockdown for the French Health Agency (ARS) on the 
    website “Terr-eSanté”: the French equivalent to the NHS website.
    """
)

# --- JOB 3
st.write("\n")
st.write("🧠", "**Science Teacher | Phnom Penh, Cambodia | Royal University of Phnom Penh**")
st.write("11/2019 - 06/2020")
st.write(
    """
    - → Interned in humanitarian field, designed physics practicals
    """
)


# ---Projects & Accomplishements
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
