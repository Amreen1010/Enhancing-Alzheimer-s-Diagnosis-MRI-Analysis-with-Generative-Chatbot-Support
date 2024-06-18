import streamlit as st
import base64
HOME_BACKGROUND = "brain.jpg"
def set_page_background(png_file):
    @st.cache_data
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bin_str}");
            background-size: cover;
        }}
        </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    

def login_page():
    st.title("Login Page")
    set_page_background(HOME_BACKGROUND)
     
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Define your username and password here
    correct_username = "Usernaame"
    correct_password = "Password"
    
    if st.button("Login"):
        # Perform authentication logic here
        if username == correct_username and password == correct_password:
            st.success("Logged in successfully!")
            # Set session variable to indicate authentication status
            st.session_state.logged_in = True
        else:
            st.error("Invalid username or password")
