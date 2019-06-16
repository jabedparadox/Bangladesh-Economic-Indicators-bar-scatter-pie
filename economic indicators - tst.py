#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3

# -*- coding: utf8 -*-
# 
# date                 :- 
# author               :- Md Jabed Ali(jabed)
#':='  eg: string := ''

import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import pandas
import os
import time

readcsv = pandas.read_csv('economic indicators.csv', sep=',')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

bar1 = go.Bar(
    x = readcsv['Year'],
    y = readcsv['GDP'],
    name='GDP (Bil. US$ PPP)'
)
bar2 = go.Bar(
    x = readcsv['Year'],
    y = readcsv['GDP per capita'],
    name='GDP per capita (US$ PPP)'
)
bar3 = go.Bar(
    x = readcsv['Year'],
    y = readcsv['GDP growth'],
    name='GDP growth'
)
bar4 = go.Bar(
    x = readcsv['Year'],
    y = readcsv['Inflation rate'],
    name='Inflation rate (Percent)'
)
bar5 = go.Bar(
    x = readcsv['Year'],
    y = readcsv['Government debt'],
    name='Government debt (% of GDP)'
)

data = [bar1, bar2, bar3, bar4, bar5]

layout = go.Layout(
    title=go.layout.Title(
        text='Bangladesh Economic Indicators.',
        xref='paper',
        x=0
    ),
    barmode='stack',
    xaxis=go.layout.XAxis(
        title=go.layout.xaxis.Title(
            text='Year',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    ),
    yaxis=go.layout.YAxis(
        title=go.layout.yaxis.Title(
            text='Value',
            font=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            )
        )
    )
)


#pie_view_budget = 
#scatter_view_budget = 

app.layout = html.Div([
    dcc.Graph(id='bar_plot',
              figure=go.Figure(data=data,
                               layout=layout)
              )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
