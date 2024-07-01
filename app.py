from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
CURRENT_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = CURRENT_DIR / "styles" / "main.css"
ASSET = CURRENT_DIR / "assets"
RESUME = ASSET / "CV_Lucas_PASCAL_data.pdf"
PROFILE_PICTURE = ASSET / "profile-pic.png"
FAVICON_PATH = ASSET / "favicon.ico"
SOFTWARE_REPU_PATH = ASSET / "software_republique.jpeg"
SOFTWARE_REPU_2_PATH = ASSET / "software_repu_2.jpeg"
HOLIDAYS_PATH = ASSET / "holidays.jpg"
HOLIDAYS_PATH = ASSET / "india.jpg"
SAIL_PATH = ASSET / "sail.jpg"

FAVICON_IMG = Image.open(FAVICON_PATH)

# --- GENERAL Setting ---
PAGE_TITLE = "Digital CV  |  Lucas PASCAL"
PAGE_ICON = FAVICON_IMG
NAME= "Hi, I'm Lucas :wave:"
DESCRIPTION = """
I am a French Data Scientist consultant.
"""
EMAIL = "lucas_pascal@aol.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/lucas222pascal",
    "GitHub":"https://github.com/Luzartug",
    "Kaggle":"https://www.kaggle.com/luzartug"
    }

PROJECTS = {
    "🏦 Société Générale: Market Risk Variation Algorithm Explanation":"http://lucaspascal.com",
    "👀 End-to-end data pipeline integrates monitoring, data and model versioning (mlflow), and CI/CD processes (Docker)":"https://github.com/Luzartug/ML_pipeline",
    "📚 A RAG system uses a locally quantized Mistral model and llama-ccp to analyze and interpret the French Work Laws":"https://github.com/Luzartug/local_lawyer_bot/tree",
    "🧠 Psychologue Asistant: Conversational (text and speech) chatbot with emotional analysis":"https://github.com/Luzartug",
    "🎧 Podcast Analysis: Summarize of a podcast, keyword search and word cloud graph":"https://github.com/Luzartug",
    "🏆 Hackathon Winner 🏆: Vigil'Auto: In-vehicle solution using ML and generative AI to predict driver under influence and provide real-time alerts": "https://github.com/julesrubin/VigilAuto",
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
        I have previous experiences as a Software/Data Engineer for Eurostar, as Data/AI Scientist in finance for Société Générale and in consulting (Equancy, Groupe EDG).\n
        I've lived in Paris, in London and Phnom Penh.\n
        My education is in engineering, data science and business management (EFREI, Panthéon Assas University).\n
        When my laptop is closed, I am also a passionate sailer and swimmer.
        """)

# --- HARD SKILLS ---
st.write("\n")
st.subheader("Hard & soft skills")
st.write(
    """
    - 💻 **Programming**: Python, SQL, Spark
    - 🤖 **Gen AI**: LangChain (LCEL), LangSmith, RAG (Weaviate, LlamaIndex...), Fine-tuning
    - 📚 **Data Science**: Pandas, NumPy, Scikit-Learn, SciPy, PyTorch, Streamlit
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
st.write("🌆", "**Data/AI Scientist | Paris, France | Equancy, EDG Groupe**")
st.write("03/2024 - 09/2024")
st.write(
    """
    - → Adapted an image generation model for Vinci Airport marketing materials 
    - → Developed a model to forecast Nespresso Group's capsule sales
    - → Created a generative AI app, using techniques like RAGs, Chains and Agents
    """
)

# --- JOB 2
st.write("\n")
st.write("📈", "**Data Scientist | Paris, France | Société Générale**")
st.write("11/2022 - 03/2023")
st.write(
    """
    - → Developed an NLP-based prototype to enhance automated insights for financial risk analysts
    """
)

# --- JOB 3
st.write("\n")
st.write("📈", "**Software/Data Engineer | London, UK | Eurostor Int.**")
st.write("11/2022 - 03/2023")
st.write(
    """
    - → Developed and deployed new features for the rebranding of Eurostar.com (merged with Thalys)
    - → Extracted and formatted Jira data from the API for the analyst team
    - → Hackathon Winner : proof of concept that allows customers to visualize their seats in 3D
    """
)

# --- JOB 4
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
    
software_repu_1 = Image.open(SOFTWARE_REPU_PATH)
software_repu_2 = Image.open(SOFTWARE_REPU_2_PATH)
st.image(software_repu_1)
st.image(software_repu_2)

# --- EXTRA WORK ---
st.write("\n")
st.subheader("Extra work - Hobbies")
st.write("---")
india = Image.open(HOLIDAYS_PATH)
sail = Image.open(SAIL_PATH)
st.image(sail)
st.image(india)