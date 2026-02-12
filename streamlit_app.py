import streamlit as st
from datetime import datetime, date

# --- CONFIGURATION ---
st.set_page_config(page_title="H&A Pulse", page_icon="⚡", layout="wide")

# Custom CSS for that "Dubai Premium" Dark Mode Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; }
    .itinerary-card { background-color: #1c1f26; padding: 20px; border-radius: 15px; border-left: 5px solid #FF4B4B; margin-bottom: 10px; }
    h1, h2, h3 { color: #d4af37 !important; } /* Gold accents */
    </style>
    """, unsafe_allow_label_visibility=True)

# --- SIDEBAR: THE COUNTDOWN ---
st.sidebar.title("⏳ The Countdown")
arrival_date = datetime(2026, 2, 16, 14, 0) # Feb 16, 2026 at 2 PM
time_left = arrival_date - datetime.now()

if time_left.days > 0:
    st.sidebar.metric("Days until Aaron lands", f"{time_left.days} Days")
    st.sidebar.write(f"Arrival: Monday, Feb 16th")
else:
    st.sidebar.success("He's in Dubai! 🇦🇪")

# --- MAIN INTERFACE ---
st.title("⚡ H&A Pulse: The Doha-Dubai Bridge")
st.subheader(f"Hasna (Al Quoz) x Aaron (Business Bay)")

tab1, tab2, tab3 = st.tabs(["🌉 Remote Bridge", "📍 The 72-Hour Plan", "🎵 Vibe Check"])

with tab1:
    st.header("Remote Mode: Bridging the Gap")
    st.info("Daily conversation starters to keep the momentum until Feb 16.")
    
    pulses = {
        12: "If we could teleport to a dinner spot right now, where are we going?",
        13: "What’s one thing you're definitely packing that describes your personality?",
        14: "Valentine's Eve: What's the best 'first date' story you've ever heard?",
        15: "What's the first thing you want to say to me when you see me at the airport/hotel?"
    }
    
    today_day = datetime.now().day
    daily_pulse = pulses.get(today_day, "Ready for the Dubai takeover?")
    
    st.markdown(f"> **Today's Pulse:** {daily_pulse}")
    
    st.text_area("Drop a note for Aaron here...", placeholder="Write something spicy or sweet...")
    if st.button("Send to the Cloud"):
        st.toast("Message saved for Aaron!")

with tab2:
    st.header("The Dubai Itinerary (Feb 16-19)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="itinerary-card">
            <h3>Mon 16 Feb: The Business Bay Welcome</h3>
            <p><b>Evening:</b> Drinks at <b>The Guild</b> or <b>Privé</b>.</p>
            <p>Watch the Burj Khalifa sparkle from his 'backyard'.</p>
        </div>
        <div class="itinerary-card">
            <h3>Tue 17 Feb: The Al Quoz Soul</h3>
            <p><b>Morning:</b> Coffee at <b>Nightjar</b> (Alserkal Avenue).</p>
            <p><b>Afternoon:</b> Art gallery hopping and maybe a quick padel match.</p>
        </div>
        """, unsafe_allow_label_visibility=True)

    with col2:
        st.markdown("""
        <div class="itinerary-card">
            <h3>Wed 18 Feb: The Grand Finale</h3>
            <p><b>Sunset:</b> Private boat rental from Business Bay Canal.</p>
            <p><b>Night:</b> Dinner in <b>DIFC</b> (Zuma or Josette).</p>
        </div>
        <div class="itinerary-card">
            <h3>Thu 19 Feb: The See-You-Soon</h3>
            <p><b>Early Morning:</b> Quick breakfast at <b>Cassette</b> Al Quoz.</p>
            <p>Uber to DXB. Back to Doha, but better.</p>
        </div>
        """, unsafe_allow_label_visibility=True)

with tab3:
    st.header("Shared Vibe Board")
    st.write("Collaborative space for music and visuals.")
    
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder for a shared 'Our Song'
    
    st.multiselect("Activities we both want to do:", 
                  ["Desert Safari", "Museum of the Future", "Deep Dive Dubai", "Beach Club Day", "Stay in & Order Joe & The Juice"],
                  default=["Stay in & Order Joe & The Juice"])

st.divider()
st.caption("Built with ❤️ for Hasna & Aaron | Feb 2026")
