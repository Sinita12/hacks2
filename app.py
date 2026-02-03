import streamlit as st
import pandas as pd
from utils.scoring import calculate_score
from datetime import datetime

st.set_page_config(
    page_title="EcoScore",
    page_icon="🌱",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- HEADER ----------
st.markdown(
    """
    <h1 style='text-align:center;'>🌱 EcoScore</h1>
    <p style='text-align:center; font-size:18px;'>
    Understand <b>your impact on the environment</b> — one habit at a time.
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------- HOW IT WORKS ----------
st.header("How It Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### 1️⃣ Log Habits")
    st.caption("Plastic, transport, diet, and energy use")

with col2:
    st.markdown("### 2️⃣ EcoScore")
    st.caption("Instant score from 0–100")

with col3:
    st.markdown("### 3️⃣ Insights")
    st.caption("Personalized sustainability tips")

with col4:
    st.markdown("### 4️⃣ Progress")
    st.caption("Track improvement over time")

st.markdown("---")

# ---------- INPUT + OUTPUT LAYOUT ----------
left, right = st.columns([1, 1])

# ---------- INPUT ----------
with left:
    st.subheader("📝 Log Today’s Habits")

    plastic = st.slider("Plastic items used today", 0, 10, 3)

    transport = st.selectbox(
        "Primary transport",
        ["Walking/Cycling", "Public Transport", "Car"]
    )

    diet = st.selectbox(
        "Diet today",
        ["Vegan", "Vegetarian", "Mixed", "Meat-heavy"]
    )

    energy = st.slider("Electricity usage (hours)", 0, 24, 6)

    calculate = st.button("🌍 Calculate My Impact")

# ---------- RESULTS ----------
with right:
    if calculate:
        score, tips = calculate_score(plastic, transport, diet, energy)

        # Store history
        st.session_state.history.append({
            "Date": datetime.now().strftime("%d %b %H:%M"),
            "EcoScore": score
        })

        st.subheader("🌍 Your Environmental Impact")

        st.metric("EcoScore", f"{score}/100")

        if score >= 75:
            st.success("Low impact 🌿 You're doing great!")
        elif score >= 50:
            st.warning("Moderate impact ⚡ Some changes can help.")
        else:
            st.error("High impact 🚨 Immediate action recommended.")

        st.markdown("**What you can improve:**")
        if tips:
            for tip in tips:
                st.write("•", tip)
        else:
            st.write("Amazing — no major improvements needed today!")

# ---------- PROGRESS TRACKING ----------
if st.session_state.history:
    st.markdown("---")
    st.header("📊 Your Sustainability Progress")

    df = pd.DataFrame(st.session_state.history)

    st.line_chart(
        df.set_index("Date")["EcoScore"],
        height=300
    )

    st.caption("EcoScore trend — higher is better 🌱")

    with st.expander("📄 View raw history"):
        st.dataframe(df)
