import streamlit as st

from forms.contact import contact_form

@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("assets/julie.png", width=230)
with col2:
    st.title("Julie Powers", anchor=False)
    st.write(
        "Surprise, M'lady. Yes, I do. It's black... and it beats for you. Te Veo."
    )
    if st.button("💋 Contact Me"):
        show_contact_form()

# --- SECTION 1 ---
st.write("\n")
st.subheader("Surprise, M'lady", anchor=False)
st.write(
    """
    - Mamma mia, here I go again
    - My my how can I resist you?
    - Mamma mia, does it show again?
    - My my how can I let you go?
    """
)

# --- SECTION 2 ---
st.write("\n")
st.subheader("Surprise, M'lady", anchor=False)
st.write(
    """
    - Mamma mia, here I go again
    - My my how can I resist you?
    - Mamma mia, does it show again?
    - My my how can I let you go?
    """
)

# --- HERO SECTION ---
st.write("\n")
col1, col2 = st.columns(2, gap="small", vertical_alignment="bottom")
with col2:
    st.image("assets/julie.png", width=230)
with col1:
    st.title("Julie Powers", anchor=False)
    st.write(
        "Surprise, M'lady. Yes, I do. It's black... and it beats for you. Te Veo."
    )
    