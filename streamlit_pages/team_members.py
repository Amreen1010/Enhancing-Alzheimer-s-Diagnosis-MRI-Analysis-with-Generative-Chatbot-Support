TEAM_MEMBERS = [
    {"name": "Name", "role": "Developer", "links":["your_link"]},
]
EMOJI = "emo.webp"
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




        
