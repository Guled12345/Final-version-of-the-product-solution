import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from utils.data_utils import load_student_data, load_parent_observations
from utils.model_utils import load_model, make_prediction

# Configure Streamlit page
st.set_page_config(
    page_title="EduScan - Learning Difficulties Detection Tool",
    page_icon="⭕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS matching the HTML design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Reset and base styles */
    .stApp {
        font-family: 'Poppins', sans-serif !important;
        background: linear-gradient(rgba(248, 250, 252, 0.95), rgba(248, 250, 252, 0.95)), 
                    url('data:image/jpeg;base64,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');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Hide default Streamlit elements */
    .stDeployButton {display: none;}
    #MainMenu {visibility: hidden;}
    .stHeader {display: none;}
    .stToolbar {display: none;}
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: white !important;
        border-right: 1px solid #e5e7eb !important;
    }
    
    .css-1lcbmhc .css-1outpf7 {
        background-color: white !important;
    }
    
    /* Main content area */
    .main .block-container {
        background-color: #f8fafc !important;
        padding: 1.5rem !important;
        max-width: none !important;
    }
    
    /* Dashboard cards */
    .dashboard-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .dashboard-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
    }
    
    .card-header {
        display: flex;
        justify-content: between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .card-icon {
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-left: auto;
    }
    
    .icon-blue { background-color: #dbeafe; color: #2563eb; }
    .icon-green { background-color: #dcfce7; color: #16a34a; }
    .icon-yellow { background-color: #fef3c7; color: #d97706; }
    .icon-red { background-color: #fee2e2; color: #dc2626; }
    
    .card-number {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.25rem;
    }
    
    .card-label {
        color: #6b7280;
        font-size: 0.875rem;
    }
    
    .card-title {
        color: #6b7280;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Section containers */
    .section-container {
        background: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.5rem;
    }
    
    .section-title {
        font-size: 1.125rem;
        font-weight: 600;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    
    /* Assessment items */
    .assessment-item {
        display: flex;
        align-items: center;
        padding: 0.75rem;
        background: #f9fafb;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .assessment-icon {
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
    }
    
    .assessment-content {
        flex: 1;
    }
    
    .assessment-title {
        font-weight: 500;
        color: #1f2937;
        font-size: 0.875rem;
        margin-bottom: 0.25rem;
    }
    
    .assessment-subtitle {
        color: #6b7280;
        font-size: 0.75rem;
    }
    
    .assessment-time {
        color: #1f2937;
        font-size: 0.875rem;
        font-weight: 500;
    }
    
    /* Student cards */
    .student-item {
        display: flex;
        align-items: center;
        padding: 0.75rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    
    .student-item.high-risk { background: #fef2f2; }
    .student-item.medium-risk { background: #fefbf0; }
    .student-item.low-risk { background: #f0fdf4; }
    
    .student-avatar {
        width: 2.5rem;
        height: 2.5rem;
        border-radius: 50%;
        background: #e5e7eb;
        margin-right: 1rem;
    }
    
    .student-info {
        flex: 1;
    }
    
    .student-name {
        font-weight: 500;
        color: #1f2937;
        font-size: 0.875rem;
        margin-bottom: 0.25rem;
    }
    
    .student-details {
        color: #6b7280;
        font-size: 0.75rem;
    }
    
    .risk-badge {
        padding: 0.25rem 0.625rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .risk-high { background: #fee2e2; color: #991b1b; }
    .risk-medium { background: #fef3c7; color: #92400e; }
    .risk-low { background: #dcfce7; color: #166534; }
    
    /* View all links */
    .view-all-link {
        color: #2563eb;
        font-size: 0.875rem;
        font-weight: 500;
        text-decoration: none;
    }
    
    .view-all-link:hover {
        color: #1d4ed8;
    }
    
    /* Page header */
    .page-header {
        background: white;
        padding: 1rem 1.5rem;
        border-bottom: 1px solid #e5e7eb;
        margin: -1.5rem -1.5rem 2rem -1.5rem;
    }
    
    .page-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1f2937;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

def create_sidebar():
    """Create sidebar navigation matching the HTML design"""
    with st.sidebar:
        # Logo and title
        st.markdown("""
        <div style="padding: 1rem 0; border-bottom: 1px solid #e5e7eb; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center;">
                <div style="background: #2563eb; color: white; padding: 0.5rem; border-radius: 0.5rem; margin-right: 0.75rem;">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"/>
                    </svg>
                </div>
                <div>
                    <h1 style="font-size: 1.25rem; font-weight: 700; color: #1f2937; margin: 0;">EduScan</h1>
                    <p style="font-size: 0.75rem; color: #6b7280; margin: 0;">Learning Difficulties Detection Tool</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu
        st.markdown("### Navigation")
        
        # Create navigation buttons
        pages = [
            "Dashboard",
            "Students", 
            "Assessment Form",
            "Teacher Resources",
            "Parent Activities",
            "Settings"
        ]
        
        # Get current page from session state
        if 'current_page' not in st.session_state:
            st.session_state.current_page = 'Dashboard'
        
        # Navigation buttons
        for page_name in pages:
            if st.button(page_name, key=page_name, use_container_width=True):
                if page_name == "Assessment Form":
                    st.switch_page("pages/01_Prediction.py")
                elif page_name == "Teacher Resources":
                    st.switch_page("pages/02_Teacher_Resources.py")
                elif page_name == "Parent Activities":
                    st.switch_page("pages/03_Parent_Tracker.py")
                elif page_name == "Settings":
                    st.switch_page("pages/04_Educational_Content.py")
                else:
                    st.session_state.current_page = page_name
                    st.rerun()
        
        # User info at bottom
        st.markdown("---")
        st.markdown("""
        <div style="display: flex; align-items: center; padding: 1rem 0;">
            <div style="width: 2rem; height: 2rem; border-radius: 50%; background: #e5e7eb; margin-right: 0.75rem;"></div>
            <div>
                <p style="font-size: 0.875rem; font-weight: 500; color: #1f2937; margin: 0;">Guled Mohamed</p>
                <p style="font-size: 0.75rem; color: #6b7280; margin: 0;">Teacher</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_dashboard_cards():
    """Create dashboard statistics cards using native Streamlit components"""
    try:
        student_data = load_student_data()
        total_students = len(student_data) if student_data else 42
        
        if student_data:
            risk_predictions = [s.get('prediction', 0) for s in student_data]
            at_risk = sum(1 for p in risk_predictions if p == 1)
            on_track = total_students - at_risk
            intervention = min(4, at_risk)  # Assume some at-risk students need intervention
        else:
            total_students = 42
            on_track = 28
            at_risk = 10
            intervention = 4
    except:
        total_students = 42
        on_track = 28
        at_risk = 10
        intervention = 4
    
    # Create four columns for the metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Students",
            value=total_students,
            help="Total number of students in the system"
        )
    
    with col2:
        st.metric(
            label="On Track",
            value=on_track,
            delta=f"{(on_track/total_students*100):.1f}%" if total_students > 0 else "0%",
            help="Students performing well academically"
        )
    
    with col3:
        st.metric(
            label="At Risk",
            value=at_risk,
            delta=f"-{(at_risk/total_students*100):.1f}%" if total_students > 0 else "0%",
            delta_color="inverse",
            help="Students who may need additional support"
        )
    
    with col4:
        st.metric(
            label="Need Intervention",
            value=intervention,
            delta=f"-{(intervention/total_students*100):.1f}%" if total_students > 0 else "0%",
            delta_color="inverse",
            help="Students requiring immediate intervention"
        )

def create_performance_chart():
    """Create class performance overview chart"""
    subjects = ['Reading', 'Writing', 'Math', 'Science', 'Social', 'Art', 'Music', 'Physical', 'Language']
    performance = [65, 80, 45, 70, 65, 90, 60, 75, 50]
    
    fig = go.Figure(data=[
        go.Bar(
            x=subjects,
            y=performance,
            marker_color='#2563eb',
            text=[f"{p}%" for p in performance],
            textposition='outside',
            textfont=dict(size=12, color='#6b7280'),
            marker_line=dict(width=0)
        )
    ])
    
    fig.update_layout(
        title=None,
        xaxis_title="",
        yaxis_title="",
        yaxis=dict(
            range=[0, 100], 
            showticklabels=False,
            showgrid=False,
            zeroline=False
        ),
        xaxis=dict(
            tickfont=dict(size=12, color='#6b7280', family='Poppins'),
            showgrid=False,
            zeroline=False
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Poppins', size=12),
        margin=dict(l=0, r=0, t=40, b=0),
        height=300,
        showlegend=False
    )
    
    return fig

def create_recent_assessments():
    """Create recent assessments section using native Streamlit components"""
    st.subheader("Recent Assessments")
    
    # Create a dataframe for assessments
    assessments_data = {
        "Assessment": ["Reading Comprehension", "Basic Mathematics", "Language Development"],
        "Grade": ["Grade 3", "Grade 2", "Grade 1"],
        "Students": [24, 18, 22],
        "Date": ["Today", "Yesterday", "2 days ago"],
        "Status": ["Completed", "Completed", "Completed"]
    }
    
    assessments_df = pd.DataFrame(assessments_data)
    st.dataframe(assessments_df, use_container_width=True, hide_index=True)

def create_students_needing_attention():
    """Create students needing attention section using native Streamlit components"""
    st.subheader("Students Needing Attention")
    
    # Create a dataframe for at-risk students
    students_data = {
        "Student Name": ["Amina Hassan", "Mohamed Ali", "Farah Jama"],
        "Grade": ["Grade 3", "Grade 2", "Grade 3"],
        "Issue": ["Reading Difficulties", "Math Difficulties", "Attention Issues"],
        "Risk Level": ["High Risk", "Medium Risk", "Medium Risk"]
    }
    
    students_df = pd.DataFrame(students_data)
    
    # Color code the risk levels
    def highlight_risk(val):
        if val == "High Risk":
            return 'background-color: #fee2e2; color: #991b1b'
        elif val == "Medium Risk":
            return 'background-color: #fef3c7; color: #92400e'
        else:
            return 'background-color: #dcfce7; color: #166534'
    
    styled_df = students_df.style.applymap(highlight_risk, subset=['Risk Level'])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

def main():
    # Create page header
    st.title("Dashboard")
    
    # Create sidebar
    create_sidebar()
    
    # Dashboard content
    st.header("Overview")
    create_dashboard_cards()
    
    st.divider()
    
    # Performance chart
    st.header("Class Performance Overview")
    with st.container():
        fig = create_performance_chart()
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    st.divider()
    
    # Bottom grid sections
    col1, col2 = st.columns(2)
    
    with col1:
        create_recent_assessments()
    
    with col2:
        create_students_needing_attention()

if __name__ == "__main__":
    main()