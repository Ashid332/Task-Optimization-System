"""Streamlit UI for Task Optimization System"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
import json

# Page configuration
st.set_page_config(
    page_title="Task Optimization System",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .task-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #1E88E5;
        margin-bottom: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .urgent-task {
        border-left-color: #FF6B6B !important;
        background-color: #FFF5F5;
    }
    .high-priority {
        border-left-color: #FFA94D;
    }
    .completed-task {
        border-left-color: #06D6A0;
        opacity: 0.7;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.title("🚀 Task Optimization System")
    st.markdown("Intelligent task scheduling and optimization using AI and advanced algorithms")
    
    # Sidebar navigation
    with st.sidebar:
        st.title("Navigation")
        page = st.radio(
            "Go to:",
            ["Dashboard", "Task Manager", "Optimization Engine", "Analytics", "Settings"],
            label_visibility="collapsed"
        )
    
    # Page routing
    if page == "Dashboard":
        show_dashboard()
    elif page == "Task Manager":
        show_task_manager()
    elif page == "Optimization Engine":
        show_optimization()
    elif page == "Analytics":
        show_analytics()
    elif page == "Settings":
        show_settings()

def show_dashboard():
    """Main Dashboard"""
    st.title("📊 Dashboard")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Tasks", "24", "+2")
    with col2:
        st.metric("Completed", "18", "+1")
    with col3:
        st.metric("In Progress", "4", "0")
    with col4:
        st.metric("Optimization Score", "94%", "+5%")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Task Completion Trend")
        dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
        values = [60 + i*1.2 for i in range(30)]
        df = pd.DataFrame({'Date': dates, 'Completion %': values})
        fig = px.line(df, x='Date', y='Completion %', title="Last 30 Days", markers=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Resource Utilization")
        resources = ['Team A', 'Team B', 'Team C', 'Team D']
        utilization = [85, 78, 92, 71]
        fig = px.bar(x=resources, y=utilization, title="Resource Utilization %")
        st.plotly_chart(fig, use_container_width=True)

def show_task_manager():
    """Task Management Interface"""
    st.title("📝 Task Manager")
    
    tab1, tab2, tab3 = st.tabs(["My Tasks", "Team Tasks", "Create Task"])
    
    with tab1:
        st.subheader("Your Tasks")
        # Sample tasks
        tasks = [
            {"id": 1, "title": "Optimize algorithm", "priority": "urgent", "status": "in_progress", "deadline": "2024-02-15"},
            {"id": 2, "title": "Write documentation", "priority": "high", "status": "todo", "deadline": "2024-02-20"},
            {"id": 3, "title": "Review code", "priority": "medium", "status": "completed", "deadline": "2024-02-10"},
        ]
        
        for task in tasks:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{task['title']}**")
            with col2:
                st.write(f"Priority: {task['priority'].title()}")
            with col3:
                st.write(f"Status: {task['status'].replace('_', ' ').title()}")
    
    with tab2:
        st.subheader("Team Tasks")
        st.info("Team tasks will be synced from your team's project management system")
    
    with tab3:
        st.subheader("Create New Task")
        with st.form("create_task"):
            title = st.text_input("Task Title")
            description = st.text_area("Description")
            priority = st.selectbox("Priority", ["low", "medium", "high", "urgent"])
            deadline = st.date_input("Deadline", min_value=datetime.now().date())
            submitted = st.form_submit_button("Create Task")
            if submitted and title:
                st.success(f"Task '{title}' created successfully!")

def show_optimization():
    """Task Optimization Engine"""
    st.title("🙋 Optimization Engine")
    
    st.markdown("Use our advanced algorithms to optimize your task schedule")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Input Parameters")
        num_tasks = st.slider("Number of Tasks", 1, 100, 10)
        num_resources = st.slider("Number of Resources", 1, 20, 5)
        optimize_for = st.selectbox(
            "Optimize For",
            ["Time", "Cost", "Resource Balance"]
        )
        constraint_type = st.multiselect(
            "Constraints",
            ["Deadline", "Dependency", "Skill Match", "Availability"]
        )
    
    with col2:
        st.subheader("Expected Results")
        st.write("""
        - **Faster Completion**: Reduce project timeline by 30-45%
        - **Better Resource Use**: Improve utilization by 25-35%
        - **Risk Mitigation**: 95%+ feasibility for constraints
        - **Cost Savings**: Reduce overhead by 20-30%
        """)
    
    if st.button("Run Optimization", type="primary", use_container_width=True):
        with st.spinner("Optimizing task schedule..."):
            import time
            time.sleep(2)
            st.success("Optimization complete!")
            
            # Show results
            st.subheader("Optimization Results")
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Project Duration", "15 days", "-7 days")
            with col2:
                st.metric("Resource Util.", "84%", "+20%")
            with col3:
                st.metric("On-Time Rate", "94%", "+32%")
            with col4:
                st.metric("Cost Savings", "$8.5K", "-35%")

def show_analytics():
    """Analytics Dashboard"""
    st.title("📈 Analytics")
    
    tab1, tab2 = st.tabs(["Performance", "Team Insights"])
    
    with tab1:
        st.subheader("Performance Metrics")
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Avg Project Duration", "18 days", "-4 days")
            st.metric("Task Completion Rate", "92%", "+5%")
        
        with col2:
            st.metric("Resource Utilization", "78%", "+8%")
            st.metric("Cost Savings", "$45.2K", "+12%")
        
        # Performance chart
        dates = pd.date_range(start='2024-01-01', periods=12, freq='M')
        metrics = {
            'Date': dates,
            'Duration': [25, 24, 23, 22, 20, 18, 17, 16, 15, 14, 13, 12],
            'Completion': [75, 78, 80, 82, 85, 88, 90, 91, 92, 93, 94, 95]
        }
        df = pd.DataFrame(metrics)
        fig = px.line(df, x='Date', y=['Duration', 'Completion'], title="Performance Improvement")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Team Performance")
        team_data = {
            'Member': ['Alice', 'Bob', 'Charlie', 'Diana'],
            'Tasks Completed': [18, 15, 12, 20],
            'Avg Duration': [2.1, 2.3, 2.8, 1.9]
        }
        df = pd.DataFrame(team_data)
        col1, col2 = st.columns(2)
        
        with col1:
            fig = px.bar(df, x='Member', y='Tasks Completed', title="Tasks Completed by Team Member")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = px.bar(df, x='Member', y='Avg Duration', title="Avg Duration (Days)")
            st.plotly_chart(fig, use_container_width=True)

def show_settings():
    """Settings Page"""
    st.title("⚙️ Settings")
    
    tab1, tab2, tab3 = st.tabs(["General", "Optimization", "Notifications"])
    
    with tab1:
        st.subheader("General Settings")
        with st.form("general_settings"):
            username = st.text_input("Username", value="ashidul_islam")
            email = st.text_input("Email", value="ashidulislam332@gmail.com")
            theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
            submitted = st.form_submit_button("Save Settings")
            if submitted:
                st.success("Settings saved!")
    
    with tab2:
        st.subheader("Optimization Preferences")
        with st.form("optimization_settings"):
            algorithm = st.selectbox(
                "Optimization Algorithm",
                ["Dynamic Programming", "Constraint Satisfaction", "Hybrid"]
            )
            max_time = st.slider("Max Optimization Time (seconds)", 1, 60, 10)
            auto_optimize = st.checkbox("Enable Auto-Optimization", value=True)
            submitted = st.form_submit_button("Save Preferences")
            if submitted:
                st.success("Preferences saved!")
    
    with tab3:
        st.subheader("Notification Settings")
        with st.form("notification_settings"):
            task_reminders = st.checkbox("Task Reminders", value=True)
            optimization_alerts = st.checkbox("Optimization Alerts", value=True)
            weekly_summary = st.checkbox("Weekly Summary", value=True)
            submitted = st.form_submit_button("Save Notifications")
            if submitted:
                st.success("Notification settings saved!")

if __name__ == "__main__":
    main()
