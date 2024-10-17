import pickle
from pathlib import Path

import streamlit_authenticator as stauth
import streamlit as st

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

#load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "dashboard",
                "abcdef", cooke_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:

    # Function for the Dashboard page
    def show_dashboard():
        st.title("Dashboard")
        st.write("Welcome to the Dashboard!")
        st.write("Here you can find an overview of your data.")

    # Function for the History page
    def show_history():
        st.title("History")
        st.write("This is the History page.")
        st.write("You can view your previous records here.")

    # Function for the POS page
    def show_pos():
        st.title("POS (Point of Sale)")
        st.write("This is the POS page.")
        st.write("You can process transactions and sales here.")

    # Main App Logic
    def main():
        
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome {name}")

        # Store the current page in session state
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Dashboard"

        # Create buttons for each page
        if st.sidebar.button("Dashboard", key="dashboard_button" if st.session_state.current_page == "Dashboard" else None):
            st.session_state.current_page = "Dashboard"
            
        if st.sidebar.button("History", key="history_button" if st.session_state.current_page == "History" else None):
            st.session_state.current_page = "History"
            
        if st.sidebar.button("POS", key="pos_button" if st.session_state.current_page == "POS" else None):
            st.session_state.current_page = "POS"

        # Render the selected page content based on current_page
        if st.session_state.current_page == "Dashboard":
            show_dashboard()
        elif st.session_state.current_page == "History":
            show_history()
        elif st.session_state.current_page == "POS":
            show_pos()

    # Run the app
    if __name__ == "__main__":
        main()
