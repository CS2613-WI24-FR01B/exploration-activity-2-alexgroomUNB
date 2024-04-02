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
    
try:
    with open('database/ChartData.json', 'r') as file_in:
        chart_config = js.load(file_in)['Chart_Config']
        chart_config_json = js.dumps(chart_config)
        
except (FileNotFoundError, js.JSONDecodeError):
    st.write('No data for charts')

# Embed Chart.js in Streamlit
html_template = f"""
<div>
    <canvas id="myChart"></canvas>
</div>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {chart_config_json});
</script>
"""

st.components.v1.html(html_template, height=500)
