import streamlit as st
import time
import streamlit.components.v1 as components
import random

# --- GIF cycling (background) ---
if "gif_idx" not in st.session_state:
    st.session_state.gif_idx = 0
    st.session_state.gif_start = time.time()

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

gifs = [
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXF5c296c216OXVwenA1Zm5wdXJhbjRsNWh4OHR4djA3anc5MW0xNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wzXztwFQrHfHw2gK4d/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeThrNm0xbmZ1MDl3MG9sZTBzNWI2eGJ1YXhweHZpaXUyZTR3b3duNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/UV4VbvnURq4MNlc0LU/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTFnbTk2cWE4d3c5YXhtdHJ1dm80aG42cHk3aTYxMWhoeW1leWZ3YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BpbVZC5u3jmyYSxD62/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTFnbTk2cWE4d3c5YXhtdHJ1dm80aG42cHk3aTYxMWhoeW1leWZ3YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5jDrXDhXA9yST3jNEy/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTFnbTk2cWE4d3c5YXhtdHJ1dm80aG42cHk3aTYxMWhoeW1leWZ3YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UV4VbvnURq4MNlc0LU/giphy.gif",
]

if time.time() - st.session_state.gif_start >= 2:
    st.session_state.gif_idx = (st.session_state.gif_idx + 1) % len(gifs)
    st.session_state.gif_start = time.time()
    st.rerun()

current_gif = gifs[st.session_state.gif_idx]

# --- Audio playlist (hidden) ---
audio_urls = [
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Ophelia.mp3",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/alltoowell.mp4",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Physical%20Audio.mp3",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Dancing%20Alone.mp3",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Keep%20Watching%20Audio.mp3",
]

audio_html = f"""
<audio id="a" preload="auto" style="display:none;">
  <source src="{audio_urls[0]}" type="audio/mpeg">
</audio>
<script>
  const pl = {audio_urls};
  let i = 0;
  const a = document.getElementById('a');
  const trimS = 5, trimE = 5;
  function play(){{
    a.src = pl[i]; a.load();
    a.onloadedmetadata = ()=>{{
      a.currentTime = trimS;
      a.play().catch(e=>console.log(e));
    }};
  }}
  a.ontimeupdate = ()=>{{
    if (a.currentTime >= a.duration-trimE){{ i=(i+1)%pl.length; play(); }}
  }};
  play();
</script>
"""
components.html(audio_html, height=0)

# --- Image carousel setup ---
image_urls = [
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/vik_bday.jpeg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4663.PNG",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4956.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4958.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4959.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4960.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4961.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4962.jpg",
    "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/IMG_4963.jpg",
]

if "img_idx" not in st.session_state:
    st.session_state.img_idx = 0

def prev_img():
    st.session_state.img_idx = (st.session_state.img_idx - 1) % len(image_urls)
    st.rerun()

def next_img():
    st.session_state.img_idx = (st.session_state.img_idx + 1) % len(image_urls)
    st.rerun()

current_img = image_urls[st.session_state.img_idx]

# --- Quiz configuration (update captions to whatever you need) ---
quiz_questions = [
    {
        "id": "q1",
        "prompt": "Which of these iconic aunty matches your vibesssss?",
        "options": [
            {"label": "Bharwi aunty", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.35.35.png"},
            {"label": "Chai pi lo", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.38.59.png"},
            {"label": "Rasode m kaun tha?", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.43.56.png"},
            {"label": "Uska pati sirf mera h", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.46.51.png"},
        ],
    },
    {
        "id": "q2",
        "prompt": "Which of these is the most iconic taylor swift line?",
        "options": [
            {"label": "Nothing lasts forever, but this is gonna take me down", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.54.25.png"},
            {"label": "And you're tossing out blame, drunk on this pain, crossing out the good years", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2010.59.15.png"},
            {"label": "And I never knew I could feel that much", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.01.30.png"},
            {"label": "Now all he thinks about is me", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.03.26.png"},
        ],
    },
    {
        "id": "q3",
        "prompt": "Pick the most iconic flashback from Big Boss",
        "options": [
            {"label": "baap p jana nahi", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.15.22.png"},
            {"label": "bigg boss mujhe hurt ho raha h", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.15.53.png"},
            {"label": "pooja aap aise dustbin nai phek sakte", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.16.22.png"},
            {"label": "Shut up, how dare you!", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.14.35.png"},
        ],
    },
    {
        "id": "q4",
        "prompt": "Which one of these is most outrageous Kardashian line?",
        "options": [
            {"label": "She's just pissed because she's married to a barking dog", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.35.01.png"},
            {"label": "Kim would you stop taking pictures of yourself, your sister's going to jail", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.35.01.png"},
            {"label": "I'm sick of you. You think you're hot shit because you have the biggest ass in LA", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.35.01.png"},
            {"label": "I could literally slap the shit out of you and feel so much better.", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.35.01.png"},
        ],
    },
    {
        "id": "q5",
        "prompt": "I know there are many but among these which is motherr's best work?",
        "options": [
            {"label": "Cats movie", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.50.06.png"},
            {"label": "Fate of Ophelia", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.49.45.png"},
            {"label": "Look what you made me do", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.49.18.png"},
            {"label": "All Too Well", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.48.57.png"},
        ],
    },
    {
        "id": "q6",
        "prompt": "Finally, which one of these is your future child?",
        "options": [
            {"label": "josh talks", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.57.51.png"},
            {"label": "mera papa scooter dho rahe", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.58.16.png"},
            {"label": "dun dun dun dun", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.58.41.png"},
            {"label": "in do aankhon se kitna dekha ja sakta tha", "image": "https://raw.githubusercontent.com/Vinayak-Bajoria/streamlit_apps/main/Screenshot%202025-10-31%20at%2011.59.22.png"},
        ],
    },
]

feedback_messages = [
    "Wow. Just... wow.",
    "Big brain, huh?",
    "Nice one, Einstein.",
    "Classic. Real smooth.",
    "Oh, brilliant idea.",
    "A+ stupidity right there.",
    "Top-tier genius move.",
    "Peak intelligence.",
    "Amazing. Truly pathetic.",
    "Congrats, you played yourself.",
    "Oh, that’s science, alright.",
    "Yeah, that’ll totally work.",
    "Beautiful disaster.",
    "Flawless logic, really.",
    "Galaxy brain moment.",
    "This is dumb 101.",
    "Oh look, evolution in reverse.",
    "Incredible.",
    "Wow, revolutionary nonsense.",
    "Oh yeah, real  material.",
    "Oh, smart move, genius.",
    "Yeah, that’s gonna end well.",
    "Big brain strikes again.",
    "Real five-star thinking.",
    "Spectacular failure, 10/10.",
    "Like watching a car crash in slow motion.",
    "Oh yeah, science approves this nonsense.",
    "Another day, another dumb idea.",
    "Bravo, you broke the simulation.",
    "Wow, my IQ just left the room."
]


taylor_albums = [
    {
        "name": "Fearless",
        "quote": "\"Cause when you’re fifteen and somebody tells you they love you, you’re gonna believe them.\" — Fifteen"
    },
    {
        "name": "Speak Now",
        "quote": "\"Don’t say yes, run away now.\" — Speak Now"
    },
    {
        "name": "Red",
        "quote": "\"You call me up again just to break me like a promise.\" — All Too Well"
    },
    {
        "name": "1989",
        "quote": "\"He’s so tall and handsome as hell, he’s so bad but he does it so well.\" — Wildest Dreams"
    },
    {
        "name": "Reputation",
        "quote": "\"The world moves on, another day, another drama — but not for me, all I think about is karma.\" — Look What You Made Me Do"
    },
    {
        "name": "Lover",
        "quote": "\"Can I go where you go? Can we always be this close forever and ever?\" — Lover"
    },
    {
        "name": "Folklore",
        "quote": "\"I knew you, stepping on the last train, marked me like a bloodstain.\" — The 1"
    },
    {
        "name": "Evermore",
        "quote": "\"What must it be like to grow up that beautiful, with your hair falling into place like dominoes?\" — Dorothea"
    },
    {
        "name": "Midnights",
        "quote": "\"It's me, hi, I'm the problem, it's me.\" — Anti-Hero"
    },
    {
        "name": "The Tortured Poets Department",
        "quote": "\"You know you’re special, I know it’s true.\" — Fortnight (feat. Post Malone)"
    },
    {
        "name": "Fearless",
        "quote": "\"But you’ll always be my thunderstorm, and I’ll always be your girl.\" — Forever & Always"
    },
    {
        "name": "Speak Now",
        "quote": "\"People like me are gone forever when you say goodbye.\" — Last Kiss"
    },
    {
        "name": "Red",
        "quote": "\"We are never ever ever getting back together.\" — We Are Never Ever Getting Back Together"
    }
]



if "quiz_answers" not in st.session_state:
    st.session_state.quiz_answers = {}

# --- CSS for cards and quiz ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    .stApp {{
        background: url({current_gif}) center/cover no-repeat fixed;
        transition: background 1s ease-in-out;
    }}
    [data-testid="stSidebar"], button[kind="header"] {{display: none !important;}}

    .card-wrapper {{
        background: rgba(255,255,255,0.15) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
        padding: 32px !important;
        margin: 20px 0 !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        min-height: 450px !important;
        width: 65% !important;
        margin-left: 0 !important;
        margin-right: auto !important;
    }}

    .card-wrapper .text-card-content {{
        color: #ffffff !important;
        font-family: 'proxima-nova', 'Proxima Nova', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-style: italic !important;
        font-weight: 400 !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7) !important;
        line-height: 1.7 !important;
        letter-spacing: 0.5px !important;
    }}
    
    .card-wrapper .text-card-content p {{
        margin: 0 0 1.2rem 0 !important;
        color: #ffffff !important;
        font-size: 1.1rem !important;
        opacity: 0.95 !important;
        font-style: italic !important;
        font-family: 'proxima-nova', 'Proxima Nova', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    }}

    .card-wrapper [data-testid="stMarkdownContainer"] {{
        color: #ffffff !important;
        font-family: 'proxima-nova', 'Proxima Nova', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-style: italic !important;
    }}

    .card-wrapper [data-testid="stMarkdownContainer"] p {{
        color: #ffffff !important;
        font-family: 'proxima-nova', 'Proxima Nova', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        font-style: italic !important;
        font-size: 1.1rem !important;
        line-height: 1.7 !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7) !important;
        margin-bottom: 1.2rem !important;
    }}

    div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) {{
        background: rgba(255,255,255,0.15) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
        padding: 32px !important;
        margin: 20px 0 !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        min-height: 450px !important;
        display: flex !important;
        align-items: center !important;
    }}

    #carousel-card-anchor {{display: none !important;}}

    div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) div[data-testid="column"] {{
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) div[data-testid="column"] > div[data-testid="stVerticalBlock"] {{
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }}

    div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) img {{
        max-height: 350px !important;
        max-width: 100% !important;
        object-fit: contain !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.18) !important;
    }}

    [data-testid="stButton"] > button {{
        background: rgba(255,255,255,0.22) !important;
        border: none !important;
        border-radius: 50% !important;
        width: 48px !important;
        height: 48px !important;
        font-size: 1.8rem !important;
        color: #fff !important;
        cursor: pointer !important;
        opacity: 0.85 !important;
        transition: all 0.3s !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
        flex-shrink: 0 !important;
    }}
    [data-testid="stButton"] > button:hover {{
        background: rgba(255,255,255,0.45) !important;
        opacity: 1 !important;
        transform: scale(1.1) !important;
    }}

    .quiz-card {{
        background: rgba(255,255,255,0.15) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 18px !important;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3) !important;
        padding: 28px !important;
        margin: 24px 0 !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }}

    .quiz-card h3 {{
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
        margin-bottom: 18px !important;
    }}

    .quiz-option {{
        text-align: center !important;
        color: #ffffff !important;
        font-family: 'Montserrat', sans-serif !important;
    }}

    .quiz-option img {{
        width: 100% !important;
        height: 160px !important;
        object-fit: cover !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 16px rgba(0,0,0,0.18) !important;
        margin-bottom: 12px !important;
    }}

    .quiz-option span {{
        display: inline-block !important;
        margin-top: 4px !important;
        font-weight: 600 !important;
    }}

    .quiz-card [data-testid="stButton"] > button {{
        display: block !important;
        margin: 12px auto 0 !important;
        background: rgba(255, 215, 0, 0.2) !important;
        border: 1px solid #ffd700 !important;
        border-radius: 20px !important;
        padding: 8px 16px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        width: auto !important;
        min-width: auto !important;
        transition: all 0.3s ease !important;
    }}

    .quiz-card [data-testid="stButton"] > button:hover {{
        background: rgba(255, 215, 0, 0.4) !important;
        transform: none !important;
    }}

    .selected-indicator {{
        text-align: center !important;
        margin-top: 12px !important;
        font-size: 1.8em !important;
        color: #ffd700 !important;
        font-weight: bold !important;
        font-family: 'Montserrat', sans-serif !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
    }}

    .stAlert {{display: none !important;}}

    .quiz-top-gap {{
        height: 240px;
    }}

    @media (max-width: 900px) {{
        .card-wrapper {{
            min-height: auto !important; 
            padding: 20px !important;
        }}
        div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) {{
            min-height: auto !important;
            padding: 20px !important;
        }}
        div[data-testid="stVerticalBlock"]:has(> #carousel-card-anchor) img {{
            max-height: 250px !important;
        }}
        .text-card-content p {{font-size: 1rem !important;}}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Layout: Side-by-side columns ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="card-wrapper">
            <div class="text-card-content">
                <p>As this music fades from pop to something serene 🎶🌅</p>
                <p>I wish your life ahead includes both experiences: working hard and playing hard, as well as calm, restful days, each bringing peace in its own way. 💪🧘‍♂️</p>
                <p>To your 28th year round the sun</p>
                <p>Happy Birthday Vikash 🥳🎂</p>
                <p>Love,</p>
                <p>Vinayak</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div id="carousel-card-anchor"></div>', unsafe_allow_html=True)
        left_col, center_col, right_col = st.columns([1, 8, 1], gap="small", vertical_alignment="center")
        with left_col:
            if st.button("‹", key="prev"):
                prev_img()
        with center_col:
            st.image(current_img, use_container_width=True)
        with right_col:
            if st.button("›", key="next"):
                next_img()

# --- Quiz section ---
st.markdown('<div class="quiz-top-gap"></div>', unsafe_allow_html=True)
st.markdown("# Take this quiz to find your Taylor Swift album, cutooooo")

for idx, question in enumerate(quiz_questions, start=1):
    st.markdown(
        f"""
        <div class="quiz-card">
            <h4>{question['prompt']}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if f"selected_{question['id']}" not in st.session_state:
        st.session_state[f"selected_{question['id']}"] = -1

    selected_idx = st.session_state[f"selected_{question['id']}"]

    option_cols = st.columns(len(question["options"]), gap="medium")

    for i, option in enumerate(question["options"]):
        with option_cols[i]:
            is_selected = (selected_idx == i)
            dull_filter = "filter: grayscale(100%) !important; opacity: 0.6 !important;" if not is_selected else ""
            highlight_border = "border: 3px solid #ffd700 !important; box-shadow: 0 0 20px rgba(255,215,0,0.5) !important;" if is_selected else ""
            img_style = f"width: 100% !important; height: 160px !important; object-fit: cover !important; border-radius: 12px !important; box-shadow: 0 4px 16px rgba(0,0,0,0.18) !important; margin-bottom: 12px !important; {dull_filter} {highlight_border}"
            caption_style = f"text-align: center !important; color: #ffffff !important; margin: 8px 0 16px 0 !important; font-weight: 600 !important; font-size: 0.9rem !important; {'color: #ffd700 !important; font-weight: bold !important;' if is_selected else ''}"

            col_container = st.container()
            with col_container:
                st.markdown(
                    f"""
                    <div class="quiz-option">
                        <img src="{option['image']}" alt="{option['label']}" style="{img_style}">
                        <p style="{caption_style}">{option['label']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if not is_selected:
                    btn_left, btn_center, btn_right = st.columns([1.5, 2, 0.5], gap="small")
                    with btn_center:
                        if st.button("", key=f"select_{question['id']}_{i}"):
                            st.session_state[f"selected_{question['id']}"] = i
                            st.session_state.quiz_answers[question['id']] = option['label']
                            st.session_state[f"feedback_{question['id']}"] = random.choice(feedback_messages)
                            st.rerun()
                else:
                    message = st.session_state.get(f"feedback_{question['id']}", "Wow. Just... wow.")
                    st.markdown(
                        f'<div class="selected-indicator">{message}</div>',
                        unsafe_allow_html=True,
                    )

all_answered = all(st.session_state.get(f"selected_{q['id']}") != -1 for q in quiz_questions)

if all_answered:
    if "ts_album_result" not in st.session_state:
        st.session_state.ts_album_result = random.choice(taylor_albums)

    album = st.session_state.ts_album_result
    st.markdown(
        f"""
        <div class="quiz-card" style="border: 2px solid #ffd700;">
            <h3 style="color:#ffd700; text-align:center;">Your Taylor Swift album is:</h3>
            <h2 style="color:#ffffff; text-align:center; margin-bottom:0.5rem;">{album['name']}</h2>
            <p style="color:#ffffff; text-align:center; font-style:italic;">{album['quote']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("🔁", key="retake_quiz"):
        for question in quiz_questions:
            st.session_state[f"selected_{question['id']}"] = -1
            st.session_state.pop(f"feedback_{question['id']}", None)
        st.session_state.quiz_answers = {}
        st.session_state.pop("ts_album_result", None)
        st.rerun()