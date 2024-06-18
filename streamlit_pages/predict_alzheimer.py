import time
import joblib
import pandas as pd
CSS = open("C:\\Users\\ASHWIN M\\Alzheimers_Prediction_System-main\\assets\\css\\styles.css", 'r').read()


# ASSETS
BACKGROUND = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/bg.webp"

DEFAULT_IMAGE = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/default.webp"
SIDE_BANNER = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/side_banner.webp"
EMOJI = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/emo.webp"

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
KEYWORD = "alzheimer"
# TEAM MEMBERS PAGE
TEAM_MEMBERS = [
    {"name": "Amreen", "role": "Developer", "links":["https://www.linkedin.com/in/arpitsengar", "https://github.com/arpy8"]},
]
import streamlit as st

def prediction_page():
    def convert_to_one_hot(selected_category, all_categories):
            one_hot = [True if category == selected_category else False for category in all_categories]
            for value in one_hot:
                user_input.append(value)

    def predict_alzheimer(input_data):
        loaded_model = joblib.load('model/alzheimer_model.pkl')
        predictions = loaded_model.predict(input_data)

        return predictions

    st.title("Patient Information")

    age = st.number_input("Age", min_value=0, max_value=122, step=1, value=65)
    gender = st.selectbox("Gender", ("Male", "Female"))
    education = st.number_input("Years of Education", min_value=0, value=12)

    st.write("<br>", unsafe_allow_html=True)

    st.header("Demographics")
    ethnicity = st.radio("Ethnicity", ("Hisp/Latino", "Not Hisp/Latino", "Unknown"))
    race_cat = st.radio("Race Category", ("White", "Black", "Asian"))

    st.write("<br>", unsafe_allow_html=True)

    st.header("Genetic Information")
    apoe_allele_type = st.selectbox("APOE Allele Type", ["APOE4_0", "APOE4_1", "APOE4_2"])
    apoe_genotype = st.selectbox("APOE4 Genotype", ("2,2", "2,3", "2,4", "3,3", "3,4", "4,4"))
    imputed_genotype = st.radio("Imputed Genotype", ("True", "False"))

    st.header("Cognitive Assessment")
    mmse = st.number_input("MMSE Score", min_value=0, max_value=30, step=1)

    st.write("<br>", unsafe_allow_html=True)
    predict_button = st.button("Predict")
    st.write("")

    loading_bar = st.empty()
    if age and education and mmse and apoe_genotype and race_cat and gender and apoe_allele_type and imputed_genotype and ethnicity and predict_button:
        loading_bar.write("Thank you for entering the patient's information.")
        progress_text = "Please wait, we're predicting your clinical condition..."
        my_bar = loading_bar.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.02)
            my_bar.progress(percent_complete + 1, text=progress_text)

        user_input = [age, education, mmse]

        convert_to_one_hot("PTRACCAT_" + race_cat, PTRACCAT_CATEGORIES)
        convert_to_one_hot("APOE Genotype_" + apoe_genotype, APOE_CATEGORIES)
        convert_to_one_hot("PTETHCAT_" + ethnicity, PTHETHCAT_CATEGORIES)
        convert_to_one_hot(apoe_allele_type, APOE4_CATEGORIES)
        convert_to_one_hot("PTGENDER_" + gender, PTGENDER_CATEGORIES)
        convert_to_one_hot("imputed_genotype_" + imputed_genotype, IMPUTED_CATEGORIES)

        data = pd.DataFrame([user_input])
        predicted_condition = predict_alzheimer(data)
        
        loading_bar.empty()

        st.write("")
        st.write("")
        st.write("### Predicted Clinical Condition:", unsafe_allow_html=True)
        st.write(f"## <b>{ABBREVIATION[predicted_condition[0]]}</b> ({predicted_condition[0]})", unsafe_allow_html=True)
        st.write(f"{CONDITION_DESCRIPTION[predicted_condition[0]]}", unsafe_allow_html=True)
