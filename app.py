import streamlit as st
import pandas as pd
from ai_analyzer import analyze_prospect
from email_generator import generate_email
from datetime import datetime
import os

# Configuración de la página
st.set_page_config(
    page_title="Sales Copilot AI",
    layout="wide",
    page_icon="🤖"
)

# CSS personalizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        margin: 0.5rem 0;
    }
    .security-warning {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 5px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🤖 Sales Copilot AI</h1>
    <h3>AI-Powered Sales Assistant</h3>
    <p>Transform prospect data into winning sales strategies</p>
</div>
""", unsafe_allow_html=True)

# Función para obtener API key de forma segura
def get_api_key():
    """
    Obtiene la API key de forma segura:
    1. Streamlit Secrets (producción)
    2. Environment variables
    3. User input (solo desarrollo)
    """
    # Primero intentar desde Streamlit Secrets
    try:
        if hasattr(st, 'secrets') and 'OPENAI_API_KEY' in st.secrets:
            return st.secrets['OPENAI_API_KEY']
    except:
        pass
    
    # Luego desde environment variables
    env_key = os.getenv('OPENAI_API_KEY')
    if env_key:
        return env_key
    
    # Finalmente desde user input (solo para desarrollo)
    return None

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    
    # Obtener API key de forma segura
    api_key_from_secrets = get_api_key()
    
    if api_key_from_secrets:
        st.success("🔑 API Key loaded securely from environment")
        openai_api_key = api_key_from_secrets
        # Ocultar input si la key ya está cargada
        st.info("API Key loaded from secure source")
    else:
        st.warning("⚠️ Enter API Key for development")
        openai_api_key = st.text_input(
            "OpenAI API Key:",
            type="password",
            help="Get your API key from https://platform.openai.com"
        )
        if openai_api_key:
            st.success("🔑 API Key entered")
    
    st.header("🎯 Your Offer")
    products = st.text_area(
        "Products/Services:",
        value="SaaS enterprise solutions, Digital transformation consulting, Cloud implementation services, Technical support and maintenance",
        height=100
    )
    
    st.header("🏢 Your Company")
    company_name = st.text_input("Company Name:", value="TechSolutions MX")
    company_industry = st.selectbox("Your Industry:", ["Technology", "Consulting", "Software", "IT Services"])

# Security warning
if not openai_api_key:
    st.markdown("""
    <div class="security-warning">
        <strong>⚠️ Security Notice:</strong> For production use, set your OpenAI API key as an environment variable 
        or use Streamlit Secrets. Never commit API keys to version control.
    </div>
    """, unsafe_allow_html=True)

# Main application tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🔍 Analyze Prospect", 
    "📧 Generate Email", 
    "💼 Sales Pipeline", 
    "🚀 Quick Analysis"
])

with tab1:
    st.header("🔍 Complete Prospect Analysis")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Prospect Information")
        
        with st.form("prospect_form"):
            # Basic information
            name = st.text_input("Full Name:*", placeholder="e.g., Ana López Rodríguez")
            company = st.text_input("Current Company:*", placeholder="e.g., TechRetail Solutions")
            position = st.text_input("Position:*", placeholder="e.g., Technology Director")
            industry = st.selectbox("Company Industry:", 
                                  ["Technology", "Finance", "Manufacturing", "Healthcare", "Retail", "Services", "Other"])
            
            # Advanced information
            st.subheader("Advanced Details (Optional)")
            company_size = st.selectbox("Company Size:", 
                                      ["Don't know", "Startup (1-10)", "SMB (11-50)", "Mid-Market (51-200)", "Enterprise (201+)"])
            location = st.text_input("Location:", placeholder="e.g., Mexico City")
            
            # Context information
            st.subheader("Prospect Context")
            pain_points = st.text_area(
                "Known Pain Points/Needs:",
                placeholder="e.g., Legacy systems not scaling, high operational costs, integration challenges...",
                height=80
            )
            
            objectives = st.text_area(
                "Known Objectives/Goals:",
                placeholder="e.g., Digital transformation, cost reduction, market expansion...",
                height=80
            )
            
            additional_info = st.text_area(
                "Additional Relevant Information:",
                placeholder="e.g., Recently secured funding, expanding team, showed interest in AI solutions...",
                height=60
            )
            
            submitted = st.form_submit_button("🧠 Analyze Prospect with AI", type="primary")
    
    with col2:
        st.subheader("AI Analysis & Strategy")
        
        if submitted:
            if not all([name, company, position]):
                st.error("❌ Please complete at least the required fields (*)")
            elif not openai_api_key:
                st.error("❌ Configure your OpenAI API key in the sidebar")
            else:
                # Build prospect data
                prospect_data = f"""
                PROSPECT: {name}
                COMPANY: {company} ({industry})
                POSITION: {position}
                COMPANY SIZE: {company_size}
                LOCATION: {location}
                KNOWN PAIN POINTS: {pain_points}
                OBJECTIVES: {objectives}
                ADDITIONAL INFORMATION: {additional_info}
                """
                
                company_context = f"{company_name} ({company_industry})"
                
                with st.spinner("🤖 Analyzing prospect and generating strategy..."):
                    analysis = analyze_prospect(prospect_data, products, company_context, openai_api_key)
                    
                    if not analysis.startswith("Error"):
                        st.session_state.current_analysis = analysis
                        st.session_state.prospect_data = prospect_data
                        st.success("✅ Analysis generated!")
                        
                        # Display analysis
                        st.subheader("🎯 Generated Sales Strategy")
                        st.markdown(analysis)
                        
                        # Action buttons
                        col_act1, col_act2, col_act3 = st.columns(3)
                        with col_act1:
                            if st.button("📋 Copy Analysis"):
                                st.code(analysis, language="markdown")
                                st.success("✅ Analysis copied to clipboard")
                        with col_act2:
                            if st.button("📧 Generate Email"):
                                st.session_state.generate_email = True
                        with col_act3:
                            if st.button("💾 Save Prospect"):
                                st.success("✅ Prospect saved to pipeline")
                    else:
                        st.error(analysis)

with tab2:
    st.header("📧 Email Outreach Generator")
    
    st.info("Generate highly personalized outreach emails for your prospects")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Email Context")
        email_objective = st.selectbox("Email Objective:", 
                                     ["Initial outreach", "Follow-up", "Demo invitation", "Proposal follow-up", "Relationship building"])
        email_tone = st.selectbox("Tone:", ["Professional", "Friendly", "Urgent", "Consultative"])
        
        prospect_name = st.text_input("Prospect Name:")
        prospect_company = st.text_input("Prospect Company:")
        prospect_position = st.text_input("Prospect Position:")
        
    with col2:
        st.subheader("Generated Email")
        
        if st.button("🔄 Generate Email", type="primary") and openai_api_key:
            if not prospect_name:
                st.error("Enter at least the prospect name")
            else:
                email_context = f"""
                Prospect: {prospect_name}
                Company: {prospect_company}
                Position: {prospect_position}
                Objective: {email_objective}
                Tone: {email_tone}
                """
                
                with st.spinner("Crafting perfect email..."):
                    email = generate_email(email_context, products, company_name, openai_api_key)
                    
                    if not email.startswith("Error"):
                        st.markdown(f"```\n{email}\n```")
                        
                        if st.button("📋 Copy Email to Clipboard"):
                            st.code(email, language="markdown")
                            st.success("✅ Email copied to clipboard")
                    else:
                        st.error(email)

with tab3:
    st.header("💼 Sales Pipeline")
    
    st.info("🚧 Pipeline management functionality coming soon!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Active Prospects")
        st.write("Future home for your sales pipeline")
        
    with col2:
        st.subheader("Key Metrics")
        st.metric("Prospects in Pipeline", "0")
        st.metric("Conversion Rate", "0%")
        st.metric("Pipeline Value", "$0")

with tab4:
    st.header("🚀 Quick Analysis")
    
    st.info("Need fast insights? Analyze with minimal information")
    
    quick_info = st.text_area(
        "What you know about the prospect:",
        placeholder="e.g., IT Director at retail company, mentioned scalability issues, interested in cloud solutions...",
        height=100
    )
    
    if st.button("⚡ Quick Analysis", type="primary") and openai_api_key and quick_info:
        with st.spinner("Analyzing available information..."):
            quick_data = f"QUICK INFO: {quick_info}"
            analysis = analyze_prospect(quick_data, products, company_name, openai_api_key)
            
            if not analysis.startswith("Error"):
                st.markdown(analysis)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Sales Copilot AI</strong> • Developed by Omar Cordero</p>
    <p>AI-powered sales intelligence 🚀</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_analysis' not in st.session_state:
    st.session_state.current_analysis = None
if 'prospect_data' not in st.session_state:
    st.session_state.prospect_data = None
if 'generate_email' not in st.session_state:
    st.session_state.generate_email = False