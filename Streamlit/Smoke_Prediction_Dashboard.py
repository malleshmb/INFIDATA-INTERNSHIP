import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title('Smoke Prediction Dashboard')
st.markdown('The dashboard will help a reseacher to get to know \ more about the give datasets and its output')

#sidebar
st.sidebar.title('Select Visual Charts')
st.sidebar.markdown('Select the charts/plots accordingly:')

data=pd.read_csv('demo_data_set.csv')

chart_visual=st.sidebar.selectbox('Select charts/plots type',
                                  ('Line chart','Bar chart','Bubble chart'))
st.sidebar.checkbox('Show Analysis by smoking Status',True)
select_status=st.sidebar.selectbox('Select Smoking status',
                                   options=['Formerly_smoked','Smokes','Never_Smoked','Unknown'])

fig=go.Figure()
if chart_visual=="Line chart":
    if select_status=='Formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,
                                 mode="lines",
                                 name='Formerly_smoked'))
    elif select_status=='Smokes':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,
                                 mode="lines",
                                 name='Smokes'))

    elif select_status=='Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Never_Smoked,
                                 mode="lines",
                                 name='Never_Smoked'))

    elif select_status=='Unknown':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Unknown,
                                 mode="lines",
                                 name='Unknown'))

elif chart_visual == "Bar chart":
    if select_status == 'Formerly_smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.formerly_smoked,
                                 name='Formerly_smoked'))
    elif select_status == 'Smokes':
        fig.add_trace(go.Bar(x=data.Country, y=data.Smokes,
                                 name='Smokes'))

    elif select_status == 'Never_Smoked':
        fig.add_trace(go.Bar(x=data.Country, y=data.Never_Smoked,
                                 name='Never_Smoked'))

    elif select_status == 'Unknown':
        fig.add_trace(go.Bar(x=data.Country, y=data.Unknown,
                                 name='Unknown'))

if chart_visual=="Bubble chart":
    if select_status=='Formerly_smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.formerly_smoked,
                                 mode="markers",
                                 marker_size=[40.60,80,60,40,50],
                                 name='Formerly_smoked'))
    elif select_status=='Smokes':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Smokes,
                                 mode="markers",
                                 marker_size=[40.60, 80, 60, 40, 50],
                                 name='Smokes'))

    elif select_status=='Never_Smoked':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Never_Smoked,
                                 mode="markers",
                                 marker_size=[40.60, 80, 60, 40, 50],
                                 name='Never_Smoked'))

    elif select_status=='Unknown':
        fig.add_trace(go.Scatter(x=data.Country,y=data.Unknown,
                                 mode="markers",
                                 marker_size=[40.60, 80, 60, 40, 50],
                                 name='Unknown'))



st.plotly_chart(fig, use_container_width=True)