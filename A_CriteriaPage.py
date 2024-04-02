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
    
    
if 'criterion_name' not in st.session_state:
    st.session_state['criterion_name'] = ''

if 'criterion_weight' not in st.session_state:
    st.session_state['criterion_weight'] = 0
if 'criterion_id' not in st.session_state:
    st.session_state['criterion_id'] = 2000

def log_criterion(ID, name, weight):
    d = {
        'id': ID,
        'name': name,
        'weight': weight
    }

    try:
        with open('database/CriteriaObj.json') as file_in:
            data = js.load(file_in)
    except (FileNotFoundError, js.JSONDecodeError):
        data = []

    data.append(d)
    with open('database/CriteriaObj.json', 'w') as file_out:
        js.dump(data, file_out, indent=4)

    st.session_state['criterion_id'] = st.session_state['criterion_id'] + 1
    st.session_state['criterion_name'] = ''
    st.session_state['criterion_weight'] = 0
    

st.title('Sequential Criteria Input')

st.text_input(label='Criterion Name',key='criterion_name', value=st.session_state['criterion_name'])
st.number_input(label='Weight Criteria', key='criterion_weight', value=st.session_state['criterion_weight'])

st.button('Log Criterion', on_click=log_criterion, args = (st.session_state['criterion_id'], st.session_state['criterion_name'], st.session_state['criterion_weight'] ))