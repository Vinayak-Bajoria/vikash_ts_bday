import streamlit as st
import time

# Initialize session state
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.show_content = False
    st.session_state.music_playing = False

# Set page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Define background images
initial_bg = "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNmppenRxZGZjbW9hZXg0amF4bHN5eGJ6Mmw5dzkzM3M2N3o5N3g0MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fI8R1Q7EuHWJLcSadC/giphy.gif"
pooja_bg = "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHoxMWJiMTRuOXlvcDNtaHFsZXFqZjg2Zno0ZnUxY3owcXlvYXB2ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3GKxWq8XL00A4g2h3R/giphy.gif"

# Choose background based on music state
image_url = pooja_bg if st.session_state.music_playing else initial_bg

# CSS for background
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        transition: background-image 0.5s ease-in-out;
    }}
    
    /* Hide sidebar completely */
    [data-testid="stSidebar"] {{
        display: none;
    }}
    
    /* Hide sidebar collapse button */
    button[kind="header"] {{
        display: none;
    }}
    
    /* Fade-in animation */
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    .fade-in {{
        animation: fadeIn 2s ease;
    }}
    
    /* Make ALL buttons transparent with no border */
    div.stButton > button {{
        background-color: transparent !important;
        border: none !important;
        color: white !important;
        font-size: 18px !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        animation: fadeIn 2s ease;
        text-shadow: 2px 2px 4px black;
    }}
    
    div.stButton > button:hover {{
        background-color: rgba(255, 255, 255, 0.2) !important;
        transform: scale(1.05);
    }}
    
    /* Specific styling for center primary button */
    div[data-testid="stHorizontalBlock"]:has(button[kind="primary"]) button {{
        font-size: 20px !important;
        padding: 15px 30px !important;
    }}
    
    /* Hide audio player */
    .stAudio {{
        display: none;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Calculate elapsed time
elapsed_time = time.time() - st.session_state.start_time

# Check if content should be shown
if elapsed_time >= 2:
    st.session_state.show_content = True

# Display countdown if content isn't ready to show
if not st.session_state.show_content:
    # Display countdown
    remaining_time = max(0, 2 - elapsed_time)
    
    # Center the countdown
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            f"""
            <div style="text-align: center; color: white; font-size: 24px; text-shadow: 2px 2px 5px black;">
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Rerun to update countdown
    time.sleep(0.1)
    st.rerun()
else:
    # Audio file URL
    github_audio_url = "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/pooja_audio.mp3"
    
    # Play audio if music button was clicked
    if st.session_state.music_playing:
        st.audio(github_audio_url, format='audio/mp3', autoplay=True, loop=True)
    
    # Add spacing
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    
    # Centered transparent button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Big boss chahte h aap yaha dabaye ! 😁", type="primary", use_container_width=True):
            st.switch_page("pages/2_Surprise.py")
    
    # Add more spacing to push button to bottom
    st.markdown("<br><br><br><br><br><br>", unsafe_allow_html=True)
    
    # Music control button in bottom right
    col_empty1, col_empty2, col_music = st.columns([3, 1, 1])
    with col_music:
        if st.button("Jyada chul h toh yaha dabaye"):
            st.session_state.music_playing = True
            st.rerun()  # Force rerun to update background