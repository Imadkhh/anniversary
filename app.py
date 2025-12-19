import streamlit as st
from datetime import date

# ---------- PASSWORD PROTECTION ----------
PASSWORD = "290403"  # CHANGE THIS TO YOUR DESIRED PASSWORD

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.markdown(
        """
        <style>
        body {
            background: linear-gradient(135deg, #fff8f8 0%, #fdf3f3 50%, #faf5f7 100%);
            font-family: 'Lora', serif;
        }
        .password-container {
            max-width: 400px;
            margin: 150px auto;
            padding: 40px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 24px;
            box-shadow: 0 10px 35px rgba(168, 93, 110, 0.15);
            text-align: center;
            border: 1px solid rgba(212, 165, 176, 0.3);
        }
        .password-title {
            font-family: 'Playfair Display', serif;
            font-size: 36px;
            color: #a85d6e;
            margin-bottom: 20px;
        }
        .password-subtitle {
            font-size: 18px;
            color: #7a6a72;
            margin-bottom: 30px;
            font-style: italic;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="password-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="password-title">❤️</h1>', unsafe_allow_html=True)
    st.markdown('<p class="password-subtitle">This page is just for you, my love.<br>Enter the password to continue.</p>', unsafe_allow_html=True)

    password_input = st.text_input("Password", type="password", label_visibility="collapsed")

    if st.button("Enter"):
        if password_input == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password. Try again, a chaba ❤️")

    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()  # Stop execution until authenticated

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="One Year With You ya NOUR ELHOUDA",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS WITH ROMANTIC AESTHETIC ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Lora:wght@400;500;600&family=Dancing+Script:wght@600&display=swap');

    body {
        background: linear-gradient(135deg, #fff8f8 0%, #fdf3f3 50%, #faf5f7 100%);
        font-family: 'Lora', serif;
        color: #4a3f45;
    }

    .main-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
    }

    .title {
        font-family: 'Playfair Display', serif;
        font-size: 52px;
        text-align: center;
        color: #a85d6e;
        margin: 50px 0 15px 0;
        letter-spacing: 1px;
        animation: fadeInDown 1s ease-out;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #7a6a72;
        font-style: italic;
        margin-bottom: 70px;
        animation: fadeInUp 1s ease-out 0.3s both;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
        color: #a85d6e;
        text-align: center;
        margin: 80px 0 50px 0;
        position: relative;
        animation: fadeIn 0.8s ease-out;
    }

    .section-title::after {
        content: '';
        display: block;
        width: 100px;
        height: 2px;
        background: linear-gradient(to right, transparent, #d4a5b0, transparent);
        margin: 20px auto;
        border-radius: 1px;
    }

    /* Decorative hearts */
    .section-title::before {
        content: '✦';
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        top: -30px;
        font-size: 18px;
        color: #d4a5b0;
        opacity: 0.6;
    }

    .letter-card, .sweet-card, .memory-card, .future-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        border-radius: 24px;
        padding: 35px;
        margin: 25px 0;
        box-shadow: 0 10px 35px rgba(168, 93, 110, 0.1);
        border: 1px solid rgba(212, 165, 176, 0.25);
        transition: all 0.4s ease;
        animation: fadeInUp 0.6s ease-out;
    }

    .letter-card:hover, .future-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 45px rgba(168, 93, 110, 0.15);
    }

    .text-content {
        font-size: 18px;
        line-height: 1.9;
        color: #5a4a50;
    }

    .sweet-card {
        text-align: center;
        font-size: 18.5px;
        color: #7a5d68;
        background: linear-gradient(135deg, rgba(255, 250, 252, 0.95), rgba(253, 243, 247, 0.95));
        position: relative;
        overflow: hidden;
        padding: 30px 40px;
    }

    .sweet-card::before {
        content: '"';
        position: absolute;
        top: -10px;
        left: 20px;
        font-size: 80px;
        color: #f3c6d4;
        opacity: 0.3;
        font-family: 'Playfair Display', serif;
    }

    .sweet-card:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 40px rgba(168, 93, 110, 0.12);
    }

    .memory-card {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(253, 248, 250, 0.95));
        padding: 0;
        overflow: hidden;
        margin: 40px 0;
        animation: fadeInUp 0.8s ease-out;
    }

    .memory-card:hover {
        transform: translateY(-10px) scale(1.01);
        box-shadow: 0 20px 50px rgba(168, 93, 110, 0.18);
    }

    .memory-header {
        padding: 35px 35px 25px 35px;
    }

    .memory-title {
        font-family: 'Dancing Script', cursive;
        font-size: 28px;
        font-weight: 600;
        color: #a85d6e;
        margin-bottom: 15px;
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
        padding: 0 20px 20px 20px;
        display: flex;
        justify-content: center;
    }

    .memory-image-wrapper {
        position: relative;
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 30px rgba(168, 93, 110, 0.15);
        border: 6px solid white;
        transition: all 0.4s ease;
        max-width: 200px;
        width: 100%;
    }

    .memory-image-wrapper:hover {
        box-shadow: 0 12px 40px rgba(168, 93, 110, 0.25);
        transform: scale(1.02);
    }

    .memory-image-wrapper::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(to bottom, transparent 50%, rgba(168, 93, 110, 0.03) 100%);
        pointer-events: none;
    }

    .memory-image-wrapper img {
        display: block;
        width: 100%;
        height: auto;
        border-radius: 10px;
    }

    /* Floating hearts animation */
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }

    .heart-decoration {
        position: fixed;
        font-size: 20px;
        opacity: 0.15;
        animation: float 6s ease-in-out infinite;
        pointer-events: none;
        color: #d4a5b0;
    }

    .footer {
        text-align: center;
        color: #9a8a92;
        font-size: 16px;
        margin: 100px 0 50px 0;
        font-style: italic;
        animation: fadeIn 1s ease-out;
    }

    hr {
        border: none;
        height: 1px;
        background: linear-gradient(to right, transparent, #d4a5b0, transparent);
        margin: 80px 0;
    }

    /* Smooth scroll behavior */
    html {
        scroll-behavior: smooth;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes fadeInUp {
        from { 
            opacity: 0;
            transform: translateY(30px);
        }
        to { 
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeInDown {
        from { 
            opacity: 0;
            transform: translateY(-30px);
        }
        to { 
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Staggered animations for memory cards */
    .memory-card:nth-child(1) { animation-delay: 0.1s; }
    .memory-card:nth-child(2) { animation-delay: 0.2s; }
    .memory-card:nth-child(3) { animation-delay: 0.3s; }

    /* Hide Streamlit's default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Progress indicator */
    .scroll-indicator {
        position: fixed;
        top: 0;
        left: 0;
        height: 4px;
        background: linear-gradient(to right, #a85d6e, #d4a5b0);
        z-index: 9999;
        transition: width 0.2s ease;
    }
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

st.markdown('<h1 class="title">One Year With You</h1>', unsafe_allow_html=True)

# ---------- LETTER SECTION ----------
st.markdown('<h2 class="section-title">A Letter for You</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="letter-card">
    <div class="text-content">
    My Nour Elhouda,<br><br>
    20th December is a day I will always hold close to my heart—the day we became <em>us</em>. I am so proud of that decision, and every single moment with you since then has been PERFECT. You make me the happiest man alive, and I am endlessly grateful for you.<br><br>
    I promise to be by your side through all of life’s good days and bad days. Yes, we may sometimes argue, but every disagreement is worth it, because you are the only girl I want, the only one I need. I also want to apologize for the times you went to sleep upset because of me. Please know it was never my intention to cause you the slightest discomfort—your happiness is one of my greatest goals in life.<br><br>
    You are breathtaking, Nour Elhouda—truly stunning. Everything about you is perfect: your laugh, your face, your eyes, your hair… I could go on forever, and still it wouldn’t capture all your beauty. But what touches me even more is your heart. You are the kindest, purest, and most innocent soul I have ever known.<br><br>
    I am so grateful to have you in my life a 3ayniya, and I look forward to countless more memories together. You are my love, my joy, and my everything.<br><br>
    <strong>Forever yours,</strong><br>
    IMAD
    </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------- SWEET THINGS SECTION ----------
st.markdown('<h2 class="section-title">Things I Love About You</h2>', unsafe_allow_html=True)

sweet_things = [
    "The way you care about everyone and everything.",
    "Your kindness.",
    "How you believe in me, sometimes more than I believe in myself.",
    "Your honesty. It makes everything feel safe.",
    "The way you feel like home, even from far away.",
    "Your laugh—it lights up my day.",
    "Your creativity.",
    "How you make even ordinary moments special.",
    "Your gorgeous smile.",
    "Your eyes",
    "The way you look at me.",
    "YOU"
]

for thing in sweet_things:
    st.markdown(f'<div class="sweet-card"><div class="text-content">{thing}</div></div>', unsafe_allow_html=True)

# ---------- MEMORIES SECTION ----------
st.markdown('<h2 class="section-title">Our Memories</h2>', unsafe_allow_html=True)

memories = [
    {"date": "The First Message", "pov": "That first text is the best thing i have ever done ", "image": "media/images/memory1.jpg"},
    {"date": "Our First Meeting", "pov": "Seeing you for the first time felt surreal. Everything I imagined suddenly became real, and in that moment, the distance felt smaller.", "image": "media/images/memory2.jpg"},
    {"date": "My Hoodie on You", "pov": "This picture still makes me smile. Seeing you in my hoodie made me feel close to you in a quiet, comforting way.", "image": "media/images/memory3.jpg"},
    {"date": "When I Said I Loved You", "pov": "I remember exactly how heavy and real those words felt. Saying them was scary, but it felt honest. And im really grateful", "image": "media/images/memory3_1_love_text.jpg"},
    {"date": "Our First Real Date", "pov": "That sushi date meant more than just going out. I was nervous because meeting you felt important — like something I didn't want to mess up.", "image": "media/images/memory4.jpg"},
    {"date": "L GATEAUUU (super delecious)", "pov": "This made me genuinely happy. It wasn't just what you baked — it was the care and thought behind it that stayed with me.", "image": "media/images/memory5.jpg"},
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
    
    st.image(m['image'], use_container_width=True)
    
    st.markdown(
        """
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<h2 class="section-title">Our Video Memories</h2>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="memory-card" style="padding: 40px;">
        <div class="memory-title" style="margin-bottom: 25px;">A Moment Captured in Time</div>
        <div class="memory-text" style="margin-bottom: 30px;">Every second with you is worth remembering.</div>
    """,
    unsafe_allow_html=True
)

# Video player
video_file = open('media/videos/our_video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)

st.markdown(
    """
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
    One year has passed, and I look forward to many more tears, smiles, and unforgettable moments together, <em>Inchallah a chaba</em>.<br><br>
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