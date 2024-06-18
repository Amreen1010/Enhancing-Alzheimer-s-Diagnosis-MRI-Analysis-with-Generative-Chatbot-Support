TEAM_MEMBERS = [
    {"name": "Amreen", "role": "Developer", "links":["https://www.linkedin.com/in/amreen-rafiq-a35119229?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app"]},
]
EMOJI = "C:/Users/ASHWIN M/Alzheimers_Prediction_System-main/assets/images/emo.webp"
import streamlit as st


def team_members():
    st.markdown(f"<h1 style='text-align:center;'>Developed by</h1>", unsafe_allow_html=True)
    st.markdown("<br><br><div class='team-container'>", unsafe_allow_html=True)

    for member in TEAM_MEMBERS:
        st.markdown(
            f"""
            <div class='team-member'>
                <a href={member['links'][0]} target="_blank">
                    <h3 style='text-align:center;'>{member['name']}</h3>
                    <p>{member['role']}</p>
                </a>
            </div>
            <br>
            """,
            unsafe_allow_html=True
        )

    st.markdown("</div>", unsafe_allow_html=True)




        