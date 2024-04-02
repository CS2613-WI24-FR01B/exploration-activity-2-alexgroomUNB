import streamlit as st

st.set_page_config(page_title="Exploration Activity 2")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.page_link("app.py", label="Home")

with col2:
    st.page_link("pages/A_CriteriaPage.py", label="Criteria")

with col3:
    st.page_link("pages/B_ProjectsPage.py", label="Projects")

with col4:
    st.page_link("pages/C_RankingPage.py", label="Rank")
with col5:
    st.page_link("pages/D_ChartsPage.py", label="Charts")

st.markdown("""
            **Using the App**

            This app allows companies to input weighted criteria and projects to choose the best option

            Steps:
            1. Select the 'Criteria' tab and input all desired criteria one-by-one with their respective weight's.
            2. Select the 'Projects' tab and input all projects one-by-one to be considered for analysis. Rank each project based on the criteria.
            3. Select the 'Rank' tab, for each project there will be a drop down to rank each criteria (1-10) for each project. Once you are finished ALL rankings press the confirm button
            4. Select the 'Charts' tab to view project comparisons.
            
            """)
