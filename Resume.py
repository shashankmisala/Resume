from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shashank Misala"
PAGE_ICON = ":wave:"
NAME = "Shashank Misala"
DESCRIPTION = """ STUDENT """
EMAIL = "misala.shashank@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/shashank-misala/",
    "GitHub": "https://github.com/",
}
PROJECTS = {
    "🏆 Fake News Detector  ": "https://fake-news-detector-by-shashank-misala.streamlit.app/",
    "🏆 Movie Recommendation Engine with API ": "https://github.com/shashankmisala/Movie-Recommendation-System",
    "🏆 Book Recommendation Engine ": "https://github.com/shashankmisala/Book-Recommendation-System",
    "🏆 Chat GPT Clone Using Streamlit and OpenAi API": "https://github.com/shashankmisala/Chat-GPT-Clone",
    "🏆 Song Recommendation System Using K-Means Clustering": "https://spotify-recommendation-system-kmeans.streamlit.app/",


}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col2:
    st.image(profile_pic, width=230)

with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Education")
st.write(
    """
- => Brown University - (July '23 - Aug '23)
  -  AI, Machine Learning and Data Science
- => Narayana Institute - (March - '21 - May - '23)
  -  Grades - 11 & 12
- => International Educational Academy - (March '13 - March '20 ) 
  -  Grades - 3rd - 10th
"""
)



# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python , HTML , CSS , JavaScript , R(Programming Language)
- 📊 Data Visulization: MS Excel, Plotly , Matplotlib , Seaborn , Tableau
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MongoDB, MySQL
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
