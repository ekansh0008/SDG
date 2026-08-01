"""
Streamlit Web App for SDG Group Discussion AI Agent.
Enables students/participants to access Phase I, II, and III strategies instantly from any browser/phone.
"""

import streamlit as st
from sdg_agent.config import SDG_DATA, EVALUATION_CRITERIA
from sdg_agent.phase1_prioritisation import generate_phase1_strategy
from sdg_agent.phase2_policy import generate_phase2_analysis
from sdg_agent.phase3_poa import generate_phase3_poa

st.set_page_config(
    page_title="SDG GD AI Coach",
    page_icon="🌍",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .card {
        background-color: #F8FAFC;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2563EB;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-header">🌍 SDG Based Group Discussion (GD) AI Coach</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your intelligent companion for Phase I (Negotiation), Phase II (Policy Analysis), & Phase III (Plan of Action)</p>', unsafe_allow_html=True)

# Sidebar Configuration
st.sidebar.header("⚙️ Competition Settings")

sdg_option = st.sidebar.selectbox(
    "Select Designated SDG",
    options=["SDG 5 – Gender Equality", "SDG 9 – Industry, Innovation & Infrastructure", "SDG 13 – Climate Action"],
    index=0
)

sdg_map = {
    "SDG 5 – Gender Equality": "5",
    "SDG 9 – Industry, Innovation & Infrastructure": "9",
    "SDG 13 – Climate Action": "13"
}
chosen_sdg = sdg_map[sdg_option]

phase_option = st.sidebar.radio(
    "Select Competition Phase",
    options=[
        "Phase I: Prioritisation & Negotiation (25 Marks)",
        "Phase II: Policy Analysis (40 Marks)",
        "Phase III: Plan of Action / PoA (35 Marks)"
    ]
)

data = SDG_DATA[chosen_sdg]

st.sidebar.markdown("---")
st.sidebar.info(f"**Active Focus:**\n\n**{data['title']}**\n\n*{data['tagline']}*")

# Main Content Area
if "Phase I" in phase_option:
    st.markdown(f"## 🗣️ Phase I: SDG Prioritisation & Negotiation")
    st.markdown(f"*Target Goal: **{data['title']}** — Total: {EVALUATION_CRITERIA['phase1']['marks']} Marks*")
    
    strat = generate_phase1_strategy(chosen_sdg)
    
    st.markdown("### 💬 Opening Advocacy Hook")
    st.info(f'"{strat["opening_hook"]}"')
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### ⚡ Urgency")
        st.write(strat["urgency_argument"])
    with col2:
        st.markdown("### 🛠️ Feasibility & Policy")
        st.write(strat["feasibility_argument"])
        st.write(f"**Policy Relevance:** {strat['policy_relevance']}")
        
    st.markdown("### ⚖️ Comparative Advantages vs Other Goals")
    for comp in strat["comparisons"]:
        st.markdown(f"- **Vs {comp['vs']}:** {comp['argument']}")
        
    st.markdown("### 🤝 Consensus-Building Statement")
    st.success(f'"{strat["consensus_builder"]}"')

elif "Phase II" in phase_option:
    st.markdown(f"## 📊 Phase II: Policy Analysis & Discussion")
    st.markdown(f"*Target Goal: **{data['title']}** — Total: {EVALUATION_CRITERIA['phase2']['marks']} Marks*")
    
    analysis = generate_phase2_analysis(chosen_sdg)
    
    for dim, content in analysis['dimensions'].items():
        with st.container():
            st.markdown(f"### 📌 {dim}")
            if isinstance(content, list):
                for item in content:
                    st.markdown(f"- {item}")
            else:
                st.write(content)
            st.markdown("")

else:
    st.markdown(f"## 📋 Phase III: Lobbying & Plan of Action (PoA)")
    st.markdown(f"*Target Goal: **{data['title']}** — Total: {EVALUATION_CRITERIA['phase3']['marks']} Marks*")
    
    team_name = st.text_input("Enter your Team Name", value="Team SDG-Champions")
    poa = generate_phase3_poa(chosen_sdg, team_name)
    
    st.markdown(f"### Proposal by: `{poa['team_name']}` for `{poa['selected_sdg']}`")
    
    for sec, desc in poa['sections'].items():
        with st.expander(f"🔹 {sec}", expanded=True):
            st.write(desc)

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built for SDG Group Discussion Competition | Powered by AI Agent System</p>", unsafe_allow_html=True)
