from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume = current_dir / "assets/CV_Lucas_PASCAL.pdf"
picture = current_dir / "assets/profile-pic.png"

# --- GENERAL Setting ---
PAGE_TITLE = "Digital CV  |  Lucas PASCAL"
PAGE_ICON = "🌊"
NAME= "Lucas PASCAL :wave:"
DESCRIPTION = """
I am in a last year Master in Data and AI, looking for a 6-months final internship as **Data Scientist Intern**.
"""
EMAIL = "lucas.pascal.internship@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/lucas222pascal",
    "GitHub":"https://github.com/Luzartug",
    "Kaggle":"https://www.kaggle.com/luzartug",
    "Instagram":"https://www.instagram.com/"
}
PROJECTS = {
    "🏦 Société Générale: Market Risk Variation Algorithm Explanation":"https://wholesale.banking.societegenerale.com/en/solutions/investment-banking/",
    "👀 Streamlit for Netflix Users":"https://github.com/Luzartug",
    "🧠 Psychologue Asistant: Conversational (text and speech) chatbot with emotional analysis":"https://github.com/Luzartug",
    "⛑️ E-Reputation analysis on TWITTER":"https://github.com/Luzartug",
    "🎧 Podcast Analysis: Summarize of a podcast, keyword search and word cloud graph":"https://github.com/Luzartug"
}
CERTIFICATION ={
    "AZ-900 certified : Azure Fundamentals":"https://www.credly.com/badges/6603caeb-7e02-4ad3-96be-048357487799/linked_in_profile",
    "AI-900 certified : Azure AI Fundamentals":"https://www.credly.com/badges/fe94c44c-4607-49c3-89af-0022d8972c59/linked_in_profile",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.write("#")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}<style>".format(f.read()), unsafe_allow_html=True)
with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(picture)

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
        file_name=resume.name,
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
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔︎ Creating dashboards and predictive models to monitor KPIs for 2 companies
    - ✔︎ Passionate about digital and data: **web analytics, programmatic, Datalake, dataviz, data science**
    - ✔︎ Good understanding of statistical and their respective applications
    - ✔︎ Strong interest in data project for marketing & business issues
    - ✔︎ Excellent team-player and displaying strong sense of initiative on tasks
    """ 
)

# --- HARD SKILLS ---
st.write("\n")
st.subheader("Hard & soft skills")
st.write(
    """
    - 💻 Programming: **SQL**, **Javascript** and **Python**
    - 📊 Data Visualisation: **Streamlit, Plotly, Matplotlib, Seaborn & PowerBI**
    - 📚 **Data Science: Machine / Deep Learning, Statistical analysis, computing**
    - 💽 Databases: mySQL, MongoDB, ElastikSearch
    """
)
st.write(
    """  
    - 📡 Good Communication 
    - 🚀 Consistently aiming for excellence
    - 📚 Complexe problem solving
    - 🎙️ Vulgarization
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
st.write("📈", "**Data Analyst Intern | London, UK | Eurostor Int.**")
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

# --- JOB 2
st.write("\n")
st.write("🦠", "**Hotline Health Consultant | Orsay, France | French Health Agency (ARS)**")
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
