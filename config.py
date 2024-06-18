import streamlit as st

# PAGE CONFIG
CSS = open("styles.css", 'r').read()


# ASSETS
BACKGROUND = "bg.webp"

DEFAULT_IMAGE = "default.webp"
SIDE_BANNER = "side_banner.webp"
EMOJI = "emo.webp"

# PREDICTION PAGE
APOE_CATEGORIES = ['APOE Genotype_2,2', 'APOE Genotype_2,3', 'APOE Genotype_2,4', 
                   'APOE Genotype_3,3', 'APOE Genotype_3,4', 'APOE Genotype_4,4']
PTHETHCAT_CATEGORIES = ['PTETHCAT_Hisp/Latino', 'PTETHCAT_Not Hisp/Latino', 'PTETHCAT_Unknown']
IMPUTED_CATEGORIES = ['imputed_genotype_True', 'imputed_genotype_False']
PTRACCAT_CATEGORIES = ['PTRACCAT_Asian', 'PTRACCAT_Black', 'PTRACCAT_White']
PTGENDER_CATEGORIES = ['PTGENDER_Female', 'PTGENDER_Male']
APOE4_CATEGORIES = ['APOE4_0', 'APOE4_1', 'APOE4_2']
ABBREVIATION = {
                "AD": "Alzheimer's Disease ",
                "LMCI": "Late Mild Cognitive Impairment ",
                "CN": "Cognitively Normal"
            }

CONDITION_DESCRIPTION = {
    "AD": "This indicates that the individual's data aligns with characteristics commonly associated with "
        "Alzheimer's disease. Alzheimer's disease is a progressive neurodegenerative disorder that affects "
        "memory and cognitive functions.",
    "LMCI": "This suggests that the individual is in a stage of mild cognitive impairment that is progressing "
            "towards Alzheimer's disease. Mild Cognitive Impairment is a transitional state between normal "
            "cognitive changes of aging a   nd more significant cognitive decline.",
    "CN": "This suggests that the individual has normal cognitive functioning without significant impairments. "
        "This group serves as a control for comparison in Alzheimer's research."
}

# NEWS PAGE
NEWS_API_KEY = st.secrets["NEWS_API"]
KEYWORD = "alzheimer"


# CHATBOT PAGE
HF_EMAIL = st.secrets['HF_EMAIL']
HF_PASS = st.secrets['HF_PASS']    
BASE_PROMPT = st.secrets['BASE_PROMPT']


# TEAM MEMBERS PAGE
TEAM_MEMBERS = [
    {"name": "Name", "role": "Developer", "links":["Linkedin_link", "Github_Link"]},
]
