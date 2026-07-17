[7/17/2026 9:51 PM] Pavithra Bandara: import streamlit as st

# Configure the web page layout, title, and favicon
st.set_page_config(
    page_title="Testrun2 | Health Assistant",
    page_icon="🚭",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS styling for premium look and card designs
st.markdown("""
<style>
    /* Styling for custom result cards */
    .metric-card {
        background-color: #f8fafc;
        border-left: 5px solid #3b82f6;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 20px;
    }
    .warning-card {
        background-color: #fffbeb;
        border-left: 5px solid #f59e0b;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 20px;
    }
    .danger-card {
        background-color: #fef2f2;
        border-left: 5px solid #ef4444;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 20px;
    }
    .success-card {
        background-color: #f0fdf4;
        border-left: 5px solid #22c55e;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        margin-bottom: 20px;
    }
    /* Polish default Streamlit elements */
    .stTextInput>div>div>input {
        border-radius: 8px;
    }
    .stNumberInput>div>div>input {
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR RESOURCES ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1527137341206-2916b17aa18f?auto=format&fit=crop&w=300&q=80", caption="Your journey to healthy lungs starts here.")
    st.markdown("## 🧠 Health Insights")
    st.info("Did you know? Just 20 minutes after your last cigarette, your heart rate and blood pressure drop back to normal levels.")
    
    st.markdown("---")
    st.markdown("### 📞 Support Hotlines")
    st.caption("If you or a loved one needs immediate quitting support, reach out to local professional cessation coaches or healthcare providers.")

# --- MAIN HERO SECTION ---
st.title("🚭 Testrun2 Health Assistant")
st.markdown("#### *'The secret of getting ahead is getting started!'*")
st.write("Thank you for selecting Testrun2. Let's work together to understand your habits and chart a healthier path forward.")
st.markdown("---")

# --- USER INPUT SECTION (Organized in neat columns) ---
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("👤 What is your name?", placeholder="Type your name here...")

if name:
    with col2:
        y = st.number_input("🚬 Cigarettes Per Day (CPD):", min_value=0, max_value=120, step=1, value=0)

    st.markdown(f"### Welcome, {name}! 👋")
    st.write("Here is your personalized smoking-cessation analysis based on your current daily intake:")

    # --- ANALYSIS LOGIC WITH VISUAL CUSTOM CARDS ---
    if y == 0:
        st.markdown(f"""
        <div class="success-card">
            <h4 style="margin:0; color:#15803d;">🎉 Outstanding, {name}!</h4>
            <p style="margin:5px 0 0 0; color:#166534;">You are currently smoke-free. Keep up the excellent work protecting your health, wealth, and future!</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif 1 <= y <= 5:
        st.markdown(f"""
        <div class="warning-card">
            <h4 style="margin:0; color:#b45309;">⚠️ Light Smoking Analysis</h4>
            <p style="margin:5px 0 0 0; color:#92400e;"><strong>The cigarette does not relieve stress.</strong> It temporarily relieves the nicotine withdrawal that the previous cigarette created.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif 6 <= y <= 10:
        st.markdown(f"""
        <div class="success-card">
[7/17/2026 9:51 PM] Pavithra Bandara: <h4 style="margin:0; color:#15803d;">🔑 Prison Break Mode</h4>
            <p style="margin:5px 0 0 0; color:#166534;">The moment you throw away your last pack, you are not giving up a friend. <strong>You are executing a prison break!</strong> Freedom is waiting.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif 11 <= y <= 15:
        st.markdown(f"""
        <div class="warning-card">
            <h4 style="margin:0; color:#b45309;">💡 A Timeless Truth</h4>
            <p style="margin:5px 0 0 0; color:#92400e;">Remember the words: <em>"A cigarette is a pipe with a fire at one end and a fool at the other."</em> You are worth much more than this cycle.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif 16 <= y <= 20:
        st.markdown(f"""
        <div class="danger-card">
            <h4 style="margin:0; color:#b91c1c;">🚨 The Whole Pack Trap</h4>
            <p style="margin:5px 0 0 0; color:#991b1b;">There is no such thing as "just one cigarette." <strong>One always leads back to the whole pack.</strong> Breaking the absolute first link in the chain is your key to victory.</p>
        </div>
        """, unsafe_allow_html=True)
        
    elif y >= 21:
        st.markdown(f"""
        <div class="danger-card">
            <h4 style="margin:0; color:#b91c1c;">⚠️ Professional Intervention Advised</h4>
            <p style="margin:5px 0 0 0; color:#991b1b;">Seeking help means you are ready to make a change. <strong>Please consider taking professional medical support immediately.</strong> Remember, it is never too late to start!</p>
        </div>
        """, unsafe_allow_html=True)

    # --- MOTIVATIONAL FOOTER ---
    st.markdown("---")
    st.subheader("Do not smoke your future away. Your health is the only true wealth you have! ❤️")
    st.caption("#quitsmoking #healthyfuture #testrun2")
