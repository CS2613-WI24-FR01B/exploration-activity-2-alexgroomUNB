import streamlit as st
import json as js
import subprocess

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.page_link('app.py', label='Home')

with col2:
    st.page_link('pages/A_CriteriaPage.py', label='Criteria')

with col3:
    st.page_link('pages/B_ProjectsPage.py', label='Projects')

with col4:
    st.page_link('pages/C_RankingPage.py', label='Rank')
with col5:
    st.page_link('pages/D_ChartsPage.py', label='Charts')
    

with open('database/CriteriaObj.json') as file_in:
    criteria = js.load(file_in)
with open('database/ProjectObj.json') as file_in:
    projects = js.load(file_in)

if 'rankings' not in st.session_state:
    st.session_state.rankings = {}

for project in projects:
    with st.expander(f"{project['name']}"):
        
        if 'criteria_rankings' not in project:
            project['criteria_rankings'] = []

        for crit in criteria:
            key = f"proj_{project['id']}_crit_{crit['id']}" 
            ranking = st.slider(f"Rank for {crit['name']}", min_value=1, max_value=10, step=1, key=key, value=5)
            st.session_state.rankings[key] = ranking

            ranking_obj = next((r for r in project['criteria_rankings'] if r['id'] == crit['id']), None)
            if ranking_obj:
                ranking_obj['ranking'] = ranking
            else:
                project['criteria_rankings'].append({'id': crit['id'], 'name': crit['name'], 'weight': crit['weight'], 'ranking': ranking})

node_path = 'node'  # This should work if Node.js is correctly installed and in your system's PATH
script_path = 'javascript/FunctionalProcessing.js'  # Relative path to your script from the project root

def save_project_rankings():
    
    with open('database/ProjectObj.json', 'w') as file_out:
        js.dump(projects, file_out, indent=4)
    result = subprocess.run([node_path, script_path], capture_output=True, text=True, cwd='./')

    # Handle the output
    if result.stdout:
        st.text(result.stdout)
    if result.stderr:
        st.error(result.stderr)

st.button(label='Confirm Rankings', on_click=save_project_rankings)
