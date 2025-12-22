import streamlit as st
from datetime import date, datetime, timedelta
import random
from fpdf import FPDF
from PIL import Image
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="One Year With You ya NOUR ELHOUDA",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- PASSWORD PROTECTION ----------
PASSWORD = "290403"  # CHANGE THIS TO YOUR DESIRED PASSWORD

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;500;600&family=Dancing+Script:wght@600&display=swap');

        body {
            background: radial-gradient(circle at top, #ffe6f0 0%, #fff8fb 35%, #fdf3f3 70%, #f9f0f5 100%);
            font-family: 'Lora', serif;
        }
        .password-container {
            max-width: 420px;
            margin: 140px auto;
            padding: 40px 32px 32px 32px;
            background: rgba(255, 255, 255, 0.96);
            border-radius: 26px;
            box-shadow: 0 18px 55px rgba(168, 93, 110, 0.23);
            text-align: center;
            border: 1px solid rgba(212, 165, 176, 0.35);
            position: relative;
            overflow: hidden;
        }
        .password-container::before {
            content: '';
            position: absolute;
            width: 220px;
            height: 220px;
            background: radial-gradient(circle, rgba(255,192,203,0.35), transparent 60%);
            top: -80px;
            right: -40px;
            opacity: 0.7;
        }
        .password-title {
            font-family: 'Playfair Display', serif;
            font-size: 38px;
            color: #a85d6e;
            margin-bottom: 8px;
        }
        .password-heart {
            font-size: 32px;
            margin-bottom: 10px;
            animation: heartbeat 1.5s ease-in-out infinite;
        }
        .password-subtitle {
            font-size: 17px;
            color: #7a6a72;
            margin-bottom: 26px;
            font-style: italic;
            line-height: 1.5;
        }
        .password-input-label {
            font-size: 14px;
            color: #8a7680;
            margin-bottom: 6px;
        }
        .password-hint {
            margin-top: 16px;
            font-size: 13px;
            color: #b494a2;
            font-style: italic;
        }

        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.15); }
            40% { transform: scale(0.98); }
            60% { transform: scale(1.08); }
        }

        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="password-container">', unsafe_allow_html=True)
    st.markdown('<div class="password-heart">❤️</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="password-title">Just For You</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="password-subtitle">This little corner of the internet belongs to you.<br>'
        'Enter our secret to step inside, a 3ayniya.</p>',
        unsafe_allow_html=True
    )

    st.markdown('<div class="password-input-label">Our secret password</div>', unsafe_allow_html=True)
    password_input = st.text_input("Password", type="password", label_visibility="collapsed")

    if st.button("Open our world"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.success("WELCOME TO THE NORMAD EXPERIENCE.")
            st.rerun()
        else:
            st.error("Incorrect password. Try again, a chaba ❤️")

    st.markdown(
        '<div class="password-hint">hint : its your birthday</div>',
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

    # Restore scroll position after refresh
st.markdown(
    """
    <script>
    // Restore scroll position after page loads
    window.onload = function() {
        const savedPosition = localStorage.getItem('scrollPosition');
        if (savedPosition) {
            window.scrollTo(0, parseInt(savedPosition));
            localStorage.removeItem('scrollPosition');
        }
    }
    </script>
    """,
    unsafe_allow_html=True
)

# ---------- CALCULATE TIME TOGETHER AND KNOWN EACH OTHER ----------
def calculate_time_together():
    """Calculate time since December 20, 2024 12:21 AM"""
    start_date_together = datetime(2024, 12, 20, 0, 21, 0)
    now = datetime.now()
    delta = now - start_date_together
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes

def calculate_time_known():
    """Calculate time since May 5, 2023"""
    start_date_known = datetime(2023, 5, 5, 22, 2, 0)
    now = datetime.now()
    delta = now - start_date_known
    
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes

def calculate_next_anniversary():
    """Calculate days until next anniversary (Dec 20)"""
    now = datetime.now()
    current_year = now.year
    
    # If current date is past Dec 20, next anniversary is next year
    if now.month > 12 or (now.month == 12 and now.day >= 20):
        next_anniversary = datetime(current_year + 1, 12, 20, 0, 0, 0)
    else:
        next_anniversary = datetime(current_year, 12, 20, 0, 0, 0)
    
    delta = next_anniversary - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return days, hours, minutes

# ---------- CUSTOM CSS WITH ROMANTIC AESTHETIC ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;500;600&family=Dancing+Script:wght@600&display=swap');

    body {
        background: radial-gradient(circle at top, #ffe6f0 0%, #fff8fb 35%, #fdf3f3 70%, #f9f0f5 100%);
        font-family: 'Lora', serif;
        color: #4a3f45;
    }

    .main-container {
        max-width: 860px;
        margin: 0 auto;
        padding: 10px 12px 40px 12px;
    }

    .title {
        font-family: 'Playfair Display', serif;
        font-size: 52px;
        text-align: center;
        color: #a85d6e;
        margin: 30px 0 8px 0;
        letter-spacing: 1px;
        animation: fadeInDown 0.9s ease-out;
    }

    .subtitle {
        text-align: center;
        font-size: 19px;
        color: #7a6a72;
        font-style: italic;
        margin-bottom: 6px;
        animation: fadeInUp 0.9s ease-out 0.25s both;
    }

    .tiny-line {
        text-align: center;
        font-size: 13px;
        color: #b08a97;
        font-style: italic;
        margin-bottom: 28px;
    }

    .date-pill {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 999px;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(212, 165, 176, 0.4);
        font-size: 13px;
        color: #85646f;
        margin-bottom: 40px;
        box-shadow: 0 6px 18px rgba(168, 93, 110, 0.15);
        backdrop-filter: blur(10px);
        animation: fadeIn 0.8s ease-out 0.4s both;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 34px;
        color: #a85d6e;
        text-align: center;
        margin: 70px 0 40px 0;
        position: relative;
        animation: fadeIn 0.8s ease-out;
    }

    .section-title::after {
        content: '';
        display: block;
        width: 110px;
        height: 2px;
        background: linear-gradient(to right, transparent, #d4a5b0, transparent);
        margin: 18px auto 0 auto;
        border-radius: 1px;
    }

    .section-title::before {
        content: '✦';
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        top: -26px;
        font-size: 18px;
        color: #d4a5b0;
        opacity: 0.7;
    }

    .letter-card, .sweet-card, .memory-card, .future-card {
        background: rgba(255, 255, 255, 0.96);
        backdrop-filter: blur(16px);
        border-radius: 26px;
        padding: 32px 32px 30px 32px;
        margin: 20px 0;
        box-shadow: 0 12px 40px rgba(168, 93, 110, 0.14);
        border: 1px solid rgba(212, 165, 176, 0.28);
        transition: all 0.4s ease;
        animation: fadeInUp 0.6s ease-out;
    }

    .letter-card:hover, .future-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 18px 55px rgba(168, 93, 110, 0.18);
    }

    .letter-header {
        font-family: 'Dancing Script', cursive;
        font-size: 26px;
        color: #a85d6e;
        margin-bottom: 16px;
    }

    .text-content {
        font-size: 18px;
        line-height: 1.9;
        color: #5a4a50;
    }

    .signature {
        margin-top: 26px;
        font-weight: 500;
        letter-spacing: 1px;
    }

    .sweet-card {
        text-align: center;
        font-size: 18.5px;
        color: #7a5d68;
        background: linear-gradient(135deg, rgba(255, 250, 252, 0.96), rgba(253, 243, 247, 0.98));
        position: relative;
        overflow: hidden;
        padding: 22px 32px;
    }

    .sweet-card::before {
        content: '"';
        position: absolute;
        top: -18px;
        left: 24px;
        font-size: 78px;
        color: #f3c6d4;
        opacity: 0.27;
        font-family: 'Playfair Display', serif;
    }

    .sweet-card:hover {
        transform: translateY(-4px) scale(1.01);
        box-shadow: 0 14px 42px rgba(168, 93, 110, 0.16);
    }

    .sweet-index {
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: #b28a99;
        margin-bottom: 6px;
    }

    .memory-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.97), rgba(253, 248, 250, 0.97));
        padding: 0;
        overflow: hidden;
        margin: 30px 0;
        animation: fadeInUp 0.8s ease-out;
    }

    .memory-card:hover {
        transform: translateY(-6px) scale(1.005);
        box-shadow: 0 20px 55px rgba(168, 93, 110, 0.2);
    }

    .memory-header {
        padding: 26px 32px 18px 32px;
    }

    .memory-title {
        font-family: 'Dancing Script', cursive;
        font-size: 27px;
        font-weight: 600;
        color: #a85d6e;
        margin-bottom: 10px;
        text-align: center;
    }

    .memory-text {
        font-size: 17px;
        line-height: 1.8;
        color: #5a4a50;
        text-align: center;
        font-style: italic;
    }

    .memory-image-container {
        position: relative;
        margin: 0;
        padding: 0 20px 22px 20px;
        display: flex;
        justify-content: center;
    }

    .memory-image-wrapper {
        position: relative;
        border-radius: 18px;
        overflow: hidden;
        box-shadow: 0 10px 36px rgba(168, 93, 110, 0.18);
        border: 6px solid white;
        transition: all 0.4s ease;
        max-width: 230px;
        width: 100%;
    }

    .memory-image-wrapper:hover {
        box-shadow: 0 15px 46px rgba(168, 93, 110, 0.26);
        transform: scale(1.02);
    }

    .memory-image-wrapper::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(to bottom, transparent 50%, rgba(168, 93, 110, 0.06) 100%);
        pointer-events: none;
    }

    .memory-image-wrapper img {
        display: block;
        width: 100%;
        height: auto;
        border-radius: 12px;
    }

    .heart-decoration {
        position: fixed;
        font-size: 20px;
        opacity: 0.16;
        animation: float 6s ease-in-out infinite;
        pointer-events: none;
        color: #d4a5b0;
        z-index: -1;
    }

    .footer {
        text-align: center;
        color: #9a8a92;
        font-size: 15px;
        margin: 80px 0 40px 0;
        font-style: italic;
        animation: fadeIn 1s ease-out;
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #d4a5b0, transparent);
        margin: 70px 0 40px 0;
    }

    html {
        scroll-behavior: smooth;
    }

    /* TIMER STYLES */
    .timer-container {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.97), rgba(253, 248, 250, 0.97));
        border-radius: 24px;
        padding: 32px;
        margin: 40px 0;
        text-align: center;
        box-shadow: 0 12px 40px rgba(168, 93, 110, 0.12);
        border: 1px solid rgba(212, 165, 176, 0.3);
        animation: fadeInUp 0.8s ease-out;
    }

    .timer-title {
        font-family: 'Dancing Script', cursive;
        font-size: 32px;
        color: #a85d6e;
        margin-bottom: 10px;
    }

    .timer-subtitle {
        font-size: 16px;
        color: #7a6a72;
        font-style: italic;
        margin-bottom: 26px;
    }

    .timer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }

    .timer-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 18px;
        padding: 20px 15px;
        border: 1px solid rgba(212, 165, 176, 0.25);
        box-shadow: 0 6px 20px rgba(168, 93, 110, 0.1);
        transition: all 0.3s ease;
    }

    .timer-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(168, 93, 110, 0.15);
    }

    .timer-value {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        font-weight: 700;
        color: #a85d6e;
        margin-bottom: 5px;
        text-shadow: 1px 1px 2px rgba(168, 93, 110, 0.1);
    }

    .timer-label {
        font-size: 14px;
        color: #85646f;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    .timer-divider {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        color: #d4a5b0;
        font-weight: 300;
        margin: 0 10px;
    }

    .anniversary-box {
        background: linear-gradient(135deg, #f8d7e3, #f3c6d4);
        color: white;
        border-radius: 18px;
        padding: 25px 20px;
        margin: 30px 0 10px 0;
        border: none;
        box-shadow: 0 8px 30px rgba(168, 93, 110, 0.2);
    }

    .anniversary-box .timer-value {
        color: white;
        text-shadow: 1px 1px 3px rgba(168, 93, 110, 0.3);
    }

    .anniversary-box .timer-label {
        color: rgba(255, 255, 255, 0.95);
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(26px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-26px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-18px) rotate(4deg); }
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# ---------- HEADER ----------
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Floating hearts decoration
st.markdown(
    """
    <div class="heart-decoration" style="top: 15%; left: 10%;">♡</div>
    <div class="heart-decoration" style="top: 25%; right: 8%; animation-delay: 2s;">♡</div>
    <div class="heart-decoration" style="top: 65%; left: 5%; animation-delay: 4s;">♡</div>
    <div class="heart-decoration" style="top: 85%; right: 12%; animation-delay: 3s;">♡</div>
    """,
    unsafe_allow_html=True
)

# Title & subtitle
st.markdown('<h1 class="title">One Year With You</h1>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">20th December – the day we became <em>us</em>.</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="tiny-line">If you are reading this, it means you chose me again today.</div>',
    unsafe_allow_html=True
)
st.markdown(
    f'<div style="text-align:center;"><span class="date-pill">'
    f'From Imad to Nour Elhouda • {date.today().strftime("%B %d, %Y")}'
    '</span></div>',
    unsafe_allow_html=True
)


# ---------- SMALL CONTROL BAR (MUSIC TOGGLE) ----------
with st.expander("Set the mood ", expanded=False):
    st.write("Turn this on if you want some soft background music while reading.")
    music_on = st.toggle("Play background music")
    if music_on:
        try:
            audio_file = open("media/audio/Hazelwood - Coming Of Age (freetouse.com).mp3", "rb")
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, loop=True)
        except FileNotFoundError:
            st.info("Add a file at `media/audio/soft_music.mp3` to enable music.")

    # Hidden "for later" note
with st.expander("Open this only when you feel sad", expanded=False):
    st.write(
        "I just want to say that I'm very proud of you Nour, for everything you have accomplished and for the bad days you have survived. I know that you don't see it "
        "but you are so strong (and beautiful)."
    )

    # ---------- COUNTDOWN TIMERS ----------
st.markdown('<h2 class="section-title">Our Time Together</h2>', unsafe_allow_html=True)

# Create placeholders for live updating
time_together_placeholder = st.empty()
time_known_placeholder = st.empty()
next_anniversary_placeholder = st.empty()

# Calculate times
days_together, hours_together, minutes_together= calculate_time_together()
days_known, hours_known, minutes_known= calculate_time_known()
days_to_anniversary, hours_to_anniversary, minutes_to_anniversary = calculate_next_anniversary()

with time_together_placeholder.container():
    st.markdown(
        f"""
        <div class="timer-container">
            <div class="timer-title">Together Since December 20, 2024, 12:21 AM</div>
            <div class="timer-subtitle">Every second with you has been a blessing</div>
            <div class="timer-grid">
                <div class="timer-box">
                    <div class="timer-value">{days_together}</div>
                    <div class="timer-label">Days</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value">{hours_together}</div>
                    <div class="timer-label">Hours</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value">{minutes_together}</div>
                    <div class="timer-label">Minutes</div>
                </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with time_known_placeholder.container():
    st.markdown(
        f"""
        <div class="timer-container">
            <div class="timer-title">Known Each Other Since May 5, 2023, 10:02 PM</div>
            <div class="timer-subtitle">From strangers to soulmates</div>
            <div class="timer-grid">
                <div class="timer-box">
                    <div class="timer-value">{days_known}</div>
                    <div class="timer-label">Days</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value">{hours_known}</div>
                    <div class="timer-label">Hours</div>
                </div>
                <div class="timer-box">
                    <div class="timer-value">{minutes_known}</div>
                    <div class="timer-label">Minutes</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )



# ---------- LETTER SECTION ----------
st.markdown('<h2 class="section-title">A Letter for You</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="letter-card">
        <div class="letter-header">My Nour Elhouda,</div>
        <div class="text-content">
        20th December is a day I will always hold close to my heart, the day we became <em>us</em>. 
        I am so proud of that decision, and every single moment with you since then has been PERFECT. 
        You make me the happiest man alive, and I am endlessly grateful for you.<br><br>
        I promise to be by your side through all of life's good days and bad days. Yes, we may sometimes argue, 
        but every disagreement is worth it, because you are the only girl I want, the only one I need. 
        I also want to apologize for the times you went to sleep upset because of me. Please know it was never 
        my intention to cause you the slightest discomfort, your happiness is one of my greatest goals in life.<br><br>
        You are breathtaking, Nour Elhouda, truly stunning. Everything about you is perfect: your laugh, your face, 
        your eyes, your hair… I could go on forever, and still it wouldn't capture all your beauty. 
        But what touches me even more is your heart. You are the kindest, purest, and most innocent soul I have ever known.<br><br>
        I am so grateful to have you in my life a 3ayniya, and I look forward to countless more memories together. 
        You are my love, my joy, and my everything.
        <div class="signature"><br><strong>Forever yours,</strong><br>IMAD</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- DOWNLOAD LETTER AS PDF (fpdf2, simple & safe) ----------
LETTER_TEXT = """My Nour Elhouda

20th December is a day I will always hold close to my heart the day we became us.
I am so proud of that decision, and every single moment with you since then has been perfect.
You make me the happiest man alive, and I am endlessly grateful for you.
I promise to be by your side through all of life's good days and bad days. Yes, we may sometimes argue, but every disagreement is worth it, because you are the only girl I want, the only one I need.
I also want to apologize for the times you went to sleep upset because of me. Please know it was never my intention to cause you the slightest discomfort your happiness is one of my greatest goals in life.
You are breathtaking, Nour Elhouda, truly stunning. Everything about you is perfect: your laugh, your face, your eyes, your hair… I could go on forever, and still it wouldn't capture all your beauty.
But what touches me even more is your heart. You are the kindest, purest, and most innocent soul I have ever known.
I am so grateful to have you in my life, a 3ayniya, and I look forward to countless more memories together.
You are my love, my joy, and my everything.

Forever yours 
IMAD
"""

def build_pdf_bytes(text: str) -> bytes:
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    try:
        pdf.add_font("DejaVu", "", "fonts/DejaVuSans.ttf")
        pdf.set_font("DejaVu", size=12)
    except:
        pdf.set_font("Arial", size=12)

    pdf.multi_cell(0, 8, text)
    return bytes(pdf.output(dest="S"))

pdf_bytes = build_pdf_bytes(LETTER_TEXT)

st.download_button(
    label="Download this letter as PDF",
    data=pdf_bytes,
    file_name="One_Year_With_You_Letter.pdf",
    mime="application/pdf"
)

# ---------- SWEET THINGS SECTION ----------
st.markdown('<h2 class="section-title">Things I Love About You</h2>', unsafe_allow_html=True)

sweet_things = [
    "The way you care about everyone and everything.",
    "Your kindness.",
    "How you believe in me, sometimes more than I believe in myself.",
    "Your honesty. It makes everything feel safe.",
    "The way you feel like home, even from far away.",
    "Your laugh, it lights up my day.",
    "Your creativity.",
    "How you make even ordinary moments special.",
    "Your gorgeous smile.",
    "Your eyes.",
    "YOU"
]

# Extra specific reason (inside joke / very personal)
if "extra_reason_shown" not in st.session_state:
    st.session_state.extra_reason_shown = False

extra_reason = "Not a reason, I just love you so much."

st.markdown(
    """
    <style>
    .romantic-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .love-card {
        background: linear-gradient(135deg, rgba(255, 250, 252, 0.98), rgba(253, 243, 247, 0.98));
        border-radius: 20px;
        padding: 30px 24px;
        text-align: center;
        position: relative;
        overflow: hidden;
        border: 2px solid rgba(212, 165, 176, 0.3);
        box-shadow: 0 8px 32px rgba(168, 93, 110, 0.12);
        transition: all 0.3s ease;
        min-height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .love-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 15px 45px rgba(168, 93, 110, 0.2);
        border-color: rgba(212, 165, 176, 0.5);
    }
    
    .love-card::before {
        content: '♡';
        position: absolute;
        top: 15px;
        font-size: 32px;
        color: rgba(168, 93, 110, 0.15);
        animation: heartPulse 2s ease-in-out infinite;
    }
    
    .love-number {
        position: absolute;
        top: 12px;
        right: 18px;
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, #f3c6d4, #e8a5b5);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 15px;
        box-shadow: 0 4px 12px rgba(168, 93, 110, 0.2);
        font-family: 'Lora', serif;
    }
    
    .love-text {
        font-size: 17px;
        line-height: 1.7;
        color: #5a4a50;
        font-family: 'Lora', serif;
        margin-top: 20px;
        font-weight: 500;
    }
    
    .love-decorative-line {
        width: 40px;
        height: 2px;
        background: linear-gradient(to right, transparent, #d4a5b0, transparent);
        margin: 10px auto 0 auto;
    }
    
    @keyframes heartPulse {
        0%, 100% { 
            transform: scale(1); 
            opacity: 0.15;
        }
        50% { 
            transform: scale(1.2); 
            opacity: 0.25;
        }
    }
    
    .final-love-message {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(253, 243, 247, 0.98));
        border-radius: 24px;
        padding: 40px 32px;
        margin: 40px 0;
        text-align: center;
        border: 2px solid rgba(212, 165, 176, 0.4);
        box-shadow: 0 12px 40px rgba(168, 93, 110, 0.15);
    }
    
    .final-love-title {
        font-family: 'Dancing Script', cursive;
        font-size: 32px;
        color: #a85d6e;
        margin-bottom: 16px;
    }
    
    .final-love-text {
        font-size: 18px;
        line-height: 1.8;
        color: #5a4a50;
        font-family: 'Lora', serif;
    }
    
    .heart-row {
        display: flex;
        justify-content: center;
        gap: 8px;
        margin-top: 20px;
        font-size: 20px;
    }
    
    .heart-row span {
        animation: heartBeat 1.5s ease-in-out infinite;
    }
    
    .heart-row span:nth-child(2) { animation-delay: 0.2s; }
    .heart-row span:nth-child(3) { animation-delay: 0.4s; }
    .heart-row span:nth-child(4) { animation-delay: 0.6s; }
    .heart-row span:nth-child(5) { animation-delay: 0.8s; }
    
    @keyframes heartBeat {
        0%, 100% { transform: scale(1); }
        25% { transform: scale(1.2); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="romantic-grid">', unsafe_allow_html=True)

for idx, thing in enumerate(sweet_things, start=1):
    st.markdown(
        f"""
        <div class="love-card">
            <div class="love-number">{idx}</div>
            <div class="love-text">{thing}</div>
            <div class="love-decorative-line"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

# Button for one more reason
if st.button("Tap for one more reason"):
    st.session_state.extra_reason_shown = True

if st.session_state.extra_reason_shown:
    st.markdown(
        f"""
        <div class="sweet-card" style="margin-top:10px;">
            <div class="text-content">{extra_reason}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Final romantic message
st.markdown(
    """
    <div class="final-love-message">
        <div class="final-love-title">And so much more...</div>
        <div class="final-love-text">
            Every little thing about you makes my heart full. 
            You are everything I could ever wish for and more.
        </div>
        <div class="heart-row">
            <span>❤️</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- MEMORIES SECTION ----------
# ---------- MEMORIES SECTION ----------
st.markdown('<h2 class="section-title">Our Memories</h2>', unsafe_allow_html=True)

memories = [
    {"date": "The First Message", "pov": "That first text is the best thing I have ever done.", "image": "media/images/memory1.jpg"},
    {"date": "Our First Meeting", "pov": "Seeing you for the first time felt surreal. Everything I imagined suddenly became real.", "image": "media/images/memory2.jpg"},
    {"date": "My Hoodie on You", "pov": "This picture still makes me smile. Seeing you in my hoodie made me feel close to you in a quiet, comforting way.", "image": "media/images/memory3.jpg"},
    {"date": "When I Said I Loved You", "pov": "I remember exactly how heavy and real those words felt. Saying them was scary, but it felt honest. And I'm really grateful.", "image": "media/images/memory3_1_love_text.jpg"},
    {"date": "Our First Real Date", "pov": "That sushi date meant more than just going out. I was nervous because meeting you felt important , like something I didn't want to mess up.", "image": "media/images/memory4.jpg"},
    {"date": "L GATEAUUU (super delicious)", "pov": "This made me genuinely happy. It wasn't just what you baked , it was the care and thought behind it that stayed with me.", "image": "media/images/memory5.jpg"},
    {"date": "Your Birthday", "pov": "This is still my favorite picture of you. That day, I felt proud to be with you and grateful to celebrate you.", "image": "media/images/memory6.jpg"},
    {"date": "One Very Good Day", "pov": "It was one of those days that simply felt right.", "image": "media/images/memory7.jpg"},
    {"date": "The Airport", "pov": "This moment means more to me than words. You were there for me during the hardest period of my life, and I will never forget that support.", "image": "media/images/memory8.jpg"},
    {"date": "The Polaroid", "pov": "I love this picture so much. We were secretly holding hands, and every time I look at it, it reminds me how natural being with you feels.", "image": "media/images/memory9.jpg"},
    {"date": "Flowers", "pov": "Seeing you with the flowers I got you always makes me feel good. Your happiness in those moments becomes mine too.", "image": "media/images/memory10.jpg"}
]

for i, m in enumerate(memories):
    st.markdown(
        f"""
        <div class="memory-card">
            <div class="memory-header">
                <div class="memory-title">{m['date']}</div>
                <div class="memory-text">{m['pov']}</div>
            </div>
            <div class="memory-image-container">
                <div class="memory-image-wrapper">
        """,
        unsafe_allow_html=True
    )

    st.image(m['image'], width="stretch")

    st.markdown(
        """
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
# ---------- VIDEO MEMORIES ----------
st.markdown('<h2 class="section-title">Our Video Memories</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="memory-card" style="padding: 34px 26px 30px 26px;">
        <div class="memory-title" style="margin-bottom: 16px;">Every moment with you is beautiful</div>
        <div class="memory-text" style="margin-bottom: 26px;">Every second with you is worth remembering.</div>
    """,
    unsafe_allow_html=True
)

try:
    video_file = open('media/videos/our_video.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)
except FileNotFoundError:
    st.info("Add your video at `media/videos/our_video.mp4` to show it here.")

st.markdown(
    """
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- WHEN YOU MISS ME ----------
miss_messages = [
    "I'm choosing you every day, you are the only girl I want.",
    "Distance is temporary. Us is permanent.",
    "You are loved more than you know.",
    "I'm proud of you. Always.",
    "You are safe in my heart."
]

if st.button("Press here when you miss me"):
    st.markdown(
        f"""
        <div class='sweet-card' style='margin-top:26px;'>
            <div class="text-content">{random.choice(miss_messages)}</div>
            <div style="margin-top:8px; font-size:13px; color:#b08a97; font-style:italic;">
                Always in my heart.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------- FUTURE SECTION ----------
st.markdown('<h2 class="section-title">What Comes Next</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="future-card">
    <div class="text-content">
    No matter what happens in life, my goal is to spend forever with you, and I will keep trying for you every single day.<br><br>
    One year has passed, and I look forward to many more tears, smiles, and unforgettable moments together.<br><br>
    One day, this page will feel like the beginning of a much bigger story.<br><br>
    And I can't wait to write it with you.
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="footer">
        Made with all my heart , Nhabek a BOUMEDEINE Nour Elhouda • {date.today().strftime('%B %d, %Y')}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

# ---------- REAL-TIME AUTO-REFRESH ----------
# This will refresh the page every 1 second to update the timers
refresh_time = 1  # Changed from 10 to 1 second
if time.time() - st.session_state.get('last_refresh', 0) > refresh_time:
    st.session_state.last_refresh = time.time()
    # Use JavaScript to refresh the page
    st.markdown(
        f"""
        <script>
        // Store scroll position before refresh
        const scrollPosition = window.scrollY || window.pageYOffset;
        localStorage.setItem('scrollPosition', scrollPosition);
        
        setTimeout(function() {{
            window.location.reload(1);
        }}, {refresh_time * 1000});
        </script>
        """,
        unsafe_allow_html=True
    )
