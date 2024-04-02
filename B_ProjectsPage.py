import streamlit as st
import json as js

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
    

if 'project_name' not in st.session_state:
    st.session_state['project_name'] = ''

if 'project_description' not in st.session_state:
    st.session_state['project_description'] = ''
if 'project_id' not in st.session_state:
    st.session_state['project_id'] = 1000
if 'name_list' not in st.session_state:
    st.session_state['name_list'] = []

def add_project(ID, name, description):
    d = {
        'id' : ID,
        'name': name,
        'description': description,
    }

    try:
        with open('database/ProjectObj.json') as file_in:
            data = js.load(file_in)
    except (FileNotFoundError, js.JSONDecodeError):
        data = []

    data.append(d)
    with open('database/ProjectObj.json', 'w') as file_out:
        js.dump(data, file_out, indent=4)

    st.session_state['name_list'].append(st.session_state['project_name'])
    st.session_state['project_name'] = ''
    st.session_state['project_description'] = ''
    st.session_state['project_id'] = st.session_state['project_id'] + 1

st.title('Projects')

st.text_input('Project Name',key='project_name', value=st.session_state['project_name'])
st.text_input('Project Description',key='project_description', value=st.session_state['project_description'])


st.button(label='Add Project', on_click=add_project, args= (st.session_state['project_id'], st.session_state['project_name'], st.session_state['project_description']))

st.subheader("Current Projects")

try:
    with open('database/ProjectObj.json') as file_in:
        data = js.load(file_in)
        for i in range(len(data)):
            st.write(data[i]['name'])
except (FileNotFoundError, js.JSONDecodeError):
    data = []
