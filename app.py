from pathlib import Path
import streamlit as st
from PIL import Image
from emoji import emojize

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume = current_dir / "assets/CV_Lucas_PASCAL.pdf"
picture = current_dir / "assets/profile-pic.png"

# --- GENERAL Setting ---
PAGE_TITLE = "Digital CV  |  Lucas PASCAL"
PAGE_ICON = emojize(":black_large_square:") 
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
    "👀 Streamlit for Netflix Users":"",
    "🧠 Psychologue Asistant: Conversational (text and speech) chatbot with emotional analysis":"",
    "⛑️ E-Reputation analysis on TWITTER":""
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.write("#")

# --- SIDE BAR ---
#st.sidebar.success("Select a demo above.")

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
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATION ---
st.write("#")
st.subheader("Experience & Qualifacations")
st.write(
    """
    - ✔︎ Creating dashboards and predictive models to monitor KPIs for 2 companies
    - ✔︎ Experience in data collection technology: **Google Analytics** & **SQL database**
    - ✔︎ Good understanding of statistical and their respective applications
    - ✔︎ Excellent team-player and displaying strong sense of initiative on tasks
    """ 
)

# --- SKILLS ---
st.write("#")
st.subheader("Hard skills")
st.write(
    """
    - 💻 Programming: **SQL**, **Javascript** and **Python (Scikit-learn, Pandas)**
    - 📊 Data Visualisation: **PowerBi, Excel, Streamlit**
    - 📚 Modeling: Logistic regresssion, linear regression, decition trees
    - 💽 Databases: mySQL, Postgres, MongoDB
    """
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("#")
st.write("🚄", "**Data Analyst Intern | London, UK | Eurostor Int.**")
st.write("11/2022 - 03/2023")
st.write(
    """
    - → Involved in the Delta Project, a major European merger in the sector, integrating Eurostar and Thalys to drive synergies 
    and enhance operational efficiency
    - → Rotation in every team of the IS sales Team (teams in charge of eurostar.com)
    - → Working with stakeholders across the Digital Product team
    - → Creating dashboards and predictive models to monitor KPIs of the company
    """
)

# --- JOB 2
st.write("#")
st.write("🏥", "**Hotline Health Consultant | Orsay, France | French Health Agency (ARS)**")
st.write("03/2020 - 06/2020")
st.write(
    """
    - → Worked during the first Covid-19 lockdown for the French Health Agency (ARS) on the 
    website “Terr-eSanté”: the French equivalent to the NHS website.
    """
)


# ---Projects & Accomplishements
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
